#!/usr/bin/env python3

'''Wait for Cozmo to see a face, and then register face.

This is a script to show off faces, and how they are easy to use.
It waits for a face, and then will register when that face is visible.
'''

import asyncio
import time
import cozmo

def register_face(robot: cozmo.robot.Robot):

    # Move lift down and tilt the head up
    robot.move_lift(-3)
    robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

    face = None

    print("Press CTRL-C to quit")

    while True:
        if face and face.is_visible:
            face.name_face(face_name)
            print("Registered " + face.name)
            return
        else:
            # Wait until we we can see another face
            try:
                face = robot.world.wait_for_observed_face(timeout=30)
            except asyncio.TimeoutError:
                print("Didn't find a face.")
                return

        time.sleep(.1)

global face_name
face_name = input("Face Name: ")

cozmo.run_program(register_face, use_viewer=True, force_viewer_on_top=True)
