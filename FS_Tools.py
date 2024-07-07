from pyphysicssandbox import *
from pyphysicssandbox import canvas
import random
import drawBot as db

def make_fs(string,font_path,font_size,font_variations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    if font_variations:
        f.fontVariations(**font_variations)
    if not lineHeight:
        lineHeight = font_size*0.90
    f.lineHeight(lineHeight) 
    f+=string
    return f

def add_counter_and_make_fs(string,font_path,font_size,font_variations=None,lineHeight=None):
    f = db.FormattedString()
    f.font(font_path)
    f.fontSize(font_size)
    if font_variations:
        f.fontVariations(**font_variations)
    if not lineHeight:
        lineHeight = font_size*0.9
    f.lineHeight(lineHeight) 

    for i, c in enumerate(string):
        f += c
        f.getNSObject().addAttribute_value_range_("char.counter", i, (i, 1))
    return f


def fallingParagraph(fs_by_lines, text_box, color_name, font_path, font_size, line_height=None, font_variations=None, line_angle=0, split_characters=False,category=None,gravity=None):
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
        
        if isinstance(line_angle, tuple):
            if len(line_angle) == 2:
                the_line_angle=random.uniform(line_angle[0],line_angle[1])
            else:
                the_line_angle=0
                print("line angle not valid, defaulting to 0")
        else:
            the_line_angle = line_angle

        if split_characters:
            this_baselineOffset = bounds.baselineOffset
            #print(f"this_baselineOffset: {this_baselineOffset}")
            path = db.BezierPath()            
            path.text(bounds.formattedSubString)
            add_X = x
            #print(f"add_X: {add_X}")
            add_Y = y+this_baselineOffset
            #print(f"add_Y: {add_Y}")
            if path.bounds():
                minx, miny, maxx, maxy = path.bounds()
                #print(f"path.bounds(): {path.bounds()}")
            else:
                print("noBounds")
                #letter_rect = (add_X, add_Y+maxy-miny, 2, 2)
                
            letter_rect = (add_X, add_Y+maxy-miny, maxx - minx, maxy- miny)
        
        
        print(letter_rect)
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

      


        my_shapes[i][1].angle=the_line_angle

        if category:
            my_shapes[i][1].category=category
        if gravity:
            #print("GRAVITY!!!")
            my_shapes[i][1].gravity=gravity    
    return my_shapes