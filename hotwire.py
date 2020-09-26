#!/usr/bin/env python
import os
import time
import datetime
from collections import defaultdict
import signal
import RPi.GPIO as GPIO

host = '192.168.1.230'
port = '1883'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sensors = defaultdict(dict)

die('cannot find mosquitto_pub') if 

def publish(s, t):
    os.system('mosquitto_pub -h %s -p %s -t "homeassistant/binary_sensor/%s/state" -m "%s"' % (host, port, t, ("ON" if s else "OFF")))

class Sensor(object):
    def __init__(self, pin, topic):
        self.pin = pin
        self.topic = topic

        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.last_state = self.state = not bool(GPIO.input(self.pin))
        self.last_time = 0
        self.status = [self.__class__.__name__, self.topic, self.state]
        publish(self.state, self.topic)
        self.dirty = True

    def trigger(self):
        self.trig_setup()
        if self.trig_cond(): 
            self.trig_action()

    def trig_setup(self):
        self.dirty = False
        self.state = not bool(GPIO.input(self.pin))

    def trig_action(self):
        self.dirty = True
        self.last_state = self.state
        self.alarm()

    def trig_cond(self):
        return self.last_state != self.state

    def alarm(self):
        self.status = [self.__class__.__name__, self.topic, self.state]

class MotionSensor(Sensor):
    def __init__(self, pin, topic):
        self.last_time = 0
        super(MotionSensor, self).__init__(pin, topic)

    def trigger(self):
        t = time.time()
        self.trig_setup()
        if 20 < t - self.last_time and self.trig_cond():
            self.last_time = t
            self.trig_action()

class DoorSensor(Sensor):
    pass

sensors = defaultdict(dict)
#####################################################
sensors[17] = MotionSensor(17, 'motionLivingRoom')
sensors[21] = DoorSensor(21, 'garageDoor')
sensors[22] = DoorSensor(22, 'frontDoor')
sensors[23] = DoorSensor(23, 'backDoor')
#####################################################

try:
    while(True):
        for pin, sensor in sensors.items():
            sensor.trigger()
            if sensor.dirty: publish(sensor.state, sensor.topic)
        time.sleep(1)

  except sh.ErrorReturnCode as e:
    print(e)

except KeyboardInterrupt:
    print("Quit")

finally:
    GPIO.cleanup()
