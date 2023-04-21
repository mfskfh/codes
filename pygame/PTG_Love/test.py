#-*- 

import pygame


pygame.init()
pygame.font.init()
pygame.mixer.init()

game_font_L = pygame.font.Font("pygame/PTG_Love/source/font/MP_B.ttf", 25)
game_font_B = pygame.font.Font("pygame/PTG_Love/source/font/MP_L.ttf", 25)

Sound_key = pygame.mixer.Sound("pygame/PTG_Love/source/sound/Tennis Hit.wav")

print("민재바보")

def gameText(words, xPos, yPos):
    text = game_font_B.render("", True, (80, 180, 80))

    text_width = text.get_rect().size[0]
    text_height = text.get_rect().size[1]

    for textNo in range(len(words)+1):
        text = game_font_B.render(words[0:textNo], True, (80, 180, 80))
        screen.blit(text, (xPos, yPos))
        pygame.display.update()
        Sound_key.play()
        pygame.time.delay(100)
    

    

class imageload:
    def __init__(self):
        self.x = 0
        self.y = 0
    def put_img(self, address):
        self.img = pygame.image.load(address)
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))
    def get_rect(self):
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y

screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#배경
start_bg = imageload()
start_bg.put_img("pygame/PTG_Love/source/image/start_bg.png")

corridor_bg = imageload()
corridor_bg.put_img("pygame/PTG_Love/source/image/bg.png")

market_bg = imageload()
market_bg.put_img("pygame/PTG_Love/source/image/start_bg.png")

class_bg = imageload()
class_bg.put_img("pygame/PTG_Love/source/image/start_bg.png")

#UI
start_button = imageload()
start_button.put_img("pygame/PTG_Love/source/image/button.png")
start_button.change_size(400, 200)
start_button.x = (screen_width / 2) - (start_button.img.get_size()[0] / 2)
start_button.y = 7
start_button.get_rect()

# gameText("태건 : 난 햄버거 먹어야겠다 넌 뭐먹을래?",0,0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pygame.display.update()

pygame.quit()

