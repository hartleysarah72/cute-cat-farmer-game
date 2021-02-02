# File Name:  hartley_sarah_final.py
# File Path:  /home/hartleysarah/Python/hartley_sarah_final.py
# Run Command: sudo python3 /home/hartleysarah/Python/hartley_sarah_final.py

# Sarah Hartley
# 12/10/19
# Final Project

from graphics import *
import time
import random
import RPi.GPIO as GPIO
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# Define player character
class cat:
    
    def __init__(self, xloc, yloc, color1, color2, PIX_WIDTH, window):
        self.__xloc = xloc
        self.__yloc = yloc
        self.window = window
        self.color1 = color1
        self.color2 = color2
        self.pixels = []
        self.PIX_WIDTH = PIX_WIDTH
        
        cat = {"0":("green", "green", "green", self.color1, "green", self.color1, "green", "green", "green"),
               "1":("green", "green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green"),
               "2":("green", "green", self.color1, "lightskyblue", self.color1, "lightskyblue", self.color1, "green", "green"),
               "3":("green", "green", self.color1, self.color1, "pink", self.color1, self.color1, "green", "green"),
               "4":("green", "green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green"),
               "5":("green", "green", "green", self.color1, self.color2, self.color1, "green", "green", "green"),
               "6":("green", "green", self.color1, self.color1, self.color2, self.color1, self.color1, "green", "green"),
               "7":("green", "green", "green", self.color1, self.color2, self.color1, "green", self.color1, self.color1),
               "8":("green", "green", "green", self.color1, self.color2, self.color1, "green", "green", self.color1),
               "9":("green", "green", "green", self.color1, self.color2, self.color1, self.color1, self.color1, "green"),
               "10":("green", "green", "green", self.color1, self.color1, self.color1, "green", "green", "green"),
               "11":("green", "green", "green", self.color1, "green", self.color1, "green", "green", "green")}
        
        for j in range(12):
            self.pixels.append([])
            for i in range(9):
                self.pixels[j].append(Rectangle(Point(i*self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.__yloc), Point(i*self.PIX_WIDTH+self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.PIX_WIDTH+self.__yloc)))
                self.pixels[j][i].setFill(cat[str(j)][i])
                self.pixels[j][i].setOutline(cat[str(j)][i])
        
    def myCatDraw(self):
        for row in self.pixels:
            for box in row:
                box.draw(self.window)
    
    def myCatUndraw(self):
        for row in self.pixels:
            for box in row:
                box.undraw()
    
    def myCatMove(self, xdir, ydir):
        self.__xloc += xdir
        self.__yloc += ydir
        for row in self.pixels:
            for box in row:
                box.move(xdir, ydir)
    
    def getX(self):
        return self.__xloc

    def getY(self):
        return self.__yloc
        
    def animateCheer(self):
        for i in range(3):
            self.pixels[6][2].setFill("green")
            self.pixels[6][2].setOutline("green")
            self.pixels[7][2].setFill(self.color1)
            self.pixels[7][2].setOutline(self.color1)
            self.pixels[6][6].setFill("green")
            self.pixels[6][6].setOutline("green")
            self.pixels[7][6].setFill(self.color1)
            self.pixels[7][6].setOutline(self.color1)
            self.pixels[7][7].setFill("green")
            self.pixels[7][7].setOutline("green")
            self.pixels[6][8].setFill(self.color1)
            self.pixels[6][8].setOutline(self.color1)
            update(UPDATE_RATE)
            time.sleep(0.3)
            self.pixels[6][2].setFill(self.color1)
            self.pixels[6][2].setOutline(self.color1)
            self.pixels[7][2].setFill("green")
            self.pixels[7][2].setOutline("green")
            self.pixels[6][6].setFill(self.color1)
            self.pixels[6][6].setOutline(self.color1)
            self.pixels[7][6].setFill("green")
            self.pixels[7][6].setOutline("green")
            self.pixels[7][7].setFill(self.color1)
            self.pixels[7][7].setOutline(self.color1)
            self.pixels[6][8].setFill("green")
            self.pixels[6][8].setOutline("green")
            update(UPDATE_RATE)
            time.sleep(0.3)
        
    def animateTurn(self):
        left = {"0":("green", "green", "green", self.color1, "green", "green", "green", "green", "green"),
                "1":("green", "green", self.color1, self.color1, self.color1, self.color1, "green", "green", "green"),
                "2":("green", "green", "lightskyblue", self.color1, self.color1, self.color1, "green", "green", "green"),
                "3":("green", "pink", self.color1, self.color1, self.color1, self.color1, "green", "green", "green"),
                "4":("green", "green", self.color1, self.color1, self.color1, "green", "green", "green", "green"),
                "5":("green", "green", "green", self.color2, self.color1, "green", "green", "green", "green"),
                "6":("green", "green", self.color1, self.color1, self.color1, "green", self.color1, "green", "green"),
                "7":("green", "green", "green", self.color2, self.color1, "green", "green", self.color1, "green"),
                "8":("green", "green", "green", self.color2, self.color1, "green", "green", self.color1, "green"),
                "9":("green", "green", "green", self.color2, self.color1, self.color1, self.color1, "green", "green"),
                "10":("green", "green", "green", self.color1, self.color1, "green", "green", "green", "green"),
                "11":("green", "green", "green", "green", self.color1, "green", "green", "green", "green")}
        
        back = {"0":("green", "green", "green", self.color1, "green", self.color1, "green", "green", "green"),
                "1":("green", "green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green"),
                "2":("green", "green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green"),
                "3":("green", "green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green"),
                "4":("green", "green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green"),
                "5":("green", "green", "green", self.color1, self.color1, self.color1, "green", "green", "green"),
                "6":("green", "green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green"),
                "7":(self.color1, self.color1, "green", self.color1, self.color1, self.color1, "green", "green", "green"),
                "8":(self.color1, "green", "green", self.color1, self.color1, self.color1, "green", "green", "green"),
                "9":("green", self.color1, self.color1, self.color1, self.color1, self.color1, "green", "green", "green"),
                "10":("green", "green", "green", self.color1, self.color1, self.color1, "green", "green", "green"),
                "11":("green", "green", "green", self.color1, "green", self.color1, "green", "green", "green")}
        
        right = {"0":("green", "green", "green", "green", "green", self.color1, "green", "green", "green"),
                 "1":("green", "green", "green", self.color1, self.color1, self.color1, self.color1, "green", "green"),
                 "2":("green", "green", "green", self.color1, self.color1, self.color1, "lightskyblue", "green", "green"),
                 "3":("green", "green", "green", self.color1, self.color1, self.color1, self.color1, "pink", "green"),
                 "4":("green", "green", "green", self.color1, self.color1, self.color1, self.color1, "green", "green"),
                 "5":("green", "green", "green", "green", self.color1, self.color2, "green", "green", "green"),
                 "6":("green", "green", self.color1, "green", self.color1, self.color1, self.color1, "green", "green"),
                 "7":("green", self.color1, "green", "green", self.color1, self.color2, "green", "green", "green"),
                 "8":("green", self.color1, "green", "green", self.color1, self.color2, "green", "green", "green"),
                 "9":("green", "green", self.color1, self.color1, self.color1, self.color2, "green", "green", "green"),
                 "10":("green", "green", "green", "green", self.color1, self.color1, "green", "green", "green"),
                 "11":("green", "green", "green", "green", self.color1, "green", "green", "green", "green")}
        
        leftList = []
        for j in range(12):
            leftList.append([])
            for i in range(9):
                leftList[j].append(Rectangle(Point(i*self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.__yloc), Point(i*self.PIX_WIDTH+self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.PIX_WIDTH+self.__yloc)))
                leftList[j][i].setFill(left[str(j)][i])
                leftList[j][i].setOutline(left[str(j)][i])
                
        backList = []
        for j in range(12):
            backList.append([])
            for i in range(9):
                backList[j].append(Rectangle(Point(i*self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.__yloc), Point(i*self.PIX_WIDTH+self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.PIX_WIDTH+self.__yloc)))
                backList[j][i].setFill(back[str(j)][i])
                backList[j][i].setOutline(back[str(j)][i])
              
        rightList = []
        for j in range(12):
            rightList.append([])
            for i in range(9):
                rightList[j].append(Rectangle(Point(i*self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.__yloc), Point(i*self.PIX_WIDTH+self.PIX_WIDTH+self.__xloc,j*self.PIX_WIDTH+self.PIX_WIDTH+self.__yloc)))
                rightList[j][i].setFill(right[str(j)][i])
                rightList[j][i].setOutline(right[str(j)][i])
                
        for i in range(3):
            # Turn left
            for row in leftList:
                for box in row:
                    box.draw(self.window)
            for row in self.pixels:
                for box in row:
                    box.undraw()
            update(UPDATE_RATE)
            time.sleep(0.2)
            # Turn back
            for row in backList:
                for box in row:
                    box.draw(self.window)
            for row in leftList:
                for box in row:
                    box.undraw()
            update(UPDATE_RATE)
            time.sleep(0.2)
            # Turn right
            for row in rightList:
                for box in row:
                    box.draw(self.window)
            for row in backList:
                for box in row:
                    box.undraw()
            update(UPDATE_RATE)
            time.sleep(0.2)
            # Turn front
            for row in self.pixels:
                for box in row:
                    box.draw(self.window)
            for row in rightList:
                for box in row:
                    box.undraw()
            update(UPDATE_RATE)
            time.sleep(0.2)

