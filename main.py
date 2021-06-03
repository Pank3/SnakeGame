import pygame
from random import randrange

pygame.init()

def Score(sc):
    font = pygame.font.Font("freesansbold.ttf",14)
    sceen = font.render("Score : "+str(sc),True,(0,0,250))
    display.blit(sceen,(5,5))

class SnakePart:
    def __init__(self,x,y):
        self.s_l = 19
        self.s_w = 19
        self.x = x
        self.y = y

    def draw(self):
        self.sn = pygame.draw.rect(display,(0,0,0),[self.x,self.y,self.s_l,self.s_w])




class Enemy:
    def __init__(self):
        self.x = randrange(60,580,20)
        self.y = randrange(20,580,20)
    def draw(self):
        self.en = pygame.draw.rect(display,(255,0,0),[self.x,self.y,19,19])
class MoveSnake:
    def __init__(self):
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.pieces = [SnakePart(60,0),SnakePart(40,0),SnakePart(20,0)]

    def addPiece(self):
        lx,ly = self.pieces[-1].x,self.pieces[-1].y
        self.pieces.append(SnakePart(lx,ly))
    def Keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and not self.right:
            self.left = True
            self.right = False
            self.up = False
            self.down = False
        if keys[pygame.K_RIGHT] and not self.left:
            self.left = False
            self.right = True
            self.up = False
            self.down = False
        if keys[pygame.K_UP] and not self.down:
            self.left = False
            self.right = False
            self.up = True
            self.down = False
        if keys[pygame.K_DOWN] and not self.up:
            self.left = False
            self.right = False
            self.up = False
            self.down = True
    def Movement(self):
        fx,fy = self.pieces[0].x,self.pieces[0].y
        lst = self.pieces.pop()
        lst.x,lst.y = fx,fy
        if self.left:
            lst.x-=20
        if self.right:
            lst.x+=20
        if self.up:
            lst.y-=20
        if self.down:
            lst.y+=20
        self.pieces.insert(0,lst)
        for piece in self.pieces:
            piece.draw()

    def eat(self,en_obj):
        fx = self.pieces[0].x
        fy = self.pieces[0].y
        if (fx == en_obj.x and fx+20 == en_obj.x+20) and  (fy == en_obj.y and fy+20 == en_obj.y+20):
            return True
        return False

    def CheckOver(self):
        fx,fy = self.pieces[0].x,self.pieces[0].y
        if fx<0 or fx>600 or fy<0 or fy>600:
            return True
        for piece in self.pieces[1:]:
            if piece.x == fx and piece.x+20 == fx+20 and piece.y == fy and piece.y+20 ==fy+20:
                return True
        return False
    def PrintOver(self):
        font = pygame.font.Font("freesansbold.ttf",48)
        over_screen = font.render("GAME OVER",True,(0,0,0))
        return over_screen


dis_x, dis_y = 600,600
display = pygame.display.set_mode((dis_x, dis_y))
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Snake")

##Piece
piece = SnakePart(0,0)
snake = MoveSnake()
#Enemy
en_obj = Enemy()

#Score
score = 0

# MainLoop
run = True
game = True
while run:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if game:
        display.fill((150,150,170))
        en_obj.draw()

        eat = snake.eat(en_obj)
        Score(score)

        #piece.draw()
        snake.Keys()
        snake.Movement()
        if eat:
            en_obj = Enemy()
            snake.addPiece()
            score+=5
        if snake.CheckOver():
            game = False

    else:
        over = snake.PrintOver()
        display.blit(over,(150,230))
    pygame.display.update()