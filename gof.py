#!/usr/bin/env python3
# coding: utf-8


import sys
import os 
import time

#%%
class universe(object):

    def __init__(self, w, h):
        self.w = w
        self.h = h 
        self.content = {}
        for y in range(self.h):
            for x in range(self.w):
                self.content = [x, y] = 0

    def randomize(self):
        for y in range(self.h):
            for x in range(self.w):
                c = random.randint(0, 30)
                if == 0:







#%%
