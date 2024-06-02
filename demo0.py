"""
Demo 1 :: Falling Rectangles and type in drawBot
"""

from pyphysicssandbox import *

win_width = 1000
win_height = 1000
w,h = win_width, win_height

floorH = 100
wallW=10
fricT=.5
gravity = (10,-500)

window('DEMO_0', w, h, fps=30)
resistance(.55)

left_wall= static_box((0,0), wallW, h)
left_wall.elasticity=0.2

floor = static_box((0, h-floorH), w, floorH)
floor.color = Color("red")        #pygame color for live visualization (<-in pygame name notation)
floor.color = Color("#FF000000")  #pygame color for live visualization (<-in pygame rgb HEX notation)
floor._db_color = (.9,0,.2)       #drawBot color for rendering. <-in Db notation)
floor.elasticity=1.2

#boxxa = box((180, 0),523, 112)  #
boxxa = textBox((180, 0),523,113,"523, 112")
boxxa.elasticity=.75

boxxy = box((100, 100),523, 112)
boxxy.color= Color("blue")
boxxy.elasticity=.75 

#boxx =     box((125, 320),523, 112)
boxx = textBox((125, 320),550, 113, "drawbot")
boxx.color= Color('blue')

boxx.elasticity=.55

boxxx = box((355, 420),523, 112)
boxxx.elasticity=.9
boxxx.db_color=(0.2,0,.5)

run()

