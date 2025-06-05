import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Side Scroller Game")
font = pygame.font.Font(None, 50)
text_surface = font.render("0", True, "white")
text_rect = text_surface.get_rect(center=(275, 150))


#the menu starts the game 
def menu():
    image = pygame.image.load('assets\menu.png')
    image = pygame.transform.scale(image, (640, 480))
    while True:
        screen.blit(image,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(275, 400) and event.pos[1] in range(225, 350):
                    game()

#game function called by menu
def game():
    numbers = ['assets/zero.png', 'assets/one.png', 'assets/two.png', 'assets/three.png', 'assets/four.png', 'assets/five.png']
    image = pygame.image.load('assets\\background.png')
    image = pygame.transform.scale(image, (640, 480))
    bgx = 0
    player = pygame.image.load('assets/characterR.png')
    player = pygame.transform.rotozoom(player, 0, 0.7)
    player_y = 300
    gravity = .75
    jumpcount = 0
    jump = 0
    addend1 = random.randint(0, 10)
   
    while True:
        screen.blit(image,(bgx-640,0))
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))
        text_surface = font.render("Target: " + str(addend1), True, "white")
        screen.blit(text_surface, text_rect)

        bgx = bgx - 0.25
        if bgx <= -640:
            bgx = 0

        screen.blit(player, (50, player_y))
        if player_y < 300:
            player_y += gravity
        if jump == 1:
            player_y -= 4.5
            jumpcount += 1
            if jumpcount > 50:
                jumpcount = 0
                jump = 0


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                jump = 1

menu()