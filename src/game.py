#!/usr/bin/env python

#
# Vikas Gupta
#

import sys
import rospy
import numpy
import random
import operator
import enum
from collections import Counter
from sets import Set
from std_msgs.msg import String
import roslib
import cv2
from sensor_msgs.msg import CameraInfo
from sensor_msgs.msg import Image
from geometry_msgs.msg import Vector3

GAMES = 100

MAX_ROLLS = 3
NUM_DICE = 5
SIDES = 6

NONE = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
THREE_OF_KIND = 7
FOUR_OF_KIND = 8
FULL_HOUSE = 9
SMALL_STRAIGHT = 10
LARGE_STRAIGHT = 11
FIVE_OF_KIND = 12
CHANCE = 13
POINTS_FULL_HOUSE = 25
POINTS_SMALL_STRAIGHT = 30
POINTS_LARGE_STRAIGHT = 40
POINTS_FIVE_OF_KIND = 50
LARGE_STRAIGHT_FORM = [1,1,1,1]
SMALL_STRAIGHT_FORM_PRE = [1,1,1,0]
SMALL_STRAIGHT_FORM_POST= [0,1,1,1]

class yahtzee:
    def __init__(self):
        self.points = 0
        self.max_rolls = MAX_ROLLS
        self.rolls = 0 
        self.keep = []
        self.shake = []
        self.dice = [0] * NUM_DICE
        self.combination = NONE
        self.game = {
            ONES:0,
            TWOS:0,
            THREES:0,
            FOURS:0,
            FIVES:0,
            SIXES:0,
            THREE_OF_KIND:0,
            FOUR_OF_KIND:0,
            FULL_HOUSE:0,
            SMALL_STRAIGHT:0,
            LARGE_STRAIGHT:0,
            FIVE_OF_KIND:0,
            CHANCE:0}
        for i in range(GAMES):
            self.points = 0
            self.play()

    def play(self):
        for key in self.game.keys():
            self.combination = key
            #print "combination", self.combination
            for j in range(MAX_ROLLS):
                points = self.roll() 
            self.game[self.combination] = points
        for key in self.game.keys():
            #print "key", key, "points", self.game[key]
            self.points += self.game[key]

        print "GAME OVER - SCORE", self.points
 
    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = random.randint(0, SIDES)
        return self.score()

    def chance_slot(self):
       return sum(self.dice)
    
    def score(self):
        points = 0
        self.dice.sort()
        counted = Counter(self.dice)
        #print(self.dice)
        print(counted)

        if(len(counted) == 1 and self.combination == FIVE_OF_KIND):
            print "YAHTZEE"
            points = POINTS_FIVE_OF_KIND
        elif(len(counted) == 2 and self.combination == FULL_HOUSE):
            print "FULL HOUSE"
            points = POINTS_FULL_HOUSE
        elif(self.straight() == LARGE_STRAIGHT and self.combination == LARGE_STRAIGHT):
            print "LARGE STRAIGHT"
            points = POINTS_LARGE_STRAIGHT
        elif(self.straight() == SMALL_STRAIGHT and self.combination == SMALL_STRAIGHT):
            print "SMALL STRAIGHT"
            points = POINTS_SMALL_STRAIGHT
        else:
            print "COMBO"
            points = sum(self.dice)
        return points

    def straight(self):
        d = [self.dice[i+1]-self.dice[i] for i in range(len(self.dice)-1)]
        if(d == LARGE_STRAIGHT_FORM):
            return LARGE_STRAIGHT

        if(d == SMALL_STRAIGHT_FORM_PRE or d == SMALL_STRAIGHT_FORM_POST):
            return SMALL_STRAIGHT 

    def chance_slot():
        return sum(self.dice)

y = yahtzee()
