#!/usr/bin/env python3

'''Wait for Cozmo to see a face, and then turn on his backpack light.

This is a script to show off faces, and how they are easy to use.
It waits for a face, and then will light up his backpack when that face is visible.
'''

import asyncio
import time
import cozmo

def register_greet_human_event(_robot: cozmo.robot.Robot):
    global robot
    robot = _robot
    robot.world.add_event_handler(cozmo.faces.EvtFaceAppeared, greet_human)

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    print("Press CTRL-C to quit")

    while True:
        try:
            face = robot.world.wait_for_observed_face(timeout=30, include_existing=True)
        except asyncio.TimeoutError:
            print("Didn't find a face.")
            return
        time.sleep(.1)

def greet_human(evt, face, **kwargs):
    if face and face.is_visible and face.name:
        robot.say_text("Hello " + face.name + ", Happy New Year!!", play_excited_animation=False, use_cozmo_voice=True).wait_for_completed()


cozmo.run_program(register_greet_human_event, use_viewer=True, force_viewer_on_top=True)
