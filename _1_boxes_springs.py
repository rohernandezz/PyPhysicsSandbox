import drawBot
from pyphysicssandbox import *

win_width = 1000
win_height = 1000
w,h = win_width, win_height

window('DEMO_0', w, h, fps=30)
resistance = .95
floorH = 1
wallW =  5
fricT =.7
gravity(0,300)
gral_elasticity = .5

wall_elasticity = 0.2

# Static boxes
right_wall= static_box((w-wallW,0), wallW, h)
floor = static_box((0, h-floorH), w, floorH)
floor.color = Color("#FF000000")  
floor._db_color = (.9,0,.2)       
floor.elasticity = .6

# Text box setup
my_fs = drawBot.FormattedString()
my_fs.font("fonts/VF/DiploeVF.ttf")
my_fs.fontVariations(wght=100,wdth=400)
my_fs.align("left")
my_fs.fill(1,0,0)
my_fs.fontSize(100)
my_fs.append("this box")


my_fs2 = drawBot.FormattedString()
my_fs2.font("fonts/VF/DiploeVF.ttf")
my_fs2.fontVariations(wght=400,wdth=20)
my_fs2.align("left")
my_fs2.fill(0,1,0)
my_fs2.fontSize(100)
my_fs2.append("falls and stuff")

boxA=(200,0,600,120)
box_a = textBox((boxA[0], boxA[1]),boxA[2],boxA[3],my_fs)
box_a.elasticity= gral_elasticity

boxB=(200,400,600,120)
box_b = textBox((boxB[0], boxB[1]),boxB[2],boxB[3],my_fs2)
box_b.elasticity= gral_elasticity


# Static anchors
center_anchor_a  = static_ball((500,10),10)
center_anchor_a.color = Color("Red")

left_anchor_a  = static_ball((0,460),10)
left_anchor_a.color = Color("Green")
right_anchor_a = static_ball((w,460),10)
right_anchor_a.color = Color("Blue")

# Print initial positions for debugging
print(f"::::: Box A position: {box_a.body.position}")
print(f"::::: Basldkfjañlsdkfj: {box_a.body}")
#print(f"::::: Center anchor position: {left_anchor_a.body.position}")
#print(f"::::: Left anchor position: {left_anchor_a.body.position}")
#print(f"::::: Right anchor position: {right_anchor_a.body.position}")

# Create springs

_a = 350
_b = 200000
_c = 10000

theeee = spring((350,160), box_a, (500,160), center_anchor_a, _a, _b*1.2, _c)
print(theeee )
theeee_2 = spring((1000-350,160), box_a, (500,160), center_anchor_a, _a, _b, _c)
print(theeee_2)

x_theeee = spring((350,460), box_b, (500,100), left_anchor_a, _a*1.4, _b*1.5, _c)
print(x_theeee)
x_theeee_2 = spring((1000-350,460), box_b, (500,100), right_anchor_a, _a*1.4, _b*1.6, _c)
print(x_theeee_2)

run()
