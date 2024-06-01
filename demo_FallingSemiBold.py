"""
Demo 2 :: Falling lines of text
"""

from pyphysicssandbox import *

w,h = 1050, 1350
floorH = 100
wallW=10
fricT=.5

window('Hello World', w, h, fps=30)
resistance(.55)

left_wall= static_box((0,0), wallW, h)
left_wall.elasticity=0.2

floor = static_box((0, h-floorH), w, floorH)
floor.color = Color('White')
floor.elasticity=1.2

caption = text((50, 30), 'Hello World!')
caption.angle = 10
caption.wrap = True
caption.elasticity=.75
caption.friction=fricT

caption2 = text((300, 120), 'I am Diplöe')
caption2.angle = 3
caption2.wrap = True
caption2.elasticity=.75
caption2.friction=fricT

caption3 = text((65, 250), 'Hello text types')
caption3.angle = -2
caption3.wrap = True
caption3.elasticity=.75
caption3.hit((-200,-26000), (700,60))
caption3.friction=fricT

caption4 = text((355, 400), 'This is a font')
caption4.angle = 10
caption4.wrap = True
caption4.elasticity=.8
caption4.hit((-1000,-3500), (200,60))
caption4.friction=fricT

# boxxa = box((180, 0),523, 112)
# boxxa.elasticity=.75

# boxxy = box((100, 100),523, 112)
# boxxy.elasticity=.75

# boxx = box((125, 320),523, 112)
# boxx.elasticity=.55

# boxxx = box((355, 420),523, 112)
# boxxx.elasticity=.9

run()
#draw()
