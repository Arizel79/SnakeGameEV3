#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from world import *
from settings import *

class Game:
    def __init__(self, ev3):
        self.ev3 = ev3
        self.w = World(self.ev3)
        self.state = "game"
        
        

    def draw(self):

        self.ev3.screen.clear()
        if self.state == "game":
            self.w.draw(self.ev3.screen)
            self.ev3.screen.draw_text((WIDTH // 2) - 20, 0, str(self.w.sn.getScore()),
             text_color=Color.BLACK, background_color=None)

        elif self.state == "paused game":
            # self.w.draw(self.ev3.screen)
            self.ev3.screen.print("Game paused.")

        elif self.state == "game over":
            self.ev3.screen.print("Game over.")
            self.ev3.screen.print("Score: {}".format(self.w.sn.getScore()))

    def checkGameOver(self):
        if self.w.checkGameOver():
            self.state = "game over"
            if BEEP_ON:
                self.ev3.speaker.beep(20)

    def onTick(self):
        self.control()
        if self.state == "game":
            self.w.onTick()
            self.checkGameOver()

        elif self.state == "game over":
            pass
    def newGame(self):
        self.w = World(self.ev3)

    def control(self):
        btns = self.ev3.buttons.pressed()
        if self.state == "game":
            if btns:
                self.w.sn.control(btns)
            if Button.CENTER in btns:
                self.state = "paused game"
                while Button.CENTER in self.ev3.buttons.pressed():
                    pass

        elif self.state == "paused game":
            if Button.CENTER in btns:
                self.state = "game"
                while Button.CENTER in self.ev3.buttons.pressed():
                    pass

        elif self.state == "game over":
            if Button.CENTER in btns:
                while Button.CENTER in self.ev3.buttons.pressed():
                    pass
                self.state = "game"
                self.newGame()
                
        # if Button.CENTER in btns:
        #     print("CENTER")

        # elif Button.UP in btns:
        #     print("UP")
        
        # elif Button.RIGHT in btns:
        #     print("RIGHT")

        # elif Button.DOWN in btns:
        #     print("DOWN")
        
        # elif Button.LEFT in btns:
        #     print("LEFT")

    def mainloop(self):
        while True:
            self.draw()
            self.onTick()
            
            wait(10)