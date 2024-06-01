"""
Demo 1 :: Falling Rectangles
"""

from pyphysicssandbox import *

w,h = 1050, 1350
floorH = 100
wallW=10
fricT=.7

window('Hello Diplöe', w, h, fps=30)
resistance(.90)

floor = static_box((0, h-floorH), w, floorH)
floor.color = Color('Red')
floor.elasticity=1.2

lttr_D = text_with_font((204, 400), "D", "./Fonts/Diploe-Bold.otf",200)
lttr_i = text_with_font((335, 400), "i", "./Fonts/Diploe-Bold.otf",200)
lttr_p = text_with_font((385, 400), "p", "./Fonts/Diploe-Bold.otf",200)
lttr_l = text_with_font((495, 400), "l", "./Fonts/Diploe-Bold.otf",200)
lttr_o = text_with_font((542, 400), "o", "./Fonts/Diploe-Bold.otf",200)
lttr_e = text_with_font((656, 400), "e", "./Fonts/Diploe-Bold.otf",200)

umlaut_1 = ball((580,375),15,.7)
umlaut_2 = ball((620,375),15,.7)

#caption1.angle = 0
#caption1.wrap = True
#caption1.elasticity=.8
#caption1.hit((-1000,-3500), (200,60))
#caption1.friction=fricT

run()
#draw()
