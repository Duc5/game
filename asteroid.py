import pygame 
import os
import spritesheet
import random
WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
VEL = 5
pygame.display.set_caption("ISA GAME space")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

offsetX = 0
offsetY = 0

# get graphics
BACKGROUND = pygame.image.load(os.path.join('Assets','space_bg.png')) #get background
# BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH,HEIGHT))

PLAYERIMAGE = pygame.image.load(os.path.join('Assets','Spaceship_Asset.png'))
print(type(PLAYERIMAGE))
PLAYER_SIZE = (50,100)
PLAYERIMAGE = pygame.transform.scale(PLAYERIMAGE,(PLAYERIMAGE.get_width()*3,PLAYERIMAGE.get_height()*3))
activeSprites = pygame.sprite.Group()
wallsGroup = pygame.sprite.Group()
class sprite(pygame.sprite.Sprite): #class for every sprite
    def __init__(self,avatar,x,y,width,height,frameList):
        pygame.sprite.Sprite.__init__(self)
        self.image = avatar
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frameList = frameList
        activeSprites.add(self)

          
class wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width,height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        wallsGroup.add(self)
    def move(self):
         self.x - offsetX
         self.y - offsetY
sprite_sheet_image = pygame.image.load(os.path.join("Assets","Spaceship_Asset.png")).convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
background = sprite(BACKGROUND,0,0,BACKGROUND.get_size()[0],BACKGROUND.get_size()[1],[])
mainPlayerFrames = []
avatar = spritesheet.SpriteSheet(pygame.image.load(os.path.join('Assets','Spaceship_Asset.png')))
PLAYERIMAGE = avatar.get_image(1,64,64,2,BLACK)
mainPlayerFrames.append(PLAYERIMAGE)
PlayerSheetLeft = spritesheet.SpriteSheet(pygame.image.load(os.path.join('Assets','_side walk.png')))
PlayerSheetRight = spritesheet.SpriteSheet(pygame.image.load(os.path.join('Assets',"_side walk right.png")))
for i in range(4):
      spriteFrame = PlayerSheetLeft.get_image(i,64,64,2,BLACK)
      mainPlayerFrames.append(spriteFrame)
for i in range(4):
      spriteFrame = PlayerSheetRight.get_image(i,64,64,2,BLACK)
      mainPlayerFrames.append(spriteFrame)
mainPlayer = sprite(PLAYERIMAGE,WIDTH/2,HEIGHT/2,PLAYER_SIZE[0],PLAYER_SIZE[1],mainPlayerFrames) 


def main(): #Game loop
    scroll = 0
    global offsetX,offsetY
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        print(str(pygame.mouse.get_pos()),end="\r")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                      run = False
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed,mainPlayer)
        wallCollisionCheck(keys_pressed)
        scroll += 10
        display(scroll)
        if abs(scroll) >= background.image.get_height()/2:
              scroll = 0


def display(scroll):
        WIN.fill((255,255,255))
        # WIN.blit(BACKGROUND,(0,0))
        WIN.blit(background.image,(background.rect.x,background.rect.y-background.image.get_height()/2+scroll))
        # for sprites in activeSprites.sprites():
        #       if len(sprites.frameList) == 0:    
        #         WIN.blit(sprites.image,(sprites.rect.x-offsetX,sprites.rect.y-offsetY))
        #       elif sprites == mainPlayer:
        #         WIN.blit(sprites.frameList[random.randint(0,3)],(sprites.rect.x-offsetX,sprites.rect.y-offsetY))
        WIN.blit(mainPlayer.image,(mainPlayer.rect.x,mainPlayer.rect.y))    
        for walls in wallsGroup.sprites():
             WIN.blit(walls.image,(walls.rect.x-offsetX,walls.rect.y-offsetY))  

      
        pygame.display.update()

def wallCollisionCheck(keys_pressed):
        global offsetX,offsetY
        collide = pygame.sprite.spritecollideany(mainPlayer,wallsGroup)
        if collide:
                if keys_pressed[pygame.K_LEFT]:
                        mainPlayer.rect.x+=VEL
                        offsetX +=VEL
                        
                if keys_pressed[pygame.K_RIGHT]:
                        mainPlayer.rect.x-=VEL
                        offsetX -=VEL
                if keys_pressed[pygame.K_UP]:
                        mainPlayer.rect.y+=VEL
                        offsetY +=VEL
                if keys_pressed[pygame.K_DOWN]:
                        mainPlayer.rect.y-=VEL   
                        offsetY -=VEL  

                
def player_movement(keys_pressed,player):
    global offsetX,offsetY
    tick = pygame.time.get_ticks()
    if keys_pressed[pygame.K_LEFT]:
            player.rect.x-=VEL
    if keys_pressed[pygame.K_RIGHT]:
            player.rect.x+=VEL
    if keys_pressed[pygame.K_UP]:
            player.rect.y-=VEL
    if keys_pressed[pygame.K_DOWN]:
            player.rect.y+=VEL   



main()