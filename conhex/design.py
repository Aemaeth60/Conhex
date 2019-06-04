import pygame,math
from pygame.locals import *

colorBoard = (255,255,255)
colorNode = (0,0,0)
colorLine = (0,0,1)
sizeNode = 8
sizeLine = 1
blue = (0,0,255)

pos = [(10,10),(490,10),  #480/16 =30
        (70,40),(130,40),(190,40),(250,40),(310,40),(370,40),(430,40),
        (40,70),(460,70),
        (130,100),(190,100),(250,100),(310,100),(370,100),
        (40,130),(100,130),(400,130),(460,130),
        (190,160),(250,160),(310,160),
        (40,190),(100,190),(160,190),(340,190),(400,190),(460,190),
        (250,220),
        (40,250),(100,250),(160,250),(220,250),(250,250),(280,250),(340,250),(400,250),(460,250),
        (250,280),
        (40,310),(100,310),(160,310),(340,310),(400,310),(460,310),
        (190,340),(250,340),(310,340),
        (40,370),(100,370),(400,370),(460,370),
        (130,400),(190,400),(250,400),(310,400),(370,400),
        (40,430),(460,430),
        (70,460),(130,460),(190,460),(250,460),(310,460),(370,460),(430,460),
        (10,490),(490,490)] 

circles = []

screen = pygame.display.set_mode((750,500))

def main():
    pygame.init()
    pygame.display.set_caption("Cohnex")
    screen.fill(colorBoard)
    drawBoard()
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        pos = pygame.mouse.get_pos()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in circles:  #i[0] = x && i[1] = y
                    absx = abs(i[0]-pos[0])
                    absy = abs(i[1]-pos[1])
                    if absx < 12 and absy <12:
                        #pygame.draw.circle(screen,blue,(i[0],i[1]),sizeNode)
                        screen.fill(blue,i)
                print(pygame.mouse.get_pos())
                pygame.display.update()