# Background graphics class
class graphicObject:
    
    def __init__(self, dictionary, xloc, yloc, height, width, PIX_WIDTH, window):
        self.xloc = xloc
        self.yloc = yloc
        self.height = height
        self.width = width
        self.PIX_WIDTH = PIX_WIDTH
        self.window = window
        self.pixels = []
        self.dictionary = dictionary
        
        for j in range(self.height):
            self.pixels.append([])
            for i in range(self.width):
                self.pixels[j].append(Rectangle(Point(i*self.PIX_WIDTH+self.xloc,j*self.PIX_WIDTH+self.yloc), Point(i*self.PIX_WIDTH+self.PIX_WIDTH+self.xloc,j*self.PIX_WIDTH+self.PIX_WIDTH+self.yloc)))
                self.pixels[j][i].setFill(self.dictionary[str(j)][i])
                self.pixels[j][i].setOutline(self.dictionary[str(j)][i])
        
    def drawGraphic(self):
        for row in self.pixels:
            for box in row:
                box.draw(self.window)
                
    def undrawGraphic(self):
        for row in self.pixels:
            for box in row:
                box.undraw()


# Dictionaries for background graphics

#3x2
seed = {"0":("green", "burlywood"),
        "1":("papayawhip", "burlywood"),
        "2":("papayawhip", "papayawhip")}

