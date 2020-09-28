# hotwire
Ever wondered how old computer feel? Imagine being an old first gen Raspberry Pi sitting around, doing nothing, wathcing your friend living happy with purpose... 

Ok, so I wanted to known whether the garage door was left open and monitor our home while we are away. However, I didn't wanted to pay for a stupid alarm system contract and had an old Raspberry Pi getting bored with life. I decided to hookup octocouplers to the old alarm system.
![installed]

The circuit is very simple, a few optocouplers (PC817) to isolate the two system and some resistors to make everyting in spec. 
![cir]
![front]
![back]

There's no point in adding logic on the RPi. Just throw everything at an MQTT server and figure it out from there. I used HomeAssistant to finalize the logic part.
![result]

[installed]:https://github.com/northox/hotwire/raw/master/ "Old Alarm System with rpi board and shield"
[cir]:https://github.com/northox/hotwire/raw/master/ "Circuit"
[front]:https://github.com/northox/hotwire/raw/master/front.jpeg "Front of shield"
[back]:https://github.com/northox/hotwire/raw/master/back.jpeg "back of shield"
[result]:https://github.com/northox/hotwire/raw/master/result.png "Result"
