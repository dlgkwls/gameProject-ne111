import pygame, sys, random

pygame.init()

# CREATING CANVAS
canvas = pygame.display.set_mode((500, 500))

# TITLE OF CANVAS
pygame.display.set_caption("My Board")
exit = False


    


class GameState():
    def __init__(self):
        self.state = 'main_game'

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  


        screen.blit(background,(0,0))
        screen.blit(ready_text,(Screen_width/2 - 115, scrren_height/2 - 33))
        player_group.draw(Screen)
        player_group.update()
 

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                sys.exit()
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if mouse clicked .?

        
        pygame.display.flip()
        


pygame.display.update()