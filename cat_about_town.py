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
        self.hitbox = (self.x, self.y, 28, 60)
        # ^ this is init, not how hitbox will be drawn

    def draw(self, win):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        # reset once it becomes the number of images times 3... to be able to cycle them below
        
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
        self.hitbox = (self.x + 10, self.y + 15, 50, 40)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

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

class Enemy(object):
    fly_right = [
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
    fly_left = [
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

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)
        # ^ this is init, not how hitbox will be drawn
    
    def draw(self, win):
        self.move()
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        
        if self.vel > 0:
            win.blit(self.fly_right[self.walk_count //3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(self.fly_left[self.walk_count //3], (self.x, self.y))
            self.walk_count += 1
        
        self.hitbox = (self.x + 20, self.y + 20, 30, 30)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0

    def hit(self):
        print('hit')
        pass

# DRAW FUNCTION
def redraw_game_window():
    win.blit(bg, (0, 0))
    george.draw(win)
    bird.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

# MAIN LOOP
george = Player(50, 525, 64, 64)
bird = Enemy(200, 385, 64, 64, 1000)
atk_loop = 0 # our attack cool down
bullets = []
running = True

while running:
    # pygame.time.delay(35)
    clock.tick(27)

    if atk_loop > 0:
        atk_loop += 1
    if atk_loop > 3:
        atk_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if bullet.y - bullet.radius < bird.hitbox[1] + bird.hitbox[3] and bullet.y + bullet.radius > bird.hitbox[1]:
            if bullet.x + bullet.radius > bird.hitbox[0] and bullet.x - bullet.radius < bird.hitbox[0] + bird.hitbox[2]:
                bird.hit
                bullets.pop(bullets.index(bullet))

        if bullet.x < george.x + 74 and bullet.x > george.x - 16:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and atk_loop == 0:
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
        atk_loop = 1

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