def drawBoard():
    for i in range(len(pos)):
        circles.append(pygame.draw.circle(screen,colorNode,pos[i],sizeNode))
        

    #CARRE BASE
    pygame.draw.line(screen,colorLine,pos[0],pos[1],sizeLine)
    pygame.draw.line(screen,colorLine,pos[1],pos[68],sizeLine)
    pygame.draw.line(screen,colorLine,pos[0],pos[67],sizeLine)
    pygame.draw.line(screen,colorLine,pos[67],pos[68],sizeLine)

    #OUTSIDE HAUT
    pygame.draw.line(screen,colorLine,pos[2],(70,10),sizeLine);
    pygame.draw.line(screen,colorLine,pos[4],(190,10),sizeLine);
    pygame.draw.line(screen,colorLine,pos[6],(310,10),sizeLine);
    pygame.draw.line(screen,colorLine,pos[8],(430,10),sizeLine);
    pygame.draw.line(screen,colorLine,pos[2],pos[8],sizeLine);

    #OUTSIDE GAUCHE
    pygame.draw.line(screen,colorLine,pos[9],(10,70),sizeLine);
    pygame.draw.line(screen,colorLine,pos[23],(10,190),sizeLine);
    pygame.draw.line(screen,colorLine,pos[40],(10,310),sizeLine);
    pygame.draw.line(screen,colorLine,pos[58],(10,430),sizeLine);
    pygame.draw.line(screen,colorLine,pos[9],pos[58],sizeLine);

    #OUTSIDE BAS
    pygame.draw.line(screen,colorLine,pos[60],(70,490),sizeLine);
    pygame.draw.line(screen,colorLine,pos[62],(190,490),sizeLine);
    pygame.draw.line(screen,colorLine,pos[64],(310,490),sizeLine);
    pygame.draw.line(screen,colorLine,pos[66],(430,490),sizeLine);
    pygame.draw.line(screen,colorLine,pos[60],pos[66],sizeLine);

    #OUTSIDE DROITE
    pygame.draw.line(screen,colorLine,pos[10],(490,70),sizeLine);
    pygame.draw.line(screen,colorLine,pos[28],(490,190),sizeLine);
    pygame.draw.line(screen,colorLine,pos[45],(490,310),sizeLine);
    pygame.draw.line(screen,colorLine,pos[59],(490,430),sizeLine);
    pygame.draw.line(screen,colorLine,pos[10],pos[59],sizeLine);

    #OUTSIDE COIN
    pygame.draw.line(screen,colorLine,pos[2],pos[9],sizeLine);
    pygame.draw.line(screen,colorLine,pos[8],pos[10],sizeLine);
    pygame.draw.line(screen,colorLine,pos[58],pos[60],sizeLine);
    pygame.draw.line(screen,colorLine,pos[59],pos[66],sizeLine);
    
    #INSIDE 1 HAUT
    pygame.draw.line(screen,colorLine,pos[3],pos[11],sizeLine);
    pygame.draw.line(screen,colorLine,pos[5],pos[13],sizeLine);
    pygame.draw.line(screen,colorLine,pos[7],pos[15],sizeLine);
    pygame.draw.line(screen,colorLine,pos[11],pos[15],sizeLine);

    #INSIDE 1 GAUCHE
    pygame.draw.line(screen,colorLine,pos[16],pos[17],sizeLine);
    pygame.draw.line(screen,colorLine,pos[30],pos[31],sizeLine);
    pygame.draw.line(screen,colorLine,pos[49],pos[50],sizeLine);
    pygame.draw.line(screen,colorLine,pos[17],pos[50],sizeLine);

    #INSIDE 1 BAS
    pygame.draw.line(screen,colorLine,pos[53],pos[61],sizeLine);
    pygame.draw.line(screen,colorLine,pos[55],pos[63],sizeLine);
    pygame.draw.line(screen,colorLine,pos[57],pos[65],sizeLine);
    pygame.draw.line(screen,colorLine,pos[53],pos[57],sizeLine);
    
    #INSIDE 1 DROITE
    pygame.draw.line(screen,colorLine,pos[18],pos[19],sizeLine);
    pygame.draw.line(screen,colorLine,pos[37],pos[38],sizeLine);
    pygame.draw.line(screen,colorLine,pos[51],pos[52],sizeLine);
    pygame.draw.line(screen,colorLine,pos[18],pos[51],sizeLine);

    #INSIDE 1 COINS
    pygame.draw.line(screen,colorLine,pos[11],pos[17],sizeLine);
    pygame.draw.line(screen,colorLine,pos[15],pos[18],sizeLine);
    pygame.draw.line(screen,colorLine,pos[50],pos[53],sizeLine);
    pygame.draw.line(screen,colorLine,pos[51],pos[57],sizeLine);
        
    #INSIDE 2 HAUT
    pygame.draw.line(screen,colorLine,pos[12],pos[20],sizeLine);
    pygame.draw.line(screen,colorLine,pos[14],pos[22],sizeLine);
    pygame.draw.line(screen,colorLine,pos[20],pos[22],sizeLine);

    #INSIDE 2 GAUCHE
    pygame.draw.line(screen,colorLine,pos[24],pos[25],sizeLine);
    pygame.draw.line(screen,colorLine,pos[41],pos[42],sizeLine);
    pygame.draw.line(screen,colorLine,pos[25],pos[42],sizeLine);

    #INSIDE 2 BAS
    pygame.draw.line(screen,colorLine,pos[46],pos[54],sizeLine);
    pygame.draw.line(screen,colorLine,pos[48],pos[56],sizeLine);
    pygame.draw.line(screen,colorLine,pos[46],pos[48],sizeLine);

    #INSIDE 2 DROITE
    pygame.draw.line(screen,colorLine,pos[26],pos[27],sizeLine);
    pygame.draw.line(screen,colorLine,pos[43],pos[44],sizeLine);
    pygame.draw.line(screen,colorLine,pos[26],pos[43],sizeLine);

    #INSIDE 2 COINS
    pygame.draw.line(screen,colorLine,pos[20],pos[25],sizeLine);
    pygame.draw.line(screen,colorLine,pos[42],pos[46],sizeLine);
    pygame.draw.line(screen,colorLine,pos[43],pos[48],sizeLine);
    pygame.draw.line(screen,colorLine,pos[22],pos[26],sizeLine);

    #INSIDE 3 HAUT
    pygame.draw.line(screen,colorLine,pos[21],pos[29],sizeLine);

    #INSIDE 3 GAUCHE
    pygame.draw.line(screen,colorLine,pos[32],pos[33],sizeLine);
    
    #INSIDE 3 BAS
    pygame.draw.line(screen,colorLine,pos[39],pos[47],sizeLine);

    #INSIDE 3 DROITE
    pygame.draw.line(screen,colorLine,pos[35],pos[36],sizeLine);
    
    #INSIDE 3 COINS
    pygame.draw.line(screen,colorLine,pos[29],pos[33],sizeLine);
    pygame.draw.line(screen,colorLine,pos[33],pos[39],sizeLine);
    pygame.draw.line(screen,colorLine,pos[35],pos[39],sizeLine);
    pygame.draw.line(screen,colorLine,pos[29],pos[35],sizeLine);


   
    pygame.display.update();
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

    
