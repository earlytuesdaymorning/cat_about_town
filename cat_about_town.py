import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Cat About Town")

x = 50
y = 425
width = 40
height = 60
vel = 5

is_jumping = False
jump_count = 10

running = True
while running:
    pygame.time.delay(35)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    if not(is_jumping):
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            is_jumping = True
            
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
            
        else:
            is_jumping = False
            jump_count = 10





    win.fill((0, 0, 0))
    pygame.draw.rect(win, (235, 23, 106), (x, y, width, height))
    pygame.display.update()


pygame.quit()