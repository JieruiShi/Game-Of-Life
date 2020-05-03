import pygame
"""
pygame.init()
screen = pygame.display.set_mode((500,500))
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (127,127,127)"""


class Button:
    """
    build function includes both the button and the text within, rectangular button only
    (x,y,width,height,colour,colour2,framecolour,boldness) sets the property of the button and frame
    (TEXT, textcolour, textcolour2, textsize, textfont) sets the property of the text within the button
    The text is set to be in the centre of the text box and will have only one line.
    """
    def __init__(self,canvas,x,y,width,height,colour,colour2, framecolour, boldness = 3, TEXT = None, textcolour = (255,255,255), textcolour2 = (255,255,255), textsize = 20, textfont = "Times New Roman"):
        self.canvas = canvas
        self.x = x - width/2
        self.y = y - height/2
        self.width = width
        self.height = height
        self.colour = colour
        self.colour2 = colour2
        self.framecolour = framecolour
        self.boldness = boldness
        self.text = TEXT
        self.textcolour = textcolour
        self.textcolour2 = textcolour2
        self.font = pygame.font.SysFont(textfont, textsize)
        self.rendertext = self.font.render(TEXT, True, textcolour)
        self.rendertext2 = self.font.render(TEXT,True,textcolour2)
        self.textwidth = self.rendertext.get_width()
        self.textheight = self.rendertext.get_height()

    # checks if the mouse is within the button
    def mouseIn(self):
        pos = pygame.mouse.get_pos()
        return pos[0] >= self.x and pos[0] <= self.x + self.width and pos[1] >= self.y and pos[1] <= self.y + self.height

    def show(self):
        if self.mouseIn():
            pygame.draw.rect(self.canvas, self.colour2, (self.x, self.y, self.width, self.height))
            self.canvas.blit(self.rendertext,(self.x + self.width/2 - self.textwidth/2, self.y + self.height/2 - self.textheight/2))
        else:
            pygame.draw.rect(self.canvas, self.colour, (self.x, self.y, self.width, self.height))
            self.canvas.blit(self.rendertext2,(self.x + self.width/2 - self.textwidth/2, self.y + self.height/2 - self.textheight/2))
        pygame.draw.rect(self.canvas, self.framecolour,(self.x, self.y, self.width, self.height), self.boldness)

    # returns true if leftClicked while mouse is within button
    def leftClicked(self):
        return pygame.mouse.get_pressed()[0] and self.mouseIn()
#The main loop below is for testing, disable when using this module.

"""
button1 = Button(250,250,100,20,GREEN,GREY,BLUE,TEXT = "TEST")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if button1.leftClicked():
        run = False
    screen.fill(BLACK)
    pygame.time.delay(40)
    button1.show()
    pygame.display.update()
"""