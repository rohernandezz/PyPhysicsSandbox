simulation_on = False
simulation_on = True
##############################
import drawBot as db
from pyphysicssandbox import *
from random import random, choice

########## FUNCTIONS:
def add_counter_and_make_fs(string):
    f = db.FormattedString()
    f.font("Helvetica")
    f.lineHeight(89)
    f.fontSize(100)
    for i, c in enumerate(myText):      
        f += c
        f.getNSObject().addAttribute_value_range_("char.counter", i, (i, 1))          
    return f
##########

#----------------
#General Settings:
#----------------
win_width = 1080
win_height = 1920
w,h = win_width, win_height
window('Falling_Diploe_01', w, h, fps=30)
#-----------------------------
gravity(0,300)       ###👈🏼👈🏼GRAVITY
resistance = .95     #sandbox default is .95
gral_elasticity = .9 #sandbox default is .9
gral_friction   = .6   #sandbox default is .6
#---------------------------------------------------

##-------------
## World setup:
##-------------
'''
Setup foor, walls, anchors, etc, here: ---
'''
### World variables:
floor_h = 2
floor_color = Color("Red")
wall_w =  5
wall_color = Color("Blue")
y_limit = "floor"
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)

### Physicsiphy world:
left_wall  = static_box((0,0), wall_w, h)
right_wall = static_box((w-wall_w,0), wall_w, h)
left_wall.color = wall_color
right_wall.color = wall_color
#### Background
background = cosmetic_box((0, 0), w, h)
background.color = Color("Grey")
background.db_color = diploe_grey
#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, h-floor_h), w, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), w, floor_h)
floor.color = floor_color

#### DrawBot
myText = "Diplöe was made for falling"
the_font_path = "fonts/Diploe-BlackItalic.otf"
the_font_size = 100
db.font(the_font_path)
db.fontSize(the_font_size)
fs_w_counter = add_counter_and_make_fs(myText)
text_box = (50, 10, 900, 800)

my_shapes = {}


#####Make a rect for every character
for i, bounds in enumerate(db.textBoxCharacterBounds(fs_w_counter, text_box)):
    db.fill(random(), random(), random(), .5)
    x, y, w, h = bounds.bounds 
    #rect(x, y, w, h)  
    path = db.BezierPath()            
    path.text(bounds.formattedSubString)
    if path:
        add_X = x
        add_Y = y+bounds.baselineOffset
        with db.savedState():
            db.translate(x, y + bounds.baselineOffset)
            db.drawPath(path)
            db.fill(None)
            db.stroke(random(), random(), random(), .5)
            minx, miny, maxx, maxy = path.bounds()
            db.rect(minx, miny, maxx-minx, maxy-miny)
        
        letter_rect = (minx+add_X, miny+add_Y, maxx-minx, maxy-miny)    
        db.rect(*letter_rect)

        my_shapes[i]= ((letter_rect[0],letter_rect[1]), textBox_with_font((letter_rect[0], letter_rect[1]),letter_rect[2],letter_rect[3],myText[i],the_font_path,the_font_size-40))
        my_shapes[i][1].elasticity=.9

    else:
        my_shapes[i]= ((letter_rect[0],letter_rect[1]), box((letter_rect[0], letter_rect[1]),letter_rect[2], letter_rect[3]))
        my_shapes[i][1].elasticity=0.1
        my_shapes[i][1].color=Color("White")
        my_shapes[i][1].db_color= (None,None,None,None)
        
    # if i > 0:
    #     prevShape = my_shapes[i-1]
    #     thisShape = my_shapes[i]
    #     print(thisShape[1],prevShape[1])
    #     spring(prevShape[0], prevShape[1], thisShape[0], thisShape[1], thisShape[0][0]-prevShape[0][0]*1.2, 1000, 500)        

####------------------

run()