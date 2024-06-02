import drawBot
import pygame
import pymunk
import math

from .box_shape import Box
from .base_shape import BaseShape


class TextBox(Box):
    def __init__(self, space, x, y, width, height, caption, font_path, font_size, mass, static, cosmetic=False):

        self.width =  width
        self.height = height

        self.font = pygame.font.Font(font_path, font_size)
        self.font_path = font_path
        self.font_size = font_size

        #👇🏼DONT care about the textSize cause it'll be a drawBot textBox, and if it doesn't fit, drawBot will handle
        #👇🏼.....write smth to handle better preview *LATER*
        #width, height = self.font.size(caption) 
        #print(self.font.size(caption))#SIZE OF TEXT DRAWING CALCULATED BY PYGAME 

        self.caption = caption #the text string
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
        #Draw pygame kktext
        rotated = pygame.transform.rotate(self.label, degrees)
        size = rotated.get_rect()
        screen.blit(rotated, (self.position.x-(size.width/2), self.position.y-(size.height/2)))

        ##👾drawBot:
        label_fs = drawBot.FormattedString(align='center')
        label_fs.font(self.font_path)
        label_fs.fontSize(self.font_size)
        label_fs.fill(*self.db_color)
        label_fs.append(self.caption)

        with drawBot.savedState():
            drawBot.rotate(degrees, center=(self.x, 1000-self.y)) #NEEEDS CONMVEDRTING TO drawbotY👈🏼
            drawBot.translate(-self.width/2,-self.height/2) #Go back to 0,0
            
            with drawBot.savedState():    
                drawBot.fill(None)
                drawBot.stroke(*self.db_color)
                shifted_y = 1000-self.position.y # FIX THIS HARCODED 1350
                db_text_rect= (self.position.x,shifted_y,self.width,self.height)
                drawBot.rect(*db_text_rect)
            drawBot.fill(0)
            drawBot.textBox(label_fs,db_text_rect)

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
