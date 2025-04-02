#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from settings import *

class Seg:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getXY(self):
        return (self.x, self.y)

    def draw(self, screen):
        x, y = self.x * TILE, self.y * TILE
        screen.draw_box(x, y, x + TILE, y + TILE, r=0, fill=True, color=Color.BLACK)

class Snake:
    def __init__(self):
        self.body = [Seg(5, 5), Seg(5, 6)]
        self.dx, self.dy = 1, 0
        self.t = StopWatch()

    def control(self, btns):
        h = head = self.body[0].getXY()
        bodyXY = [i.getXY() for i in self.body]

        if Button.UP in btns and (h[0], h[1] - 1) not in bodyXY:
            self.dx, self.dy = 0, -1

        elif Button.RIGHT in btns and (h[0] + 1, h[1]) not in bodyXY:
            self.dx, self.dy = 1, 0

        elif Button.DOWN in btns and (h[0], h[1] + 1) not in bodyXY:
            self.dx, self.dy = 0, 1
        
        elif Button.LEFT in btns and (h[0] - 1, h[1]) not in bodyXY:
            self.dx, self.dy = -1, 0

    def draw(self, screen):
        for i in self.body:
            i.draw(screen)

    def addSeg(self):
        end = self.body[-1]
        self.body.append(Seg(end.x, end.y))

    def move(self):
        b = self.body
        hx, hy = b[0].x + self.dx, b[0].y + self.dy
        b.insert(0, Seg(hx, hy))
        del b[-1]

    def tryMove(self):
        if self.t.time() > MOVE_TIMEOUT:
            self.move()
            self.t.reset()

    def getScore(self):
        return len(self.body)

    def isDead(self):
        head = self.body[0]
        if head.x < 0 or head.x > MAX_X or head.y < 0 or head.y > MAX_Y:
            return True
            
        else:
            deadCoords = []
            for i in self.body[1:]:
                deadCoords.append((i.x, i.y))

            if (head.x, head.y) in deadCoords:
                return True

        return False

        
        