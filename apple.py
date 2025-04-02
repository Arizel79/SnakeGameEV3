#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from settings import *

class Apple:
    def __init__(self, x, y, score=1):
        self.x = x
        self.y = y
        self.score = score

    def draw(self, screen):
        x, y = self.x * TILE, self.y * TILE
        screen.draw_circle(x + TILE / 2, y + TILE / 2, TILE / 2, fill=True, color=Color.BLACK)