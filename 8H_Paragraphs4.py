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
canvas.window_title = "8H_paragraphsv3b"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 30
canvas.simulation_render_time = 18
#Default canvas color:
canvas.color("Black")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:

#----------------------
canvas.gravity(-16,-400)  ###👈🏼👈🏼GRAVITY:(x,y)
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
wall_w =  5
wall_color = Color("Blue")
y_limit = "ceiling"

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
right_wall = static_box((rw,0), wall_w, rh*.76)
#left_wall.color = wall_color
#right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((0, rh), rw, floor_h)    
    floor.color = floor_color
    floor.elasticity= 0.1
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0-floor_h), rw, floor_h)
    ceiling.color = floor_color
    



#### DrawBot

####------------------

the_font_path = "fonts/VF/DiploeVF.ttf" 
the_font_size = 70
text_color_name = "Black"

text_box_A = (100, 800, 800, 800)
the_text_A = "Even without a military conquest, money-power and economic domination can so impose a foreign influence as actually to provoke this disease of uprootedness."
the_text_A = the_text_A
the_fontVariations_B ={"wdth":140,"wght":300,"slnt":-11}
fs_w_counter_A = make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_B, lineHeight=the_font_size*1.1)

text_box_B = (800, 2500, 900, 800)
the_text_B = "Finally, the social relations existing in any one country can be very dangerous factors in connexion with uprootedness. In all parts of our country at the present time — and setting aside the question of the conquest — there are two poisons at work spreading this disease. One of them is money. Money destroys human roots wherever it is able to penetrate, by turning desire for gain into the sole motive. It easily manages to outweigh all other motives, because the effort it demands of the mind is so very much less. Nothing is so clear and so simple as a row of figures."
the_text_B = the_text_B
the_fontVariations_B ={"wdth":140,"wght":200,"slnt":-11}
fs_w_counter_B = make_fs(the_text_B, the_font_path, the_font_size, font_variations=the_fontVariations_B, lineHeight=the_font_size*1.1)

fallingParagraph(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_B,line_angle=0)

a_ledge = static_box((300,1500),650,20)
a_ledge.angle = 45
a_ledge.color = Color("Red")

fallingParagraph(fs_w_counter_B, text_box_B, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_B,line_angle=5)

simone = textBox_with_font((200,450),300,100,"Simone Weil","fonts/DiploeNarrow-Bold.otf",the_font_size)
simone.elasticity=.1
uproot = textBox_with_font((300,530),420,100,"Uprootedness, 1949","fonts/DiploeNarrow-RegularItalic.otf",the_font_size)
uproot.elasticity=.1
run(simulation_on)