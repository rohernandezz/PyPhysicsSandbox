simulation_on = False
simulation_on = True
##############################
from pyphysicssandbox import *
from pyphysicssandbox import canvas
from random import randint

from FS_Tools import make_fs, add_counter_and_make_fs, fallingParagraph
import drawBot as db

#=================
#General Settings:
#=================
#👉🏼👉🏼Canvas settings:
#-------------------
canvas.window_title = "7H_TextureBold_b"
canvas.render_width  = 2000
canvas.render_height = 1000
canvas.frames_x_second = 10
canvas.simulation_render_time = 1
#Default canvas color:
canvas.color("Green")

rw,rh = canvas.render_width, canvas.render_height
w,h = canvas.win_width, canvas.win_height

#----------------------
#Gral physics settings:

#----------------------
canvas.gravity(0,400)  ###👈🏼👈🏼GRAVITY:(x,y)
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
wall_w =  100
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
#left_wall  = static_box((-wall_w,0), wall_w, rh)
#right_wall = static_box((rw,0), wall_w, rh)
#left_wall.color  = wall_color
#right_wall.color = wall_color

#### Floor or ceiling: (both use floorH:int)
if y_limit == "floor":
    floor      = static_box((-rw/2, rh), rw*2, floor_h)    
elif y_limit == "ceiling":
    ceiling    = static_box((0, 0-rh), rw, floor_h)

#floor.color = floor_color
floor.category = cat1



#### DrawBot

####------------------


def makeRender(variations):

    canvas.window_title           = title
    the_fontVariations_A = variations
    
    the_font_path = "fonts/VF/DiploeVF.ttf" 
    the_font_size = 280
    text_color_name = (230,228,102,255)

    text_box_A = (-60, -1800, rw*1.2, 2000)
    the_text_A = "L’enracinement est peut-être le besoin le plus important et le plus méconnu de l’âme humaine. C’est un des plus difficiles à définir. Un être humain a une racine par sa participation réelle, active et naturelle à l’existence d’une collectivité qui conserve vivants certains trésors du passé et certains pressentiments d’avenir. Participation naturelle, c’est-à-dire amenée automatiquement par le lieu, la naissance, la profession, l’entourage. Chaque être humain a besoin d’avoir de multiples racines. Il a besoin de recevoir la presque totalité de sa vie morale, intellectuelle, spirituelle, par l’intermédiaire des milieux dont il fait naturellement partie. Les échanges d’influences entre milieux très différents ne sont pas moins indispensables que l’enracinement dans l’entourage naturel. Mais un milieu déterminé doit recevoir une influence extérieure non pas comme un apport, mais comme un stimulant qui rende sa vie propre plus intense. […] Il serait vain de se détourner du passé pour ne penser qu’à l’avenir. C’est une illusion dangereuse de croire qu’il y ait même là une possibilité. L’opposition entre l’avenir et le passé est absurde. L’avenir ne nous apporte rien, ne nous donne rien ; c’est nous qui pour le construire devons tout lui donner, lui donner notre vie elle-même. Mais pour donner il faut posséder, et nous ne possédons d’autre vie, d’autre sève, que les trésors hérités du passé et digérés, assimilés, recréés par nous. De tous les besoins de l’âme humaine, il n’y en a pas de plus vital que le passé."
    the_text_A = the_text_A
    fs_w_counter_A = add_counter_and_make_fs(the_text_A, the_font_path, the_font_size, font_variations=the_fontVariations_A, lineHeight=the_font_size*.8)

    fallingParagraph(fs_w_counter_A, text_box_A, text_color_name,the_font_path, the_font_size, font_variations=the_fontVariations_A,line_angle=(-6,2),category=cat1,split_characters=True)

    run(simulation_on)

#fontVariations_list =[
#                        {"wdth":100,"wght":900,"slnt":0},
#                        {"wdth":150,"wght":900,"slnt":0},
#                        ]


wdth_list = [50,100,150]
wght_list = [200,300,400,500,600,700,900]
slnt_list = [0,-11]

for wdth_value in wdth_list:
    for wght_value in wght_list:
        for slnt_value in slnt_list:
            variations = {"wdth":wdth_value,"wght":wght_value,"slnt":slnt_value}
            title = f"wdth{wdth_value}_wght{wght_value}_slnt{slnt_value}"
            print(f"💕 {title}")
            makeRender(variations)

#for variations in fontVariations_list:
#    title = f"{variations}"
#    print(f"💕 {title}")
#    makeRender(variations)