#4x4
bucket = {"0":("silver", "gray", "gray", "silver"),
          "1":("silver", "silver", "silver", "silver"),
          "2":("gray", "silver", "silver", "silver"),
          "3":("green", "gray", "gray", "green")}

#6x17
dirt = {"0":("green", "green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green", "green", "green", "green"),
        "1":("green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
        "2":("saddlebrown", "saddlebrown", "sienna", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown"),
        "3":("saddlebrown", "sienna", "sienna", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown"),
        "4":("green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
        "5":("green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "green", "green", "green", "green")}

#19x17
plant1 = {"0":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "1":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "2":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "3":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "4":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "5":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "6":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "7":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "8":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "9":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "10":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "11":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "12":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "13":("green", "green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green", "green", "green", "green"),
          "14":("green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "sienna", "burlywood", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "15":("saddlebrown", "saddlebrown", "sienna", "saddlebrown", "sienna", "saddlebrown", "black", "papayawhip", "burlywood", "black", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown"),
          "16":("saddlebrown", "sienna", "sienna", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "black", "black", "sienna", "sienna", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown"),
          "17":("green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "18":("green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "green", "green", "green", "green")}

#19x17
plant2 = {"0":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "1":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "2":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "3":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "4":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "5":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "6":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "7":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "8":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "9":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "10":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "11":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "12":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "13":("green", "green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "greenyellow", "greenyellow", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green", "green", "green", "green"),
          "14":("green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "sienna", "greenyellow", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "15":("saddlebrown", "saddlebrown", "sienna", "saddlebrown", "sienna", "saddlebrown", "black", "papayawhip", "greenyellow", "black", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown"),
          "16":("saddlebrown", "sienna", "sienna", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "black", "black", "sienna", "sienna", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown"),
          "17":("green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "18":("green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "green", "green", "green", "green")}

#19x17
plant3 = {"0":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "1":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "2":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "3":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "4":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "5":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "6":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "7":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "8":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "9":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "10":("green", "green", "green", "green", "green", "green", "darkgreen", "darkgreen", "green", "darkgreen", "darkgreen", "green", "green", "green", "green", "green", "green"),
          "11":("green", "green", "green", "green", "green", "green", "darkgreen", "darkgreen", "greenyellow", "darkgreen", "darkgreen", "green", "green", "green", "green", "green", "green"),
          "12":("green", "green", "green", "green", "green", "green", "green", "green", "greenyellow", "green", "green", "green", "green", "green", "green", "green", "green"),
          "13":("green", "green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "greenyellow", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green", "green", "green", "green"),
          "14":("green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "sienna", "greenyellow", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "15":("saddlebrown", "saddlebrown", "sienna", "saddlebrown", "sienna", "saddlebrown", "black", "papayawhip", "greenyellow", "black", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown"),
          "16":("saddlebrown", "sienna", "sienna", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "black", "black", "sienna", "sienna", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown"),
          "17":("green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "18":("green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "green", "green", "green", "green")}

#19x17
plant4 = {"0":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "1":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "2":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "3":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "4":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "5":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "6":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
          "7":("green", "green", "green", "green", "green", "green", "green", "lavender", "lavender", "green", "green", "green", "green", "green", "green", "green", "green"),
          "8":("green", "green", "green", "green", "green", "green", "darkgreen", "lavender", "lavender", "darkgreen", "green", "green", "green", "green", "green", "green", "green"),
          "9":("green", "green", "green", "green", "green", "green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green", "green", "green", "green", "green", "green", "green"),
          "10":("green", "green", "green", "green", "green", "green", "green", "greenyellow", "greenyellow", "green", "green", "green", "green", "green", "green", "green", "green"),
          "11":("green", "green", "green", "green", "darkgreen", "darkgreen", "green", "greenyellow", "greenyellow", "green", "darkgreen", "darkgreen", "green", "green", "green", "green", "green"),
          "12":("green", "green", "green", "green", "green", "darkgreen", "darkgreen", "greenyellow", "greenyellow", "darkgreen", "darkgreen", "green", "green", "green", "green", "green", "green"),
          "13":("green", "green", "green", "green", "saddlebrown", "saddlebrown", "darkgreen", "greenyellow", "greenyellow", "darkgreen", "saddlebrown", "saddlebrown", "saddlebrown", "green", "green", "green", "green"),
          "14":("green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "greenyellow", "greenyellow", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "15":("saddlebrown", "saddlebrown", "sienna", "saddlebrown", "sienna", "saddlebrown", "black", "greenyellow", "greenyellow", "black", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown"),
          "16":("saddlebrown", "sienna", "sienna", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "black", "black", "sienna", "sienna", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown"),
          "17":("green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "18":("green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "green", "green", "green", "green")}

#19x17
plant5 = {"0":("green", "green", "green", "green", "mediumslateblue", "green", "orange", "green", "green", "orange", "green", "mediumslateblue", "green", "green", "green", "green", "green"),
          "1":("green", "green", "green", "green", "mediumslateblue", "lavender", "gold", "green", "green", "gold", "lavender", "mediumslateblue", "green", "green", "green", "green", "green"),
          "2":("green", "green", "green", "green", "mediumslateblue", "lavender", "mediumslateblue", "lavender", "lavender", "mediumslateblue", "lavender", "mediumslateblue", "green", "green", "green", "green", "green"),
          "3":("green", "green", "green", "green", "mediumslateblue", "lavender", "mediumslateblue", "lavender", "lavender", "mediumslateblue", "lavender", "mediumslateblue", "green", "green", "green", "green", "green"),
          "4":("green", "green", "green", "green", "mediumslateblue", "lavender", "mediumslateblue", "lavender", "lavender", "mediumslateblue", "lavender", "mediumslateblue", "green", "green", "green", "green", "green"),
          "5":("green", "green", "green", "green", "green", "mediumslateblue", "lavender", "mediumslateblue", "mediumslateblue", "lavender", "mediumslateblue", "green", "green", "green", "green", "green", "green"),
          "6":("green", "green", "green", "darkgreen", "darkgreen", "mediumslateblue", "mediumslateblue", "lavender", "lavender", "mediumslateblue", "mediumslateblue", "darkgreen", "darkgreen", "green", "green", "green", "green"),
          "7":("green", "green", "green", "green", "darkgreen", "darkgreen", "darkgreen", "mediumslateblue", "mediumslateblue", "darkgreen", "darkgreen", "darkgreen", "green", "green", "green", "green", "green"),
          "8":("green", "green", "green", "green", "green", "green", "darkgreen", "greenyellow", "greenyellow", "darkgreen", "green", "green", "green", "green", "green", "green", "green"),
          "9":("green", "green", "green", "green", "green", "green", "green", "greenyellow", "greenyellow", "green", "green", "green", "green", "green", "green", "green", "green"),
          "10":("green", "green", "green", "green", "green", "green", "green", "greenyellow", "greenyellow", "green", "green", "green", "green", "green", "green", "green", "green"),
          "11":("green", "green", "green", "green", "darkgreen", "darkgreen", "green", "greenyellow", "greenyellow", "green", "darkgreen", "darkgreen", "green", "green", "green", "green", "green"),
          "12":("green", "green", "green", "green", "green", "darkgreen", "darkgreen", "greenyellow", "greenyellow", "darkgreen", "darkgreen", "green", "green", "green", "green", "green", "green"),
          "13":("green", "green", "green", "green", "saddlebrown", "saddlebrown", "darkgreen", "greenyellow", "greenyellow", "darkgreen", "saddlebrown", "saddlebrown", "saddlebrown", "green", "green", "green", "green"),
          "14":("green", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "greenyellow", "greenyellow", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "15":("saddlebrown", "saddlebrown", "sienna", "saddlebrown", "sienna", "saddlebrown", "black", "greenyellow", "greenyellow", "black", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "saddlebrown", "saddlebrown"),
          "16":("saddlebrown", "sienna", "sienna", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "black", "black", "sienna", "sienna", "saddlebrown", "saddlebrown", "sienna", "saddlebrown", "saddlebrown", "saddlebrown"),
          "17":("green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "sienna", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "green"),
          "18":("green", "green", "green", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "saddlebrown", "sienna", "sienna", "green", "green", "green", "green")}

#39x38
pond = {"0":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "indianred", "indianred", "indianred", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "1":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "2":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "indianred", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "indianred", "green", "green", "green", "green", "green", "green", "green", "green"),
        "3":("green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "indianred", "indianred", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green"),
        "4":("green", "green", "green", "green", "green", "indianred", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green"),
        "5":("green", "green", "green", "green", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green"),
        "6":("green", "green", "green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "indianred", "green", "green", "green", "green", "green", "green"),
        "7":("green", "green", "green", "indianred", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green"),
        "8":("green", "green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green"),
        "9":("green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green"),
        "10":("green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "royalblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green"),
        "11":("green", "indianred", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "indianred", "green", "green", "green", "green"),
        "12":("indianred", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green"),
        "13":("indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green"),
        "14":("indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green"),
        "15":("indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green"),
        "16":("indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "indianred"),
        "17":("green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred"),
        "18":("green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred"),
        "19":("green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred"),
        "20":("green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred"),
        "21":("green", "green", "indianred", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green"),
        "22":("green", "green", "green", "indianred", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green"),
        "23":("green", "green", "green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green"),
        "24":("green", "green", "green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "indianred", "green", "green"),
        "25":("green", "green", "green", "green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green"),
        "26":("green", "green", "green", "green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green"),
        "27":("green", "green", "green", "green", "green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green"),
        "28":("green", "green", "green", "green", "green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "indianred", "green", "green", "green", "green", "green", "green"),
        "29":("green", "green", "green", "green", "green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green"),
        "30":("green", "green", "green", "green", "green", "green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "lightskyblue", "lightskyblue", "deepskyblue", "deepskyblue", "royalblue", "royalblue", "royalblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green"),
        "31":("green", "green", "green", "green", "green", "green", "green", "indianred", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "royalblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green"),
        "32":("green", "green", "green", "green", "green", "green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green"),
        "33":("green", "green", "green", "green", "green", "green", "green", "green", "indianred", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green"),
        "34":("green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "35":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "36":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "deepskyblue", "deepskyblue", "deepskyblue", "deepskyblue", "firebrick", "firebrick", "firebrick", "firebrick", "indianred", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "37":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "indianred", "indianred", "indianred", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "firebrick", "indianred", "indianred", "indianred", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "38":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "indianred", "indianred", "indianred", "indianred", "indianred", "indianred", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green")}

#19x27
tent = {"0":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "gold", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "1":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "yellow", "gold", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "2":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "yellow", "yellow", "gold", "yellow", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "3":("green", "green", "green", "green", "green", "green", "green", "green", "green", "green", "yellow", "yellow", "gold", "gold", "gold", "yellow", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "4":("green", "green", "green", "green", "green", "green", "green", "green", "green", "yellow", "yellow", "yellow", "gold", "black", "gold", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green", "green", "green", "green", "green"),
        "5":("green", "green", "green", "green", "green", "green", "green", "green", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green", "green", "green", "green"),
        "6":("green", "green", "green", "green", "green", "green", "green", "green", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green", "green", "green", "green"),
        "7":("green", "green", "green", "green", "green", "green", "green", "yellow", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green", "green", "green"),
        "8":("green", "green", "green", "green", "green", "green", "yellow", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green", "green"),
        "9":("green", "green", "green", "green", "green", "yellow", "yellow", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green"),
        "10":("green", "green", "green", "green", "green", "yellow", "yellow", "yellow", "yellow", "gold", "gold", "black", "black", "black", "black", "black", "gold", "gold", "yellow", "yellow", "yellow", "yellow", "green", "green", "green", "green", "green"),
        "11":("green", "green", "green", "green", "yellow", "yellow", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "black", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "yellow", "yellow", "green", "green", "green", "green"),
        "12":("green", "green", "green", "green", "yellow", "yellow", "yellow", "yellow", "gold", "gold", "black", "black", "black", "black", "black", "black", "black", "gold", "gold", "yellow", "yellow", "yellow", "yellow", "green", "green", "green", "green"),
        "13":("green", "green", "green", "yellow", "yellow", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "black", "black", "black", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "yellow", "yellow", "green", "green", "green"),
        "14":("green", "green", "yellow", "yellow", "yellow", "yellow", "yellow", "gold", "gold", "black", "black", "black", "black", "black", "black", "black", "black", "black", "gold", "gold", "yellow", "yellow", "yellow", "yellow", "yellow", "green", "green"),
        "15":("green", "green", "yellow", "yellow", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "yellow", "yellow", "green", "green"),
        "16":("green", "yellow", "yellow", "yellow", "yellow", "yellow", "gold", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "gold", "yellow", "yellow", "yellow", "yellow", "yellow", "green"),
        "17":("yellow", "yellow", "yellow", "yellow", "yellow", "gold", "gold", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "gold", "gold", "yellow", "yellow", "yellow", "yellow", "yellow"),
        "18":("gold", "gold", "gold", "gold", "gold", "gold", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "gold", "gold", "gold", "gold", "gold", "gold")}

#14x19
bush = {"0":("green", "green", "green", "green", "green", "green", "green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green", "green", "green", "green", "green", "green", "green", "green"),
        "1":("green", "green", "green", "green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green", "green", "green", "green", "green"),
        "2":("green", "green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "green", "green", "green"),
        "3":("green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green"),
        "4":("darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen"),
        "5":("darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen"),
        "6":("darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen"),
        "7":("darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen"),
        "8":("darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green"),
        "9":("darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green"),
        "10":("green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "green"),
        "11":("green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "red", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green", "green"),
        "12":("green", "green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green", "green", "green"),
        "13":("green", "green", "green", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "darkgreen", "green", "green", "green", "green", "green", "green")}


# Setup GPIO
GPIO.setwarnings(False) # Ignore warnings
GPIO.setmode(GPIO.BCM) # Use BCM Pin numbering
GPIO.setup(26, GPIO.IN) # Assign button GPIO

# Create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# Create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# Create the mcp object
mcp = MCP.MCP3008(spi, cs)

# Define constants
WIN_WIDTH = 500
WIN_HEIGHT = 500
PIXEL = 5
SPEED = 50
UPDATE_RATE = 30 #Frames per second
seedTracker = 0
plantTracker = 0
day = 1

# Graphics Window Setup
win = GraphWin("GraphicsWindow", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
win.setBackground("green")

# Create graphic objects
fred = cat(55, 210, "brown", "red", PIXEL, win)
tentObject = graphicObject(tent, 10, 100, 19, 27, PIXEL, win)
pondObject = graphicObject(pond, 10, 300, 39, 38, PIXEL, win)
bucketObject = graphicObject(bucket, 180, 450, 4, 4, PIXEL, win)
dirtObject = graphicObject(dirt, 310, 115, 6, 17, PIXEL, win)
seedObject = graphicObject(seed, 375, 475, 3, 2, PIXEL, win)
plant1Object = graphicObject(plant1, 310, 50, 19, 17, PIXEL, win)
plant2Object = graphicObject(plant2, 310, 50, 19, 17, PIXEL, win)
plant3Object = graphicObject(plant3, 310, 50, 19, 17, PIXEL, win)
plant4Object = graphicObject(plant4, 310, 50, 19, 17, PIXEL, win)
plant5Object = graphicObject(plant5, 310, 50, 19, 17, PIXEL, win)
bush1Object = graphicObject(bush, -20, -25, 14, 19, PIXEL, win)
bush2Object = graphicObject(bush, 65, -25, 14, 19, PIXEL, win)
bush3Object = graphicObject(bush, 150, -25, 14, 19, PIXEL, win)
bush4Object = graphicObject(bush, 235, -25, 14, 19, PIXEL, win)
bush5Object = graphicObject(bush, 320, -25, 14, 19, PIXEL, win)
bush6Object = graphicObject(bush, 405, -25, 14, 19, PIXEL, win)
bush7Object = graphicObject(bush, 490, -25, 14, 19, PIXEL, win)
bush8Object = graphicObject(bush, 460, 40, 14, 19, PIXEL, win)
bush9Object = graphicObject(bush, 460, 105, 14, 19, PIXEL, win)
bush10Object = graphicObject(bush, 460, 170, 14, 19, PIXEL, win)
bush11Object = graphicObject(bush, 460, 235, 14, 19, PIXEL, win)
bush12Object = graphicObject(bush, 460, 300, 14, 19, PIXEL, win)
bush13Object = graphicObject(bush, 460, 365, 14, 19, PIXEL, win)
bush14Object = graphicObject(bush, 460, 430, 14, 19, PIXEL, win)
bush15Object = graphicObject(bush, -40, 45, 14, 19, PIXEL, win)
night = Rectangle(Point(0,0), Point(WIN_WIDTH,WIN_HEIGHT))
night.setFill("black")
tutorial = Text(Point(300,250), "You did it!")
tutorial.setFace("courier")
tutorial.setSize(36)
tutorial.setStyle("bold")
tutorial.setTextColor("white")


# Define callback function
def button_callback(channel): 
    print ("Button Falling Edge")
    global fred
    global seedTracker
    global plantTracker
    global day
    # Pick up seed
    if (fred.getX() == 355 and fred.getY() == 410):
        seedTracker += 1
    # Plant seed
    elif (fred.getX() == 255 and fred.getY() == 60 and seedTracker == 2):
        seedTracker += 1
    # Get water
    elif (fred.getX() == 205 and fred.getY() == 410 and (seedTracker==4 or (day!=1 and plantTracker==0))):
        seedTracker += 1
        plantTracker += 1
    # Get bucket
    elif (fred.getX() == 205 and fred.getY() == 410 and (seedTracker==6 or (day!=1 and plantTracker==2))):
        seedTracker += 1
        plantTracker += 1
    # Water seed
    elif (fred.getX() == 255 and fred.getY() == 60 and (seedTracker==8 or (day!=1 and plantTracker==4))):
        seedTracker += 1
        plantTracker += 1
    # Put bucket back
    elif (fred.getX() == 205 and fred.getY() == 410 and (seedTracker==10 or (day!=1 and plantTracker==6))):
        seedTracker += 1
        plantTracker += 1
    # End day
    elif (fred.getX() == 55 and fred.getY() == 210 and (seedTracker==12 or (day!=1 and plantTracker==8))):
        seedTracker += 1
        plantTracker += 1
    
# Add event detectors
GPIO.add_event_detect(26, GPIO.FALLING, callback=button_callback, bouncetime=300)

# Move player right
def moveRight(player):
    if (player.getX() <= WIN_WIDTH - player.PIX_WIDTH*20 and not(player.getX()>=225 and player.getY()<=130)):
        player.myCatMove(SPEED, 0)
        time.sleep(0.2)

# Move player left
def moveLeft(player):
    if (player.getX() >= 10 and not(player.getX()<=130 and player.getY()<=80) and not(player.getX()<=175 and 80<=player.getY()<=175) and not(player.getX()<=220 and 250<=player.getY()<=420) and not(player.getX()>=390 and player.getY()<=120)):
        player.myCatMove((-1)*SPEED, 0)
        time.sleep(0.2)
    
# Move player up
def moveUp(player):
    if (player.getY() >= 75 and not(290<=player.getX()<=375 and player.getY()<=175) and not(player.getX()<=120 and player.getY()<=225)):
        player.myCatMove(0, (-1)*SPEED)
        time.sleep(0.2)
    
# Move player down
def moveDown(player):
    if (player.getY() <= WIN_HEIGHT - player.PIX_WIDTH*22 and not(player.getX()<=125 and player.getY()<=75) and not(player.getX()<=175 and player.getY()>=200)):
        player.myCatMove(0, SPEED)
        time.sleep(0.2)
        
# Water plant
def waterPlant(plant):
    plant.pixels[14][6].setFill("black")
    plant.pixels[14][6].setOutline("black")
    plant.pixels[14][9].setFill("black")
    plant.pixels[14][9].setOutline("black")
    plant.pixels[15][5].setFill("black")
    plant.pixels[15][5].setOutline("black")
    plant.pixels[15][10].setFill("black")
    plant.pixels[15][10].setOutline("black")
    plant.pixels[16][6].setFill("black")
    plant.pixels[16][6].setOutline("black")
    plant.pixels[16][9].setFill("black")
    plant.pixels[16][9].setOutline("black")
            
# Fill bucket
def fillBucket():
    bucketObject.pixels[0][1].setFill("deepskyblue")
    bucketObject.pixels[0][1].setOutline("deepskyblue")
    bucketObject.pixels[0][2].setFill("deepskyblue")
    bucketObject.pixels[0][2].setOutline("deepskyblue")
            
# Put bucket back
def putBucket():
    bucketObject.pixels[0][1].setFill("gray")
    bucketObject.pixels[0][1].setOutline("gray")
    bucketObject.pixels[0][2].setFill("gray")
    bucketObject.pixels[0][2].setOutline("gray")
    bucketObject.drawGraphic()
    

# Main

try:
    udV = AnalogIn(mcp, MCP.P1)
    lrV = AnalogIn(mcp, MCP.P0)
    
    tentObject.drawGraphic()
    pondObject.drawGraphic()
    bucketObject.drawGraphic()
    dirtObject.drawGraphic()
    seedObject.drawGraphic()
    bush1Object.drawGraphic()
    bush2Object.drawGraphic()
    bush3Object.drawGraphic()
    bush4Object.drawGraphic()
    bush5Object.drawGraphic()
    bush6Object.drawGraphic()
    bush7Object.drawGraphic()
    bush8Object.drawGraphic()
    bush9Object.drawGraphic()
    bush10Object.drawGraphic()
    bush11Object.drawGraphic()
    bush12Object.drawGraphic()
    bush13Object.drawGraphic()
    bush14Object.drawGraphic()
    bush15Object.drawGraphic()
    
    fred.myCatDraw()
        
    while(1): 
        ud = int(100*(udV.voltage)/3.3)
        lr = int(100*(lrV.voltage)/3.3)
        
        # Day 1
        
        # Pick up seed
        if seedTracker == 1:
            seedObject.undrawGraphic()
            fred.animateCheer()
            seedTracker += 1
            
        # Plant seed
        if seedTracker == 3:
            plant1Object.drawGraphic()
            dirtObject.undrawGraphic()
            fred.animateTurn()
            seedTracker += 1
            
        # Get water
        if seedTracker == 5:
            fillBucket()
            seedTracker += 1
        
        # Get bucket
        if seedTracker == 7:
            bucketObject.undrawGraphic()
            seedTracker += 1
            
        # Water seed
        if seedTracker == 9:
            waterPlant(plant1Object)
            plant1Object.pixels[14][7].setFill("black")
            plant1Object.pixels[14][7].setOutline("black")
            seedTracker += 1
            
        # Put bucket back
        if seedTracker == 11:
            putBucket()
            seedTracker += 1
            
        # End day 1
        if seedTracker == 13:
            night.draw(win)
            update(UPDATE_RATE)
            time.sleep(1)
            night.undraw()
            plant2Object.drawGraphic()
            plant1Object.undrawGraphic()
            fred.animateCheer()
            seedTracker += 1
            plantTracker = 0
            day += 1
            
        # Day 2
        
        # Get water
        if plantTracker == 1 and day==2:
            fillBucket()
            plantTracker += 1
        
        # Get bucket
        if plantTracker == 3 and day==2:
            bucketObject.undrawGraphic()
            plantTracker += 1
            
        # Water seed
        if plantTracker == 5 and day==2:
            waterPlant(plant2Object)
            plant2Object.pixels[14][7].setFill("black")
            plant2Object.pixels[14][7].setOutline("black")
            plantTracker += 1
            
        # Put bucket back
        if plantTracker == 7 and day==2:
            putBucket()
            plantTracker += 1
            
        # End day 2
        if plantTracker == 9 and day==2:
            night.draw(win)
            update(UPDATE_RATE)
            time.sleep(1)
            night.undraw()
            plant3Object.drawGraphic()
            plant2Object.undrawGraphic()
            fred.animateCheer()
            plantTracker = 0
            day += 1
        
        # Day 3
        
        # Get water
        if plantTracker == 1 and day==3:
            fillBucket()
            plantTracker += 1
        
        # Get bucket
        if plantTracker == 3 and day==3:
            bucketObject.undrawGraphic()
            plantTracker += 1
            
        # Water seed
        if plantTracker == 5 and day==3:
            waterPlant(plant3Object)
            plant3Object.pixels[14][7].setFill("black")
            plant3Object.pixels[14][7].setOutline("black")
            plantTracker += 1
            
        # Put bucket back
        if plantTracker == 7 and day==3:
            putBucket()
            plantTracker += 1
            
        # End day 3
        if plantTracker == 9 and day==3:
            night.draw(win)
            update(UPDATE_RATE)
            time.sleep(1)
            night.undraw()
            plant4Object.drawGraphic()
            plant3Object.undrawGraphic()
            fred.animateCheer()
            plantTracker = 0
            day += 1
            
        # Day 4
        
        # Get water
        if plantTracker == 1 and day==4:
            fillBucket()
            plantTracker += 1
        
        # Get bucket
        if plantTracker == 3 and day==4:
            bucketObject.undrawGraphic()
            plantTracker += 1
            
        # Water seed
        if plantTracker == 5 and day==4:
            waterPlant(plant4Object)
            plantTracker += 1
            
        # Put bucket back
        if plantTracker == 7 and day==4:
            putBucket()
            plantTracker += 1
            
        # End day 4
        if plantTracker == 9 and day==4:
            night.draw(win)
            update(UPDATE_RATE)
            time.sleep(1)
            night.undraw()
            plant5Object.drawGraphic()
            plant4Object.undrawGraphic()
            tutorial.draw(win)
            fred.animateCheer()
            fred.animateTurn()
            break
        
        # Movement
        
        if lr > 70:
            moveRight(fred)
            print(lr)
            print(fred.getX(), fred.getY())
                           
        if lr < 30:
            moveLeft(fred)
            print(lr)
            print(fred.getX(), fred.getY())
            
        if ud > 70:
            moveUp(fred)
            print(ud)
            print(fred.getX(), fred.getY())
                           
        if ud < 30:
            moveDown(fred)
            print(ud)
            print(fred.getX(), fred.getY())
            
        update(UPDATE_RATE)
                        
except KeyboardInterrupt: 
    # This code runs on a Keyboard Interrupt <CNTRL>+C
    print('\n\n' + 'Program exited on a Keyboard Interrupt' + '\n') 

except: 
    # This code runs on any error
    print('\n' + 'Errors occurred causing your program to exit' + '\n')

finally: 
    # This code runs on every exit and sets any used GPIO pins to input mode.
    GPIO.cleanup()




