#!/usr/bin/env python3
# coding: utf-8


import sys
import os 
import time


class Universe(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h 
        self.contents = {}
        for y in range(self.h):
            for x in range(self.w):
                self.contents = [x, y] = 0
        self.toString = ""
        for y in range(self):
            for x in range(self.w):
                c = self.contents = [x, y]
                if c == 0:
                    self.toString += " "
                elif c == 1:
                    self.toString += u"\u2588"
            self.toString += "\n"        
                
    def randomize(self):
        out = {}
        for y in range(self.h):
            for x in range(self.w):
                c = random.randint(0, 30)
                if c == 0:
                    out[x, y] = 1
                else:
                    out[x, y] = 0
        self.contents = out
    

    def getNeighbours(self):
        pass


try:
    width = int(sys.argv[1])
except:
    width = 100
try:
    height = int(sys.argv[2])
except:
    height = 12


universe = Universe(width, height)
universe.randomize()

while True:
    




