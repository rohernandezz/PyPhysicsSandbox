import drawBot as db
from pyphysicssandbox import *
from random import random, choice

myText = "Prueba de gusano"

def add_counter_and_make_fs(string):
    f = db.FormattedString()
    f.font("Helvetica")
    f.lineHeight(89)
    f.fontSize(100)
    for i, c in enumerate(myText):      
        f += c
        f.getNSObject().addAttribute_value_range_("char.counter", i, (i, 1))          
    return f
    
fs_w_counter = add_counter_and_make_fs(myText)

text_box = (50, 10, 900, 800)

####
w,h = 1050, 1350
floorH = 100
wallW=10
fricT=.5

gravity(-1,500)

window('Hello World', w, h, fps=30)
resistance(.55)

left_wall= static_box((0,0), wallW, h)
left_wall.elasticity=0.2

floor = static_box((0, h-floorH), w, floorH)
floor.color = Color('Red')
floor.elasticity= 1.5
####

my_shapes = {}

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

        my_shapes[i]= ((letter_rect[0],letter_rect[1]), text((letter_rect[0], letter_rect[1]),"Prueba de gusano de letras conectadas"[i]))
        my_shapes[i][1].elasticity=.9

    else:
        my_shapes[i]= ((letter_rect[0],letter_rect[1]), box((letter_rect[0], letter_rect[1]),letter_rect[2], letter_rect[3]))
        my_shapes[i][1].elasticity=0.1
        my_shapes[i][1].color=Color("White")
        
    if i > 0:
        prevShape = my_shapes[i-1]
        thisShape = my_shapes[i]
        print(thisShape[1],prevShape[1])
        spring(prevShape[0], prevShape[1], thisShape[0], thisShape[1], thisShape[0][0]-prevShape[0][0]*1.2, 1000, 500)

run()