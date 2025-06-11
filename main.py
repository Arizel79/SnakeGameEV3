#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from game import Game
from settings import *


ev3 = EV3Brick()


ev3.speaker.set_volume(2, which='Beep')
if BEEP_ON:
    ev3.speaker.beep()


def main():
    g = Game(ev3)
    g.mainloop()


if __name__ == "__main__":
    main()
