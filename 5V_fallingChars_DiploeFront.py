simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas

from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph
import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "5V_Falling_Chars_DiploeFront"
canvas.render_width  = 1080
canvas.render_height = 1920
canvas.frames_x_second = 30
canvas.simulation_render_time = 15
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:

#----------------------
canvas.gravity(0,200)  ###👈🏼👈🏼GRAVITY:(x,y)
canvas.resistance(.95) #sandbox default is .95
gral_elasticity = .9   #sandbox default is .9
gral_friction   = .6   #sandbox default is .6
#categories
cat1 = 0b100
cat2 = 0b010
cat3 = 0b001
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
floor_h = 200
floor_color = Color("Red")
wall_w =  200
wall_color = Color("Blue")
y_limit = "floor"

###🎨 COLOR SWATCHES: 🎨
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
diploe_black  = rgb_to_normalized(0,0,0,255)
####----------------------------------------

#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Grey")
background.db_color = diploe_grey

### Physicsiphy world:
left_wall  = static_box((-wall_w,0), wall_w, rh)
right_wall = static_box((rw,0), wall_w, rh)
left_wall.color  = wall_color
right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh), rw, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0-rh), rw, floor_h)
floor.color = floor_color



#### DrawBot

########## FUNCTIONS:

def add_counter_and_make_fslocal(string,font_path,font_size,font_variations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    f.tracking(-1.25)
    if font_variations: 
        f.fontVariations(**font_variations)
    if not lineHeight:
        lineHeight = font_size*0.9
    f.lineHeight(lineHeight) 

    for i, c in enumerate(string):
        f += c
        f.getNSObject().addAttribute_value_range_("char.counter", i, (i, 1))
    return f

def fallingParagraphlocal(fs_by_lines, text_box, color_name, font_path, font_size, font_variations=None, line_angle=0, keep_first_height=False):
    my_shapes = {}   
    

    #####Make a rect for every line
    #print(f"🤓text_box-orig:{text_box}")
    text_box = (text_box[0],canvas.render_height-text_box[1]-text_box[3], text_box[2],text_box[3])#👈🏼convert pysics coords TO drawBot COORDS
    for i, bounds in enumerate(db.textBoxCharacterBounds(fs_by_lines, text_box)):
        x, y, w, h = bounds.bounds #👈🏼drawBot coords
        #print(f"🤓text_box-new:{text_box}")
        #print(f"😎{bounds.bounds}")
        add_y = y+h#👈🏼add height to Y because pyhsics draws from the other side
        letter_rect = (x,add_y,w,h)

    ## Simulation Objects make:
        the_string = str(bounds.formattedSubString)
        #print(f"the_string: {the_string}")
        #print(f"y: {y}")
        #print(f"👹👹canvas.render_height: {canvas.render_height}")

        new_y = canvas.render_height-letter_rect[1]#👈🏼convert drawBot coords TO PHYSICS COORDS
        new_p = (letter_rect[0],new_y)
        #new_y = y
        #print(f"🦋 {new_y}")
        my_shapes[i]= (new_p,
                        textBox_with_font(new_p,letter_rect[2],letter_rect[3],
                                          the_string,font_path,font_size,font_variations=font_variations))
        my_shapes[i][1].color=Color(color_name)
        my_shapes[i][1].angle=line_angle
        my_shapes[i][1].category=cat2
    return my_shapes


##########////FUNCTIONS
####------------------

the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 180
text_color_name = (230,228,102,255)

text_box_A = (100, -2200, 880, 2400)
the_text_A = "Equality is a vital need of the human soul. It consists in a recognition, at once public, general, effective and genuinely expressed in institutions and customs, that the same amount of respect and consideration is due to every human being because this respect is due to the human being as such and is not a matter of degree. It follows that the inevitable differences among men ought never to imply any difference in the degree of respect. And so that these differences may not be felt to bear such an implication, a certain balance is necessary between equality and inequality. A certain combination of equality and inequality is formed by equality of opportunity. If no matter who can attain the social rank corresponding to the function he is capable of filling, and if education is sufficiently generalized so that no one is prevented from developing any capacity simply on account of his birth, the prospects are the same for every child- In this way, the prospects for each man are the same as for any other man, both as regards himself when young, and as regards his children later on. But when such a combination acts alone, and not as one factor amongst other factors, it ceases to constitute a balance and contains great dangers. To begin with, for a man who occupies an inferior position and suffers from it to know that his position is a result of his incapacity and that everybody is aware of the fact is not any consolation, but an additional motive of bitterness ; according to the individual character, some men can thereby be thrown into a state of depression, while others can be encouraged to commit crime. Then, in social life, a sort of aspirator towards the top is inevitably created. If a descending movement does not come to balance this ascending movement, the social body becomes sick. To the extent to which it is really possible for the son of a farm labourer to become one day a minister, to the same extent should it really be possible for the son of a minister to become one day a farm labourer. This second possibility could never assume any noticeable proportions without a very dangerous degree of social constraint."
the_fontVariations_A ={"wdth":80,"wght":900,"slnt":0}
fs_w_counter_A = add_counter_and_make_fslocal(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size)

fallingParagraphlocal(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=-1)

boxA=(200,-600,rw-500,200)
box_a = textBox_with_font((boxA[0], boxA[1]),boxA[2],boxA[3],"Diplöe","fonts/Diploe-ExtraLightItalic.otf",200)
box_a.color    = Color("Black")
box_a.db_color = diploe_black
box_a.elasticity = gral_elasticity
box_a.category   = cat1
box_a.hit((0,-1500000),(0,0))

boxA=(200,-400,rw-500,190)
box_a = textBox_with_font((boxA[0], boxA[1]),boxA[2],boxA[3],"Diplöe","fonts/Diploe-LightItalic.otf",200)
box_a.color    = Color("Black")
box_a.db_color = diploe_black
box_a.elasticity = gral_elasticity
box_a.category   = cat1
boxA=(200,-200,rw-500,190)
box_a = textBox_with_font((boxA[0], boxA[1]),boxA[2],boxA[3],"Diplöe","fonts/Diploe-MediumItalic.otf",200)
box_a.color    = Color("Black")
box_a.db_color = diploe_black
box_a.elasticity = gral_elasticity
box_a.category   = cat1
boxA=(200,000,rw-500,190)
box_a = textBox_with_font((boxA[0], boxA[1]),boxA[2],boxA[3],"Diplöe","fonts/Diploe-BoldItalic.otf",200)
box_a.color    = Color("Black")
box_a.db_color = diploe_black
box_a.elasticity = gral_elasticity
box_a.category   = cat1
run(simulation_on)