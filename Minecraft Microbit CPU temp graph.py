# touched.py - demonstrates using pin touch

import microbit
from mcpi import minecraft as minecraft
from mcpi import block as block
import time
import random

WoolList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

 
mc = minecraft.Minecraft.create()
 
orx,ory,orz = mc.player.getPos()

mc.postToChat("Start Graph")

TempBlock = 35,14

HumidityBlock = 35,3
Temperature_List = []#stores temp data

DataStreamCount= 0

def BuildDataBlockTemp(ImportedBlock):# take data for temp
    temp = int(microbit.temperature())
    Temperature_List.append(temp)
    orx,ory,orz = mc.player.getPos()

    for i in range (0,temp):
        x,y,z = mc.player.getPos()  
        mc.setBlock(x+30,i,z,35,ImportedBlock)
    mc.player.setPos(orx,ory,orz+1)
    msg = "Temp = {0}".format(temp)
    
    print(msg)
while True:
    
    time.sleep(0.25)
    if microbit.button_a.was_pressed():
        TempBlock = random.choice(WoolList)
        BuildDataBlockTemp(TempBlock) 
