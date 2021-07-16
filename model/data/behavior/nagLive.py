from model.data.behavior.behaviorLive import BehaviorLive
from model.data.cell import Cell
from model.data.behavior.classicDie import ClassicDie
from model.data.color import Color
import random


class NagLive(BehaviorLive):
    def __init__(self):
        BehaviorLive.__init__(self)

    def live(self):
        if not self.__liveExtended(0, -1):
            if not self.__liveExtended(-1, -1):
                if not self.__liveExtended(-1, 0):
                    if not self.__liveExtended(-1, 1):
                        if not self.__liveExtended(0, 1):
                            if not self.__liveExtended(1, 1):
                                if not self.__liveExtended(1, 0):
                                    if not self.__liveExtended(1, -1):
                                        self.getCell().setBehaviorLive(ClassicDie())

    def __liveExtended(self, x, y):
        if self.getCell().getPetri().isSquareFree(self.getCell().getX() + x, self.getCell().getY() + y):
            newColor = Color(self.getCell().getColor().getRed(),
                             self.getCell().getColor().getGreen(),
                             self.getCell().getColor().getBlue())
            newColor.darken(3)
            newCell = Cell(self.getCell().getPetri(), NagLive(),
                           self.getCell().getBirthStep() + 1)
            newCell.setColor(newColor)
            newCell.setX(self.getCell().getX() + x)
            newCell.setY(self.getCell().getY() + y)
            self.getCell().getPetri().addCell(newCell)
            self.getCell().setBehaviorLive(ClassicDie())
            return True
        return False
