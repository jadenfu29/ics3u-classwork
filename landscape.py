# pygame template

import pygame


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables


zombie_x = 300
zombie_y = 270 
flip = 1
pumpkin_x = 400
pumpkin_y = 150

# ---------------------------
offset = 0
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((23,1,31))
    pygame.draw.circle(screen,(244, 245, 169),(100,200),50)
    pygame.draw.circle(screen,(23,1,31),(150,175),75)
    rect = pygame.Rect(0,WIDTH-240,1000,1000)
    pygame.draw.rect(screen,(148, 148, 141),rect)

    

    for sidewalkbar in range(-150,640,150):
        pygame.draw.line(screen,(48, 48, 45),(sidewalkbar+offset,WIDTH-230),(sidewalkbar+200+offset,WIDTH),5)

    offset-=5
    offset%=150
    if offset == 145:
        flip *=-1

    px = pumpkin_x
    py = pumpkin_y
    if flip==1:
        pumpkin_y+=offset
    else:
        pumpkin_y+=150-offset

    #houses

    for i in range(-160,640,160):
        pygame.draw.rect(screen,(89, 66, 13),(i+offset,WIDTH-240-100,150,100))
        pygame.draw.rect(screen,(48, 39, 16),(i+offset+75,WIDTH-240-100+50,40,50))
        pygame.draw.polygon(screen,(82, 66, 25),[(i+offset-15,WIDTH-240-100),(i+offset+15+150,WIDTH-240-100),(i+offset+75,WIDTH-240-100-50)])


    #pumpkinpart


    pygame.draw.line(screen,(96, 168, 112),(zombie_x+25,zombie_y+25),(pumpkin_x+25,pumpkin_y+30),20)
    pygame.draw.line(screen,(23, 69, 29),(pumpkin_x+25,pumpkin_y+30),(pumpkin_x+25,pumpkin_y-10),10)
    pygame.draw.ellipse(screen,(252, 136, 3),(pumpkin_x-25,pumpkin_y+25/2,50,75))
    pygame.draw.ellipse(screen,(122, 78, 28),(pumpkin_x-25,pumpkin_y+25/2,50,75),5)
    pygame.draw.ellipse(screen,(252, 136, 3),(pumpkin_x+25,pumpkin_y+25/2,50,75))
    pygame.draw.ellipse(screen,(122, 78, 28),(pumpkin_x+25,pumpkin_y+25/2,50,75),5)
    pygame.draw.ellipse(screen,(252, 136, 3),(pumpkin_x,pumpkin_y,50,100))
    pygame.draw.ellipse(screen,(122, 78, 28),(pumpkin_x,pumpkin_y,50,100),5)
    pygame.draw.circle(screen,(0,0,0),(pumpkin_x+1,pumpkin_y+35),10)
    pygame.draw.circle(screen,(0,0,0),(pumpkin_x+40,pumpkin_y+35),10)
    pygame.draw.ellipse(screen,(0,0,0),(pumpkin_x+10,pumpkin_y+60,35,10))
    pumpkin_x = px
    pumpkin_y = py
    

    #zombiepart

    pygame.draw.line(screen,(71, 43, 171),(zombie_x,zombie_y+90),(zombie_x+offset-75,zombie_y+190),30)
    pygame.draw.line(screen,(71, 43, 171),(zombie_x,zombie_y+90),(zombie_x-(offset-75),zombie_y+190),30)
    
    pygame.draw.rect(screen,(67, 183, 191),(zombie_x-25,zombie_y+10,50,100))

    if flip ==1:
        pygame.draw.circle(screen,(121, 196, 98),(zombie_x,zombie_y+offset/10),25)
    else:
        pygame.draw.circle(screen,(121, 196, 98),(zombie_x,zombie_y+15-offset/10),25)




    




    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()