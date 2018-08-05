#!/usr/bin/python
import time
from phue import Bridge

b = Bridge('192.168.0.13')

TRANSITIONTIME = 1 * 10
WHITETEMP = 350  # 154 -- 500
WHITEBRIGHT = 255

b.connect()


def lights():
    initial_lights = b.get_light()

    lights = b.get_light_objects("id")
    gang = b.get_group(2, 'lights')
    for light_id in gang:
        l = lights[int(light_id)]
        l.transitiontime = TRANSITIONTIME
        l.on = True
        l.colortemp = WHITETEMP

    time.sleep(TRANSITIONTIME / 10)

    for light_id in gang:
        l = lights[int(light_id)]
        l.transitiontime = TRANSITIONTIME
        l.brightness = WHITEBRIGHT

    time.sleep(180)

    for l in b.get_light_objects():
        light_id = str(l.light_id)
        old_light = initial_lights[light_id]["state"]
        l.transitiontime = TRANSITIONTIME
        l.xy = old_light["xy"]
        l.brightness = old_light["bri"]
        l.on = old_light["on"]

