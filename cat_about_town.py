import pygame
pygame.init()

# WINDOW SETTINGS
win = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Cat About Town")

# IMAGE IMPORTS
walk_right = [
    pygame.image.load('assets/R1.png'), 
    pygame.image.load('assets/R2.png'), 
    pygame.image.load('assets/R3.png'), 
    pygame.image.load('assets/R4.png'), 
    pygame.image.load('assets/R5.png'), 
    pygame.image.load('assets/R6.png'), 
    pygame.image.load('assets/R7.png'), 
    pygame.image.load('assets/R8.png'), 
    pygame.image.load('assets/R9.png')
]
walk_left = [
    pygame.image.load('assets/L1.png'), 
    pygame.image.load('assets/L2.png'), 
    pygame.image.load('assets/L3.png'), 
    pygame.image.load('assets/L4.png'), 
    pygame.image.load('assets/L5.png'), 
    pygame.image.load('assets/L6.png'), 
    pygame.image.load('assets/L7.png'), 
    pygame.image.load('assets/L8.png'), 
    pygame.image.load('assets/L9.png')
]
idle = pygame.image.load('assets/Idle1.png')
# pygame.image.load('assets/Idle2.png')
jump_l = pygame.image.load('assets/JumpL.png')
jump_r = pygame.image.load('assets/JumpR.png')
bg = pygame.image.load('assets/bg.png')
atk_l = pygame.image.load('assets/AttackL.png')
atk_r = pygame.image.load('assets/AttackR.png')

# CLOCK/FPS
clock = pygame.time.Clock()

# GEN. VARIABLES
x = 50
y = 525
width = 64
height = 64
vel = 5

# PLAY VARIABLES
left = False
right = False
walk_count = 0

is_jumping = False
jump_count = 10

# DRAW FUNCTION
def redraw_game_window():
    global walk_count
    win.blit(bg, (0, 0))

    if walk_count + 1 >= 27:
        walk_count = 0
    
    if left:
        win.blit(walk_left[walk_count//3], (x, y))
        walk_count += 1
    elif right:
        win.blit(walk_right[walk_count//3], (x, y))
        walk_count += 1
    else:
        win.blit(idle, (x, y))
        walk_count = 0

    pygame.display.update()

# MAIN LOOP
running = True

while running:
    # pygame.time.delay(35)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 1200 - (width + vel):
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walk_count = 0

    if not(is_jumping):
        if keys[pygame.K_SPACE]:
            is_jumping = True
            right = False
            left = False
            walk_count = 0
    else:
        if jump_count >= -10:
            y -= (jump_count * abs(jump_count)) * 0.5
            jump_count -= 1
            # neg = 1
            # if jump_count < 0:
            #     neg = -1
            # y -= (jump_count ** 2) * 0.5 * neg
            # jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    redraw_game_window()

pygame.quit()