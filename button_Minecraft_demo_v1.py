"""
Written by @ncscomputing on top of the bitio produced by David Whale 
"""
import serial
from mcpi.minecraft import Minecraft
from time import sleep
from mcpi import block as block
import random


mc = Minecraft.create()

BlockIdList = [1,2,3,4,5,6,7,8,9,20,26,89]
# button.py - demonstrates using a button

import time
import microbit

print("micro:bit connected - press button A to test")

while True:
    time.sleep(0.25)
    if microbit.button_a.was_pressed():
        print("Button A pressed")
        pos = mc.player.getPos()
        BlockID = random.choice(BlockIdList)
        msg = "Button pressed = True"+"+ Block ID = "+str(BlockID)
        mc.postToChat(msg)
        mc.setBlock(pos.x,pos.y,pos.z,BlockID)
        microbit.display.show(int(BlockID))
        time.sleep(0.5)


# END
