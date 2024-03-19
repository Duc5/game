import pygame 
import os
import spritesheet
import random
import asteroid
WIDTH,HEIGHT = 900,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
VEL = 5
pygame.display.set_caption("ISA GAME MAIN")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

offsetX = 0
offsetY = 0

# get graphics
BACKGROUND = pygame.image.load(os.path.join('Assets','game_bg.png')) #get background
BACKGROUND = pygame.transform.scale(BACKGROUND,(WIDTH*3,HEIGHT*3))

PLAYERIMAGE = pygame.image.load(os.path.join('Assets','char_walk_left.gif'))
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
    def changeFrame(self):
        tick = pygame.time.get_ticks()
        frameNumber = int(tick) % len(self.frameList)
        self.image = self.frameList[int(frameNumber)]

          
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

sprite_sheet_imageLeft = pygame.image.load(os.path.join("Assets","_side walk.png")).convert_alpha()
sprite_sheetLeft = spritesheet.SpriteSheet(sprite_sheet_imageLeft)
sprite_sheet_imageRight = pygame.image.load(os.path.join("Assets","_side walk right.png")).convert_alpha()
sprite_sheetRight = spritesheet.SpriteSheet(sprite_sheet_imageRight)
sprite_sheet_imageUp = pygame.image.load(os.path.join("Assets","_up walk.png")).convert_alpha()
sprite_sheetUp = spritesheet.SpriteSheet(sprite_sheet_imageUp)
sprite_sheet_imageDown = pygame.image.load(os.path.join("Assets","_down walk.png")).convert_alpha()
sprite_sheetDown = spritesheet.SpriteSheet(sprite_sheet_imageDown)


def createplayerFrames(sprite_sheet): 
        mainPlayerFrames = []
        for i in range(4):
                spriteFrame = sprite_sheet.get_image(i,64,64,2,BLACK)
                mainPlayerFrames.append(spriteFrame)
        return mainPlayerFrames



background = sprite(BACKGROUND,0,0,BACKGROUND.get_size()[0],BACKGROUND.get_size()[1],[])
avatar = spritesheet.SpriteSheet(pygame.image.load(os.path.join('Assets','_side idle.png')))
PLAYERIMAGE = avatar.get_image(1,64,64,2,BLACK)
PlayerSheetLeft = spritesheet.SpriteSheet(pygame.image.load(os.path.join('Assets','_side walk.png')))
PlayerSheetRight = spritesheet.SpriteSheet(pygame.image.load(os.path.join('Assets',"_side walk right.png")))
mainPlayer = sprite(PLAYERIMAGE,WIDTH/2,HEIGHT/2,PLAYER_SIZE[0],PLAYER_SIZE[1],[PLAYERIMAGE]) 

def main(): #Game loop
    global offsetX,offsetY
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        print(str(pygame.mouse.get_pos()),end="\r")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                      run = False
                      pygame.quit()
                if event.key == pygame.K_BACKSLASH:
                      asteroid.main()
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed,mainPlayer)
        wallCollisionCheck(keys_pressed)
        count = 0
        display(count)

        

def display(count):
        WIN.fill((255,255,255))
        # WIN.blit(BACKGROUND,(0,0))
        for sprites in activeSprites.sprites():
        #       if len(sprites.frameList) == 0:    
        #         WIN.blit(sprites.image,(sprites.rect.x-offsetX,sprites.rect.y-offsetY))
        #       elif sprites == mainPlayer:
        #         WIN.blit(sprites.frameList[random.randint(0,3)],(sprites.rect.x-offsetX,sprites.rect.y-offsetY))
                WIN.blit(sprites.image,(sprites.rect.x-offsetX,sprites.rect.y-offsetY))    
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
            offsetX -=VEL
            frame = createplayerFrames(sprite_sheetLeft)
            mainPlayer.frameList = frame
            mainPlayer.changeFrame()
    if keys_pressed[pygame.K_RIGHT]:
            player.rect.x+=VEL
            offsetX +=VEL
            frame = createplayerFrames(sprite_sheetRight)
            mainPlayer.frameList = frame
            mainPlayer.changeFrame()
    if keys_pressed[pygame.K_UP]:
            player.rect.y-=VEL
            offsetY -=VEL
            frame = createplayerFrames(sprite_sheetUp)
            mainPlayer.frameList = frame
            mainPlayer.changeFrame()
    if keys_pressed[pygame.K_DOWN]:
            player.rect.y+=VEL   
            offsetY +=VEL  
            frame = createplayerFrames(sprite_sheetDown)
            mainPlayer.frameList = frame
            mainPlayer.changeFrame()


main()

          