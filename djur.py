# import av diverse

import random
import time
import json
from djur_calendar import *

#replace with data from file
currentTime=0
last_check=0

#constants
speedUpFactor=10.0
animal_update_interval=60*60
maxAge=10*24

# alla stats 0-100 eller bool
class Djur:
    def __init__(self,namn):
        #the name of the animal
        self.namn = namn

        #how hungry the animal is. less is need food
        self.hunger = random.randint(50,100)

        #how much the animal likes you. more is better
        self.attachment = random.randint(25,50)

        #the cleanness of the animal. more is more clean.
        self.hygiene = random.randint(40,100)

        #how entertained the animal is. more is better
        self.fun = random.randint(30,60)

        #if it is alive. Is this needed?
        self.alive = True

        #if it is sick
        self.sick = False

        #how sleepy the animal is. less means sleepy
        self.energy=random.randint(30,100)

        #how old the animal is. more is older
        self.age=0

    def load_previous_stats(self,hu,at,hy,fu,al,si,en,ag):
        self.hunger     = hu
        self.attachment = at
        self.hygiene    = hy
        self.fun        = fu
        self.alive      = al
        self.sick       = si
        self.energy     = en
        self.age        = ag

    def lower_stat(self):
        for stat_temp in [self.hunger,self.hygiene,self.fun,self.energy]:
            if stat_temp<20:
                self.attachment-=2
        self.hunger     -= 3
        self.hygiene    -= 1
        self.fun        -= 5
        self.energy     -= 3
        self.attachment += 1
        self.age        += 1
        #make no negative values or values over 100
        for stat_temp in [self.hunger,self.hygiene,self.fun,self.energy]:
            if stat_temp<0:
                stat_temp=0
            if stat_temp>100:
                stat_temp=100

    def eat(self):
        '''demo of how the stats could be changed'''
        for i in range(6):
            time.sleep(100/speedUpFactor)
            currentTime+=100
            self.hunger+=10
            print "Nom nom nom"

    def sleep(self):
        '''demo of how the stats could be changed'''
        self.energy+=100
        if energy>100:
            energy=100

    # en funktion som visar hur djuret mår
    def inspect(self):
        print "name: " self.namn + "  ålder: " + self.age
        print "hunger: " + statusBar(self.hunger)
        print "hygiene: " + statusBar(self.hygiene)
        print "attachment: " + statusBar(self.attachment)
        print "fun: " + statusBar(self.fun)
        print "energy: " + statusBar(self.energy)
        if self.sick == True:
            print self.namn + " är sjuk"

# en funktion som skapar en bar som visar djurets status
def statusBar(stat):
    bar="["
    i = 0
    while stat > 0:
        i = i+1
        stat = (stat - 10)
        bar = bar + "|"

    while i = 10:
        bar = bar + "-"
        i = i+1
    bar = bar + "]"
    return bar

# En meny som lämpligtvis visas när man ska skapa ett nytt djur
def printCreateNew():
    print "Hi it is time for you to create an animal to take care of"
    print "it is you'r responsibility to make sure the animal survives"
    print "you are going to need to teke care of youre animal on difirent ways"
    print "for example you are going to need feed it an play with it too keep it fedd and happy"
    print "to start you are first going to need to give the animal name"


# meny som lämpligtvis visas när man ska välja vad man sa göra
def printMenu():
    print "it is time to take care if youre animal"
    print "choose what you want to to with it"
    print "if you want to know more about how it is doing choose insptct"
    print "if you want to quit and save the animal do select quit"
    print "1.Feed  2.Play  3.Sleep  4.wach  5.inspect  6.give medecin  7.quit"


def moreDetails():
    pass

while True:
    if currentAnimal==None:
        nynamn=str(input("Ge ditt nya djur ett namn."))
        djur_pointer=Djur(nynamn)
    else:
        Menu()
    while last_check+animal_update_interval <= currentTime:
        djur_pointer.lower_stat()

        last_check+=animal_update_interval
