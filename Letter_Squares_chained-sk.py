import drawBot as db
from pyphysicssandbox import *
from random import random

myText = "How to hijack frames from drawbot rect letters and numbers: 0987654321 ?"

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
gravity = (10,-500)

window('Hello World', w, h, fps=30)
resistance(.55)

left_wall= static_box((0,0), wallW, h)
left_wall.elasticity=0.2

floor = static_box((0, h-floorH), w, floorH)
floor.color = Color('Red')
floor.elasticity = 1
####

my_shapes = []

#print(f"😳 {db.textBoxCharacterBounds(fs_w_counter, text_box)}")

letter_rect_prev = [0,0,0,0]
for i, bounds in enumerate(db.textBoxCharacterBounds(fs_w_counter, text_box)):
    db.fill(random(), random(), random(), .5)
    x, y, w, h = bounds.bounds 
    #rect(x, y, w, h)  
    path = db.BezierPath()            
    label = str(bounds.formattedSubString)
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
        
        letter_rect = [minx+add_X, miny+add_Y, maxx-minx, maxy-miny]    
        startCoord = (letter_rect[0],letter_rect[1]-1000)
        db.rect(*letter_rect)
        startCoord_prev = startCoord
        my_shapes.append(textBox((letter_rect[0], 1000-letter_rect[1]),letter_rect[2], letter_rect[3],label))
    else:
        my_shapes.append(textBox((letter_rect[0], 1000-letter_rect[1]),letter_rect[2], letter_rect[3],""))
    
    my_shapes[i].elasticity = .5

        
        #spring(startCoord, my_shapes[i], startCoord_prev[0]-100, my_shapes[i], startCoord[0]-startCoord_prev[0], .9, .9)

run()