"""
Demo 1 :: Falling Rectangles and type in drawBot
"""
import drawBot
from pyphysicssandbox import *

win_width = 1000
win_height = 1000
w,h = win_width, win_height

floorH = 1
wallW =  10
fricT =.5
gravity(30,-300)

window('DEMO_0', w, h, fps=30)
resistance(.55)

left_wall= static_box((0,0), wallW, h)
left_wall.elasticity=0.1

floor = static_box((0, 0), w, floorH)
#floor.color = Color("red")        #pygame color for live visualization (<-in pygame name notation)
floor.color = Color("#FF000000")  #pygame color for live visualization (<-in pygame rgb HEX notation)
floor._db_color = (.9,0,.2)       #drawBot color for rendering. <-in Db notation)
floor.elasticity = 1.1


my_fs = drawBot.FormattedString()
my_fs.font("fonts/VF/DiploeVF.ttf")
my_fs.fontVariations(wght=100,wdth=800)
my_fs.fill(1,0,0)
my_fs.fontSize(100)
my_fs.append("this box")

#boxxa = box((180, 0),523, 112)  #
boxxa = textBox((80, 500),523,113,my_fs)
boxxa.elasticity=1

boxxy = textBox_with_font((100, 600),523, 112, "was made for", "fonts/DiploeNarrow-Black.otf", 100 )
boxxy.color= Color("pink")
boxxy.elasticity=1

#boxx =     box((125, 320),523, 112)
boxx = textBox_with_font((125, 820),550, 113, "floating", "fonts/DiploeWide-MediumItalic.otf", 100 )
boxx.color= Color('blue')

boxx.elasticity=1

boxxx = textBox_with_font((355, 920),523, 112, "and that's wat it'll do", "fonts/DiploeNarrow-LightItalic.otf", 100 )
boxxx.elasticity=1
boxxx.db_color=(0.2,0,.5)

run(False)

