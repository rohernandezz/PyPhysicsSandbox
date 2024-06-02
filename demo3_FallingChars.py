"""
Demo 1 :: Falling Rectangles
"""

from pyphysicssandbox import *

w,h = 1050, 1350
floorH = 100
wallW=10
fricT=.5
gravity = (10,-500)

window('Hello World', w, h, fps=30)
resistance(.55)

left_wall= static_box((0,0), wallW, h)
left_wall.elasticity=0.2

floor = static_box((0, h-floorH), w, floorH)
floor.color = Color('Red')
floor.elasticity=1.2

boxxa = box((180, 0),523, 112)
boxxa.elasticity=.75


for




run()

