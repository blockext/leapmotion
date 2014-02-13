from __future__ import division

import blockext
from blockext import *

import Leap



@reporter("hands in view")
def get_hands():
    frame = controller.frame()
    return len(frame.hands)

@reporter("fingers in view")
def get_fingers():
    frame = controller.frame()
        return len(frame.fingers)

menu("xyz", ["x", "y", "z"])
menu("handNumber", ["1", "2"])

@reporter("%m.xyz position of hand %m.handNumber")
def hand_pos(xyz="x", handNumber="1"):
    frame = controller.frame()
        if xyz == "x":
            return frame.hands[int(handNumber) - 1].palm_position.x
        elif xyz == "y":
            return frame.hands[int(handNumber) - 1].palm_position.y
        else:
            return frame.hands[int(handNumber) - 1].palm_position.z

menu("xyz", ["x", "y", "z"])

@reporter("%m.xyz position of hand %n")
def finger_pos(xyz="x", fingerNumber=1):
    frame = controller.frame()
        if xyz == "x":
            return frame.hands[int(fingerNumber) - 1].palm_position.x
        elif xyz == "y":
            return frame.hands[int(fingerNumber) - 1].palm_position.y
        else:
            return frame.hands[int(fingerNumber) - 1].palm_position.z

menu("ypr", ["yaw", "pitch", "roll"])
menu("handNumber", ["1", "2"])

@reporter("%m.ypr of hand %m.handNumber")
def hand_ypr(ypr="yaw", handNumber="1"):
    frame = controller.frame()
        if ypr == "yaw":
            return (frame.hands[int(handNumber) - 1].direction.yaw *
                    Leap.RAD_TO_DEG)
        elif ypr == "pitch":
            return (frame.hands[int(handNumber) - 1].direction.pitch *
                    Leap.RAD_TO_DEG)
        else:
            return (frame.hands[int(handNumber) - 1].palm_normal.roll *
                    Leap.RAD_TO_DEG)



controller = Leap.Controller()
blockext.run("Leap Motion", "leap", 3434)

