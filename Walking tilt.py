#Original written by David Whale located here as part of his BITIO library
#https://github.com/whaleygeek/bitio/blob/master/src/tilt_mc.py
#adapted by @ncscomputing 19/07/17


import mcpi.minecraft as minecraft
import mcpi.block as block
import microbit
import time
import random




mc = minecraft.Minecraft.create()

blocksList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

while True:
    pos = mc.player.getTilePos()
    x = microbit.accelerometer.get_x()/300 # -ve=left/+ve=right
    y = microbit.accelerometer.get_y()/300 # -ve=forward/+ve=backward

    pos.x += x # east/west
    pos.z += y # north/south

    mc.player.setTilePos(pos.x, pos.y, pos.z)
    mc.setBlock(pos.x, pos.y-1, pos.z,35,random.choice(blocksList))
    

   # time.sleep(0.5)
