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

# OBJECT CLASSES
class Player(object):
    def __init__(self, x, y, width, height):
        # GEN. VARIABLES
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # PLAY VARIABLES
        self.vel = 5
        self.left = False
        self.right = False
        self.walk_count = 0
        self.is_jumping = False
        self.jump_count = 10
        self.standing = False
        self.idle = True

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        
        if self.idle:
            win.blit(idle, (self.x, self.y))
        else:
            if not self.standing:
                if self.left:
                    if not self.is_jumping:
                        self.vel = 5
                        win.blit(walk_left[self.walk_count//3], (self.x, self.y))
                        self.walk_count += 1
                    elif self.is_jumping:
                        self.vel = 10
                        win.blit(jump_l, (self.x, self.y))
                        self.walk_count += 1
                elif self.right:
                    if not self.is_jumping:
                        self.vel = 5
                        win.blit(walk_right[self.walk_count//3], (self.x, self.y))
                        self.walk_count += 1
                    elif self.is_jumping:
                        self.vel = 10
                        win.blit(jump_r, (self.x, self.y))
                        self.walk_count += 1
            else:
                if self.right:
                    win.blit(walk_right[5], (self.x, self.y))
                else:
                    win.blit(walk_left[5], (self.x, self.y))

class Attack(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


# GEN. VARIABLES
# x = 50
# y = 525
# width = 64
# height = 64
# vel = 5

# PLAY VARIABLES
# left = False
# right = False
# walk_count = 0

# is_jumping = False
# jump_count = 10

# DRAW FUNCTION
def redraw_game_window():
    win.blit(bg, (0, 0))
    george.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# MAIN LOOP
george = Player(50, 525, 64, 64)
bullets = []
running = True

while running:
    # pygame.time.delay(35)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.x < george.x + 74 and bullet.x > george.x - 16:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if george.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 10:
            bullets.append(
                Attack(
                    round(george.x + george.width //2), 
                    round(george.y + george.height //2), 
                    6, 
                    (0, 0, 0), 
                    facing
                )
            )

    if keys[pygame.K_LEFT] and george.x > george.vel:
        george.x -= george.vel
        george.left = True
        george.right = False
        george.standing = False
        george.idle = False
    elif keys[pygame.K_RIGHT] and george.x < 1200 - (george.width + george.vel):
        george.x += george.vel
        george.left = False
        george.right = True
        george.standing = False
        george.idle = False
    else:
        george.walk_count = 0
        george.standing = True

    if not(george.is_jumping):
        if keys[pygame.K_UP]:
            george.is_jumping = True
            # right = False
            # left = False
            george.walk_count = 0
            george.idle = False
    else:
        if george.jump_count >= -10:
            george.y -= (george.jump_count * abs(george.jump_count)) * 0.5
            george.jump_count -= 1
            george.standing = False
            # neg = 1
            # if jump_count < 0:
            #     neg = -1
            # y -= (jump_count ** 2) * 0.5 * neg
            # jump_count -= 1
        else:
            george.is_jumping = False
            george.jump_count = 10

    redraw_game_window()

pygame.quit()