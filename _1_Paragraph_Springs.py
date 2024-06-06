simulation_on = False
#simulation_on = True
##############################
from pyphysicssandbox import *
import drawBot as db


########## FUNCTIONS:
def make_fs(string,font_path,font_size,fontVariations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    #f.align('left')
    f.fontSize(font_size)
    if fontVariations:
        f.fontVariations(**fontVariations)
    if not lineHeight:
        lineHeight = font_size*0.9
    f.lineHeight(lineHeight) 
    f+=string
    return f
##########////FUNCTIONS

#----------------
#General Settings:
#----------------
win_width = 2000
win_height = 1000
w,h = win_width, win_height
window('Paragraph with springs Demo', w, h, fps=30)
#-----------------------------
gravity(-100,300)       ###👈🏼👈🏼GRAVITY
resistance = .95     #sandbox default is .95
gral_elasticity = .9 #sandbox default is .9
gral_friction   = .6   #sandbox default is .6
#---------------------------------------------------
##------------
## Setup data:
##------------
'''
Setup variables, coordinates, data, etc, here:
'''
##
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
###----------------------------------------
### Physicsiphy world:
left_wall  = static_box((0,0), wall_w, h)
right_wall = static_box((w-wall_w,0), wall_w, h)
left_wall.color = wall_color
right_wall.color = wall_color
#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, h-floor_h), w, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), w, floor_h)
floor.color = floor_color
#### Background
background = cosmetic_box((0, 0), w, h)
background.color = Color("Grey")
background.db_color = diploe_grey

#### DrawBot

####------------------
text_box = (1100, 350, 780, 700)
myText = "To be rooted is perhaps the most important and least recognized need ofj the human soul. It is one opf the hardest to define. Ap human being has roots by virtue of his real, active and natural participation in the life of a community which preserves in living shape certain particular treasures of the past and certain particular expectations for the future. This participation is a natural one, in the sense that it is automatically brought about by place, conditions of birth, profession and social surroundings. Every human being needs to have multiple roots. It is necessary for him to draw wellnigh the whole of his moral, intellectual and spiritual life by way of the environment of which he forms a natural part. asdfjkah gsdflkjahs."
the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 60
#db.font(the_font_path)
#db.fontSize(the_font_size)
#db.lineHeight(the_font_size*.85) 
fs_w_counter = make_fs(myText,the_font_path,the_font_size,fontVariations={"wdth":80,"wght":400,})
my_shapes = {}

#####Make a rect for every character
for i, bounds in enumerate(db.textBoxCharacterBounds(fs_w_counter, text_box)):
    #db.fill(random(), random(), random(), .5)
    x, y, w, h = bounds.bounds 
    print(f"🤪({bounds.bounds}")
    #y = win_height-y
    this_baselineOffset = bounds.baselineOffset
    #rect(x, y, w, h)  
    path = db.BezierPath()            
    path.text(bounds.formattedSubString)
    if path.bounds():
        _x, _y, _w, _h = path.bounds()
    else:
        _x, _y, _w, _h = 0,0,0,0

    add_X = x
    add_Y = y

    if path.bounds()== None:
        minx, miny, maxx, maxy = 0,0,1,1
    else:   
        minx, miny, maxx, maxy = path.bounds()
        
    letter_rect = (add_X, add_Y + maxy -_y, maxx - minx, maxy- miny)
        
## Simulation Objects setup:
##--------------------------
    the_string = str(bounds.formattedSubString)
    #print(f"the_string: {the_string}")

    my_shapes[i]= ((letter_rect[0],win_height-letter_rect[1]),
                    textBox_with_font((letter_rect[0],win_height-letter_rect[1]),letter_rect[2],letter_rect[3],the_string,the_font_path,the_font_size))
    #my_shapes[i][1].body.center_of_mass=(100,0)
##------------------------------------------------------


run(True)