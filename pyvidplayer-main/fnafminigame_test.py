# pygame template

import pygame
import random
import time
from pygame import mixer
from pyvidplayer import Video
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_SPACE

def fnafgame():
    pygame.init()
    pygame.font.init()

    WIDTH = 960
    HEIGHT = 351
    SIZE = (WIDTH, HEIGHT)

    VIDEO_W = 718
    VIDEO_H = 365

    screen = pygame.display.set_mode(SIZE)

    #Instantiate mixer
    mixer.init()
    
    clock = pygame.time.Clock()

    # ---------------------------
    # Initialize global variables
    text_size = 20
    text_colour = [225, 225, 160]

    pygame.display.set_caption("FNAF CHRISTMAS MINIGAME")
 
    text_font = pygame.font.Font("assets/fnaftextfont.ttf", text_size)

    # video commands
    bite_83 = Video("assets/bite_of_83.mp4")
    bite_83.set_size((VIDEO_W, VIDEO_H))

    bite_83_audio = mixer.music.load('assets/bite_of_83.mp3')

    # variables
    bg_img1 = pygame.image.load('assets/fnafpartyslide1.png')
    bg_img1 = pygame.transform.scale(bg_img1, (WIDTH, HEIGHT))

    bg_img2 = pygame.image.load('assets/fnafpartyslide2.png')
    bg_img2 = pygame.transform.scale(bg_img2, (WIDTH, HEIGHT))

    afton_img = pygame.image.load("assets/william_afton.png")
    afton_img = pygame.transform.scale(afton_img, (130, 230))
    afton_rect = pygame.Rect(750, 120, afton_img.get_width(), afton_img.get_height())

    decor_box_image = pygame.image.load("assets/Cardboard_boxes.webp")
    decor_box_image = pygame.transform.scale(decor_box_image, (150, 150))
    decor_box_rect = pygame.Rect(-10, 140, decor_box_image.get_width(), decor_box_image.get_height())

    garlands = pygame.image.load("assets/garlands.png")
    garlands = pygame.transform.scale(garlands, (480, 50))

    santa_hat = pygame.image.load("assets/santa_hat.png")
    santa_hat = pygame.transform.scale(santa_hat, (100, 70))

    cake_image = pygame.image.load("assets/fazbearcake.png")
    cake_image = pygame.transform.scale(cake_image, (150, 150))
    cake_image_rect = pygame.Rect(700, 110, cake_image.get_width(), cake_image.get_height())

    children_side1 = pygame.image.load("assets/child1_fnaf.png")
    children_side1 = pygame.transform.scale(children_side1, (230, 290))

    children_side2 = pygame.image.load("assets/child_2fnaf.png")
    children_side2 = pygame.transform.scale(children_side2, (230, 290))

    cryingchild = pygame.image.load("assets/evanafton.png")
    cryingchild = pygame.transform.scale(cryingchild, (120, 180))

    souls = pygame.image.load("assets/missing_children.png")
    souls = pygame.transform.scale(souls, (50, 50))

    full_list = "Welcome to Fredbear's Family Diner! , The Diner is preparing to celebrate Christmas! , Let's help William with the decorations. , Click the little box to set up the ceiling decor , Good job! Now click the cake to give it to the children , The children seem to enjoy the cake every much. , What's over here? , Evan? ,  Merry Christmas!"
    # goes up to 11
  

    # ---------------------------
    
    phrase = full_list.split(" , ")

    def children():
        list = []
        for i in range(4):
            x = random.randrange(0, 850)
            list.append(x)

        return list

    def video():
        mixer.music.play()
        counter = 0
        video_screen = pygame.display.set_mode((VIDEO_W, VIDEO_H))
        while True:
            bite_83.draw(video_screen, (0, 0))
            pygame.display.update()
            counter += 1
            print(counter)
            if counter == 260:
                break



    act = 1
    scene = 1
    i = 0
   

    running = True
    while running:
        # EVENT HANDLING
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    i += 1


            elif event.type == QUIT:
                running = False
        
        screen.fill((0,0,0))
        
        

        if act == 1:
            mixer.music.pause()
            screen.blit(bg_img1, (0,0))

            screen.blit(afton_img, (750, 120))

            if scene == 1:
                text = text_font.render(phrase[i], False, (text_colour))
                screen.blit(text, (20, 300))

                screen.blit(decor_box_image, decor_box_rect.topleft)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos  # gets mouse position
                        # checks if mouse position is over the button

                        if decor_box_rect.collidepoint(mouse_pos):
                            scene += 1
            elif scene == 2:
                text = text_font.render(phrase[i], False, (text_colour))
                screen.blit(text, (20, 300))

                screen.blit(afton_img, (750, 120))

                screen.blit(garlands, (0, -10))

                screen.blit(garlands, (480, -10))

                screen.blit(santa_hat, (350 , 20))

                screen.blit(cake_image, (cake_image_rect.topleft))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos  # gets mouse position
                        # checks if mouse position is over the button

                        if cake_image_rect.collidepoint(mouse_pos):
                            act = 2
                            
            
        elif act == 2:
            screen.blit(bg_img1, (0,0))

            screen.blit(afton_img, (750, 120))

            text = text_font.render(phrase[5], False, (text_colour))
            cake_text = text_font.render("Click Afton to shoo away the children." , False, (text_colour))
            screen.blit(text, (20, 300))
            screen.blit(cake_text, (30, 30))

            screen.blit(cake_image, (60, 135))

            screen.blit(cake_image, (575, 135))

            screen.blit(afton_img, afton_rect.topleft)

            for repeat in range(2):
                screen.blit(children_side1, (children()[1], 200))
                screen.blit(children_side2, (children()[2], 200))
                time.sleep(0.3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    # checks if mouse position is over the button

                    if afton_rect.collidepoint(mouse_pos):
                        act = 3
        
        elif act == 3:
            screen.blit(bg_img1, (0,0))

            screen.blit(afton_img, (750, 120))

            screen.blit(garlands, (0, -10))

            screen.blit(garlands, (480, -10))

            screen.blit(santa_hat, (350 , 20))

            text = text_font.render(phrase[i+1], False, (text_colour))
            screen.blit(text, (20, 300))

            if i == 6:
                act = 4
        if act == 4:
            text_colour[2] = 87
            screen.blit(bg_img2, (0,0))

            text = text_font.render(phrase[i], False, (text_colour))
            screen.blit(text, (20, 300))

            screen.blit(cryingchild, (700, 200))

            if i != 6 and i != 7:
                act = 5

        if act == 5:
            video()
            mixer.music.stop()
            act += 1
        
        if act == 6:
            for children in range(15): 
                x = random.randrange(0, 850)
                y = 200
                if children % 2 == 0:
                    screen.blit(souls, (x, y))
                else:
                    screen.blit(souls, (x, y))
            act += 1

        if act == 7:
            text_colour[2] = 87
            accident = text_font.render("Uh oh.", False, (text_colour))
            screen.blit(accident, (300, 100))


        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)
        #---------------------------
    
if __name__ == "__main__":
    fnafgame() 


pygame.quit()