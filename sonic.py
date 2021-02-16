background = ['ressources/background_fix.png', terrain1]
screen = create_graphics_screen()
for i in range(6):
    screen.blit(background[i], (i*10, 0))
playerpos = 3
screen.blit(playerimage, (playerpos*10, 0))