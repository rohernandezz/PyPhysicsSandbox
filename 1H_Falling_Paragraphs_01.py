simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas
import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "1H_Falling_Paragraphs_02"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 60
canvas.simulation_render_time = 10
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:
#----------------------
canvas.gravity(-15,400)  ###👈🏼👈🏼GRAVITY:(x,y)
canvas.resistance(.95) #sandbox default is .95
gral_elasticity = .9   #sandbox default is .9
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

###🎨 COLOR SWATCHES: 🎨
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
diploe_black  = rgb_to_normalized(230,228,102,255)
####----------------------------------------

### Physicsiphy world:
left_wall  = static_box((0,0), wall_w, rh)
right_wall = static_box((rw-wall_w,0), wall_w, rh)
left_wall.color = wall_color
right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh-floor_h), rw, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), rw, floor_h)
floor.color = floor_color

#### Background
background = cosmetic_box((0, 0), rw, rh)
background.color = Color("Grey")
background.db_color = diploe_grey


#### DrawBot

########## FUNCTIONS:
def make_fs(string,font_path,font_size,font_variations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    #f.align('left')
    f.fontSize(font_size)
    if font_variations:
        f.fontVariations(**font_variations)
    if not lineHeight:
        lineHeight = font_size*0.90
    f.lineHeight(lineHeight) 
    f+=string
    return f

def fallingParagraph(fs_by_lines, text_box, color_name, font_path, font_size, font_variations=None, line_angle=0):    
    my_shapes = {}    
    if font_variations:
        the_fontVariations = font_variations

    #####Make a rect for every line
    for i, bounds in enumerate(db.textBoxCharacterBounds(fs_by_lines, text_box)):
        x, y, w, h = bounds.bounds 
        print(f"🤪({bounds.bounds}")
        #this_baselineOffset = bounds.baselineOffset
        path = db.BezierPath()            
        path.text(bounds.formattedSubString)
        if path.bounds():
            _x, _y, _w, _h = path.bounds()
        else:
            _x, _y, _w, _h = 0,0,0,0
        add_X,add_Y = x,y
        if path.bounds()== None:
            minx, miny, maxx, maxy = 0,0,1,1
        else:   
            minx, miny, maxx, maxy = path.bounds()
        letter_rect = (add_X, add_Y + maxy -_y, maxx - minx, maxy- miny)
    ## Simulation Objects make:
        the_string = str(bounds.formattedSubString)
        #print(f"the_string: {the_string}")
        my_shapes[i]= ((letter_rect[0],canvas.win_height-letter_rect[1]),
                        textBox_with_font((letter_rect[0],canvas.win_height-letter_rect[1]),letter_rect[2],letter_rect[3],
                                          the_string,font_path,font_size,font_variations=font_variations))
        my_shapes[i][1].color=Color(color_name)
        my_shapes[i][1].angle=line_angle

    return my_shapes


##########////FUNCTIONS
####------------------

the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 42
text_color_name = "Black"

text_box_A = (1100, 1000, 800, 700)
the_text_A = "Uprootedness occurs whenever there is a military conquest, and in this sense conquest is nearly always an evil. There is the minimum of uprootedness when the conquerors are migrants who settle down in the conquered country, intermarry with the inhabitants and take root themselves. Such was the case with the Hellenes in Greece, the Celts in Gaul and the Moors in Spain. But when the conqueror remains a stranger in the land of which he has taken possession, uprootedness becomes an almost mortal disease among the subdued population. It reaches its most acute stage when there are deportations on a massive scale, as in Europe under the German occupation, or along the upper loop of the Niger, or where there is any brutal suppression of all local traditions, as in the French possessions in the Pacific (if Gauguin and Alain Gerbault are to be believed)."
the_text_A = the_text_A
the_fontVariations_A ={"wdth":80,"wght":400,"slnt":0}
fs_w_counter_A = make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*1.1)


text_box_B = (120, 1600, 500, 700)
the_text_B = "To be rooted is perhaps the most important and least recognized need of the human soul. It is one of the hardest to define. A human being has roots by virtue of his real, active and natural participation in the life of a community which preserves in living shape certain particular treasures of the past and certain particular expectations for the future. This participation is a natural one, in the sense that it is automatically brought about by place, conditions of birth, profession and social surroundings. Every human being needs to have multiple roots. It is necessary for him to draw wellnigh the whole of his moral, intellectual and spiritual life by way of the environment of which he forms a natural part."
the_text_B = the_text_B+the_text_B
the_fontVariations_B ={"wdth":30,"wght":200,"slnt":-11}
fs_w_counter_B = make_fs(the_text_B, the_font_path, the_font_size, font_variations=the_fontVariations_B, lineHeight=the_font_size*1.1)



fallingParagraph(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=-1)
fallingParagraph(fs_w_counter_B, text_box_B, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_B,line_angle=5)

run(simulation_on)