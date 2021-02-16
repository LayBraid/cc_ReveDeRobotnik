import sys
import pygame

def main():
    global event
    pygame.init()
    clock = pygame.time.Clock()

    size = 1200, 600

    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Le Rêve de Robotnik')

    background = pygame.image.load('resources/background_fix.png')
    bg_front = pygame.image.load('resources/background_front.png')
    bg_middle = pygame.image.load('resources/background_middle.png')

    bg_position_x = 0
    bg_position_y = 0
    bg_middle_position_x = 0
    bg_middle_position_y = 0
    bg_front_position_x = 0
    bg_front_position_y = 0

    rect_x = 0
    rect_y = 0

    speed_mode = 0

    running = False
    boost = False

    speed = 0

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if not running:
                    speed_mode += 1
                    if speed_mode == 20:
                        rect_y = 175
                        running = True
                        speed = 3
                    else:
                        speed = 1
                rect_x += 175
                if rect_x >= 700:
                    rect_x = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                boost = True
            if event.key == pygame.K_RIGHT:
                speed = 0
                speed_mode = 0
                rect_y = 0
                running = False

        bg_position_x = checkPosition(bg_position_x, 0)
        bg_middle_position_x = checkPosition(bg_middle_position_x, (1*speed))
        bg_front_position_x = checkPosition(bg_front_position_x, (2*speed))

        parallaxe(screen, background, bg_position_x, bg_position_y)
        parallaxe(screen, background, -1200 + bg_position_x, bg_position_y)

        parallaxe(screen, bg_middle, -1200 + bg_middle_position_x, bg_middle_position_y)
        parallaxe(screen, bg_middle, bg_middle_position_x, bg_middle_position_y)

        if not running:
            rect = pygame.Rect(rect_x, rect_y, 175, 175)
            spriteImage = pygame.image.load("resources/sonic.png").subsurface(rect)
            screen.blit(spriteImage, (425, 425))
        else:
            if not boost:
                rect = pygame.Rect(rect_x, rect_y, 175, 175)
                spriteImage = pygame.image.load("resources/sonic.png").subsurface(rect)
                screen.blit(spriteImage, (350, 425))
            else:
                rect = pygame.Rect(rect_x, rect_y, 175, 175)
                spriteImage = pygame.image.load("resources/sonic.png").subsurface(rect)
                screen.blit(spriteImage, (350, 425))

        parallaxe(screen, bg_front, bg_front_position_x, bg_front_position_y)
        parallaxe(screen, bg_front, -1200 + bg_front_position_x, bg_front_position_y)

        pygame.display.flip()

        clock.tick(60)
    return

def checkPosition(position, speed):
    if position < 1200:
        return position + speed
    else:
        return 0

def parallaxe(window, image, position_x, bg_position_y):
    window.blit(image, (position_x, bg_position_y))

if __name__ == "__main__":
    main()
