import pygame

pygame.init()

# class SnakePiece:
#     def __init__(self):
#         self.p_x = 20
#         self.p_y = 20
#     def Piece(self):


if __name__ == "main":

    dis_x, dis_y = 800, 800
    display = pygame.display.set_mode((dis_x, dis_y))
    #logo = pygame.image.load("")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")
    display.fill((0,255,255))




    # MainLoop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        rect = pygame.draw.rect(display,(255,0,0),(400,400),12)

        pygame.display.update()