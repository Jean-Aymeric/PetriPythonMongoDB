from model.data.behavior.behaviorLive import BehaviorLive
from model.data.cell import Cell
from model.data.behavior.classicDie import ClassicDie
from model.data.color import Color


class ClassicLive(BehaviorLive):
    def __init__(self):
        BehaviorLive.__init__(self)

    def live(self):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (x != 0 or y != 0) and self.getCell().getPetri().isSquareFree(self.getCell().getX() + x, self.getCell().getY() + y):
                    newColor = Color(self.getCell().getColor().getRed(),
                                     self.getCell().getColor().getGreen(),
                                     self.getCell().getColor().getBlue())
                    newColor.darken(10)
                    if not (newColor.getRed() == 0 and newColor.getGreen() == 0 and newColor.getBlue() == 0):
                        newCell = Cell(self.getCell().getPetri(), ClassicLive(),
                                       self.getCell().getBirthStep() + 1)
                        newCell.setColor(newColor)
                        newCell.setX(self.getCell().getX() + x)
                        newCell.setY(self.getCell().getY() + y)
                        self.getCell().getPetri().addCell(newCell)
        self.getCell().setBehaviorLive(ClassicDie())

