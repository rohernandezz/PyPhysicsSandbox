box_stroke_on = False
import drawBot
import pygame
import pymunk
import math

from .box_shape import Box
from .base_shape import BaseShape
from pyphysicssandbox import canvas

class TextBox(Box):
    def __init__(self, space, x, y, width, height, caption, font_path, font_size, mass, static, font_variations=False, cosmetic=False):

        self.width =  width
        self.height = height
        self.font = pygame.font.Font(font_path, font_size)
        self.font_path = font_path
        self.font_size = font_size
        self.label_fs = False
        
        if font_variations:
            self.font_variations = font_variations
        else:
            self.font_variations = None

        self.text_align='left'

        #👇🏼DONT care about the textSize cause it'll be a drawBot textBox, and if it doesn't fit, drawBot will handle
        #👇🏼.....write smth to handle better preview *LATER*
        #width, height = self.font.size(caption) 
        #print(self.font.size(caption))#SIZE OF TEXT DRAWING CALCULATED BY PYGAME
        
        if type(caption) == str: 
            #print("IZ STRING")
            self.caption = caption

        if type(caption).__name__ == 'FormattedString':
             print("FORMATTTTTTTTTedString")
             self.caption = str(caption)
             self.label_fs = caption
        else:
            self.caption = caption

        self.space = space #simulation space
        self.static = static 

        box_x = x #does NOT add half the width 'cause the _textBox() from __init__ already did
        box_y = y #does NOT add half the width 'cause the _textBox() from __init__ already did
        self._x = box_x
        self._y = box_y

        super().__init__(space, box_x, box_y, width, height, 3, mass, static, cosmetic)

        #Renders text label in pygame:
        self.label = self.font.render(self.caption, True, self.color)

    def _draw(self, screen):
        if self._cosmetic:
            x = self._x-self.width/2
            y = self._y-self.height/2
            ps = [(x, y), (x+self.width, y), (x+self.width, y+self.height), (x,y+self.height), (x, y)]
        else:
            ps = [self.body.local_to_world(v) for v in self.shape.get_vertices()]
            ps += [ps[0]]

        degrees = self.angle
 
        ##👾pygame:
        #Draw rect lines
        pygame.draw.lines(screen, self.color, False, ps, self.radius)
        #Draw pygame text
        rotated = pygame.transform.rotate(self.label, degrees)
        size = rotated.get_rect()
        screen.blit(rotated, (self.position.x-(size.width/2), self.position.y-(size.height/2)))

        ##👾drawBot:        
        #render_width  = canvas.render_w
        
        shifted_y = canvas.render_height-self.position.y

        if self.label_fs:
            this_label_fs = self.label_fs
        else:
            this_label_fs = drawBot.FormattedString(align=self.text_align)
            this_label_fs.font(self.font_path)
            this_label_fs.fontSize(self.font_size)
            ##### FONT VARIATIONS
            if self.font_variations:
                #print(f'aaaaa___{self.font_variations}')
                this_label_fs.fontVariations(**self.font_variations)    
            #var_slnt_value = drawBot.remap(self.position.x, 0, render_width, 0, -11)
            #var_wght_value = drawBot.remap(shifted_y, render_height, 0, 200, 600)
            
            #####///FONT VARIATIONS
            this_label_fs.lineHeight(self.font_size*0.95)
            this_label_fs.fill(*self.db_color)
            this_label_fs.append(self.caption)

        with drawBot.savedState():
            drawBot.rotate(degrees, center=(self.x, canvas.render_height-self.y))
            #drawBot.translate(-self.width/2,-self.height/2) #Go back to 0,0 
            
            with drawBot.savedState():    
                drawBot.fill(None)
                drawBot.stroke(None)
                db_text_rect= (self.position.x-self.width/2,shifted_y-self.height/2,self.width,self.height)
                #drawBot.fill(.9,.9,.9,.8) #grey fill 
                if box_stroke_on:
                    drawBot.stroke(0)
                drawBot.rect(*db_text_rect)
            
            #Descomponer rectangulo:
            origin_x,origin_y = db_text_rect[0],db_text_rect[1]
            _w, _h = db_text_rect[2],db_text_rect[3]
            
            if len(this_label_fs) == 1: #####SINGLE CHARACTER
                path = drawBot.BezierPath()
                path.text(this_label_fs)
                
                with drawBot.savedState():
                    if self.text_align == "left":
                        drawBot.translate(origin_x,origin_y)
                        #print("🤖🤖🤖")
                    elif self.text_align == "center": 
                        #print("💄💄💄💄")
                        drawBot.translate(origin_x+self.width/2,origin_y)
                    drawBot.fill(*self.db_color)
                    drawBot.drawPath(path)

            else: ####LINE OF TEXT?
                with drawBot.savedState():
                    #drawBot.translate(origin_x+self.width/2,origin_y)
                    drawBot.fill(*self.db_color)
                    hardcoded_baseline_offset = _h*.22#HACKING BASELINE OFFSET HERE, HARDCODED👈🏼
                    drawBot.translate(origin_x,origin_y+hardcoded_baseline_offset)
                    drawBot.text(this_label_fs,(0,0)) 
                    #print(f"the_string: {this_label_fs}")
                    #print(f"😎Rect: {db_text_rect}")


    def __repr__(self):
        prefix = 'box'

        if self.static:
            prefix = 'static_box'

        if self._cosmetic:
            prefix = 'cosmetic_box'

        return prefix+': p(' + str(self.position[0]) + ',' + str(self.position[1]) + '), caption: ' + self.caption + \
                        ', angle: ' + str(self.angle)

    @BaseShape.color.setter
    def color(self, value):
        BaseShape.color.fset(self, value)
        self.label = self.font.render(self.caption, True, self.color)

    @property
    def text(self):
        return self.caption

    @text.setter
    def text(self, value):
        if type(value) == str:
            self.caption = value
            self.label = self.font.render(self.caption, True, self.color)

            if not self._cosmetic:
                #👇🏼 Not calculating size, keeping the same text box
                #width, height = self.font.size(value)
                #height -= self.font.get_ascent()

                moment = pymunk.moment_for_box(self.body.mass, (self.width, self.height))

                if self.static:
                    body = pymunk.Body(self.body.mass, moment, pymunk.Body.STATIC)
                else:
                    body = pymunk.Body(self.body.mass, moment)

                body.position = self.position
                shape = pymunk.Poly.create_box(body, (self.width, self.height), self.radius)
                
                #self.width = width
                #self.height = height

                self.space.remove(self.body, self.shape)
                self.body = body
                self.shape = shape
                self.space.add(self.body, self.shape)
        else:
            print("Text value must be a string")
