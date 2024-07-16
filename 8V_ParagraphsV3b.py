simulation_on = False
simulation_on = True
##############################
#from importlib import reload

#import FS_Tools
#reload(FS_Tools)
from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph

from pyphysicssandbox import *
from pyphysicssandbox import canvas

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "8V_paragraphsv3b"
canvas.render_width  = 1080
canvas.render_height = 1920
canvas.frames_x_second = 30
canvas.simulation_render_time = 18
#Default canvas color:
canvas.color("Black")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:

#----------------------
canvas.gravity(16,250)  ###👈🏼👈🏼GRAVITY:(x,y)
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
floor_h = 2
floor_color = Color("Red")
wall_w =  50
wall_color = Color("Green")
y_limit = "floor"

###🎨 COLOR SWATCHES: 🎨
diploe_grey   = rgb_to_normalized(218,219,238,255)
diploe_yellow = rgb_to_normalized(230,228,102,255)
diploe_black  = rgb_to_normalized(230,228,102,255)
####----------------------------------------
#### Background
#background = cosmetic_box((0, 0), rw, rh)
#background.color = Color("Grey")
#background.db_color = diploe_grey

### Physicsiphy world:
left_wall  = static_box((0-wall_w,-rh*3), wall_w, rh*4)
right_wall = static_box((rw,0), wall_w, rh)
#left_wall.color = wall_color
#right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh), rw, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0), rw, floor_h)
floor.color = floor_color



#### DrawBot

####------------------

the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 70
text_color_name = "Black"

text_box_A = (100, -800, 900, 900)
the_text_A = """To be rooted is perhaps the most important and least recognized need of the human soul. It is one of the hardest to define.
A human being has roots by virtue of his real, active and natural participation in the life of a community which preserves in living shape certain particular treasures of the past and certain particular expectations for the future. This participation is a natural one, in the sense that it is automatically brought about by place, conditions of birth, profession and social surroundings. Every human being needs to have multiple roots. It is necessary for him to draw wellnigh the whole of his moral, intellectual and spiritual life by way of the environment of which he forms a natural part.To be rooted is perhaps the most important and least recognized need of the human soul. It is one of the hardest to define. A human being has roots by virtue of his real, active and natural participation in the life of a community which preserves in living shape certain particular treasures of the past and certain particular expectations for the future. This participation is a natural one, in the sense that it is automatically brought about by place, conditions of birth, profession and social surroundings. Every human being needs to have multiple roots. It is necessary for him to draw wellnigh the whole of his moral, intellectual and spiritual life by way of the environment of which he forms a natural part."""
the_text_A = the_text_A
the_fontVariations_A ={"wdth":60,"wght":400,"slnt":0}
fs_w_counter_A = make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*1.1)

text_box_B = (700, -2500, 900, 800)
the_text_B = "Uprootedness occurs whenever there is a military conquest, and in this sense conquest is nearly always an evil. There is the minimum of uprootedness when the conquerors are migrants who settle down in the conquered country, intermarry with the inhabitants and take root themselves. Such was the case with the Hellenes in Greece, the Celts in Gaul and the Moors in Spain. But when the conqueror remains a stranger in the land of which he has taken possession, uprootedness becomes an almost mortal disease among the subdued population. It reaches its most acute stage when there are deportations on a massive scale, as in Europe under the German occupation, or along the upper loop of the Niger, or where there is any brutal suppression of all local traditions, as in the French possessions in the Pacific (if Gauguin and Alain Gerbault are to be believed)."
the_text_B = the_text_B
#the_fontVariations_B ={"wdth":30,"wght":200,"slnt":-11}
fs_w_counter_B = make_fs(the_text_B, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*1.1)

fallingParagraph(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=0)

a_ledge = static_box((1100,-800),900,20)
a_ledge.angle = 25
a_ledge.color = Color("Red")

fallingParagraph(fs_w_counter_B, text_box_B, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=5)

simone = textBox_with_font((500,450),300,100,"Simone Weil",the_font_path,the_font_size,font_variations=the_fontVariations_A )
simone.elasticity=.1
uproot = textBox_with_font((400,530),420,100,"Uprootedness, 1949",the_font_path,the_font_size,font_variations=the_fontVariations_A)
uproot.elasticity=.1
run(simulation_on)