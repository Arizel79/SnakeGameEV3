#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from settings import *
from snake import *
from apple import *
from random import randint



class World:
    def __init__(self, ev3):
        self.ev3 = ev3
        self.sn = Snake()
        self.apples = [Apple(randint(0, MAX_X), randint(0, MAX_Y)) for i in range(NUM_APPLES)]

    def draw(self, screen):
        self.sn.draw(screen)
        for i in self.apples:
            i.draw(screen)

    def onTick(self):
        self.checkSnakeEatApple()
        self.sn.tryMove()

    def addRandomApple(self):
        invalid_coords = []
        for i in self.apples:
            invalid_coords.append((i.x, i.y))
        for i in self.sn.body:
            invalid_coords.append((i.x, i.y))

        while True:
            maybe_x, maybe_y = randint(0, MAX_X), randint(0, MAX_Y)
            if (maybe_x, maybe_y) in invalid_coords:
                pass
            else:
                self.apples.append(Apple(maybe_x, maybe_y))
                break
            
    def checkSnakeEatApple(self):
        head = self.sn.body[0]
        for i in self.apples:
            if i.x == head.x and i.y == head.y:
                self.sn.addSeg()
                self.apples.remove(i)
                if BEEP_ON:
                    self.ev3.speaker.beep(1200)
                self.addRandomApple()
                break

    def checkGameOver(self):
        if self.sn.isDead():
            return True

