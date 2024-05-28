"""
A traditional Hello World example for PyPhysicsSandbox.  A screencast showing the development
of this example can be found at: https://www.youtube.com/watch?v=xux3z2unaME
"""

from pyphysicssandbox import *

w,h = 1050, 1350
floorH = 100

window('Hello World', w, h)
gravity(0,100)
resistance(.99)

floor = static_box((0, h-floorH), w, floorH)
floor.color = Color(
    'white')
floor.elasticity=1.2

caption = text((425, 0), 'Hello World!')
caption.angle = 10
caption.wrap = True
caption.elasticity=.55

caption2 = text((325, 200), 'I am Diplöe')
caption2.angle = -3
caption2.wrap = True
caption2.elasticity=.55

caption3 = text((100, 0), 'Hello!')
caption3.angle = 10
caption3.wrap = True
caption3.elasticity=.55

# boxxa = box((180, 0),523, 112)
# boxxa.elasticity=.75

# boxxy = box((100, 100),523, 112)
# boxxy.elasticity=.25

# boxx = box((125, 320),523, 112)
# boxx.elasticity=.55

# boxxx = box((355, 420),523, 112)
# boxxx.elasticity=.55

run()
