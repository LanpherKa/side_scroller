import pygame
import random
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Side Scroller Game")
font = pygame.font.Font(None, 50)
text_surface = font.render("0", True, "white")
text_rect = text_surface.get_rect(center=(250, 150))
text_surface2 = font.render("0", True, "white")
text_rect2 = text_surface2.get_rect(center=(500, 450))


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
    gravity = .5
    jumpcount = 0
    jump = 0
    addend1 = random.randint(5, 10)
    addend2 = random.randint(0, 5)
    target = pygame.image.load(numbers[addend2])
    target = pygame.transform.rotozoom(target, 0, 0.5)
    target_x = 500
    score = 0
    correct_sound = pygame.mixer.Sound("assets/correct_sound1.wav")
    wrong_sound = pygame.mixer.Sound("assets/wrong.wav")

    while True:
        screen.blit(image,(bgx-640,0))
        screen.blit(image, (bgx, 0))
        screen.blit(image, (bgx+640, 0))
        text_surface = font.render( str(addend1) + " + ? = 10", True, "white")
        screen.blit(text_surface, text_rect)

        text_surface2 = font.render( "Score: " + str(score), True, "white")
        screen.blit(text_surface2, text_rect2)

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

        screen.blit(target, (target_x, 375))
        if target_x < 0:
            target_x = 600
            addend2 = random.randint(0, 5)
            target = pygame.image.load(numbers[addend2])
            target = pygame.transform.rotozoom(target, 0, 0.5)
        else:
            target_x -= 0.5

        if target_x > 30 and target_x < 80:
            if player_y > 250:
                if (addend1 + addend2 ) == 10:
                    #print("correct " + str(addend1) + " + " + str(addend2))
                    target_x = 600
                    addend2 = random.randint(0, 5)
                    target = pygame.image.load(numbers[addend2])
                    target = pygame.transform.rotozoom(target, 0, 0.5)
                    addend1 = random.randint(5, 10)
                    score = score + 1
                    pygame.mixer.Sound.play(correct_sound)
                    pygame.mixer.music.stop()
                    #text_surface = font.render( str(addend1) + " + ? = 10", True, "white")
                else:
                    score = score -1 
                    target_x = 600
                    pygame.mixer.Sound.play(wrong_sound)
                    pygame.mixer.music.stop()
                    

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                jump = 1

menu()