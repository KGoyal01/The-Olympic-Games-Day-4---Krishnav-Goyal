import pygame
import time
import math
from decimal import *

from pygame.locals import *
pygame.init()

size = 370,600
width,height = size
canvas = pygame.display.set_mode(size)
pygame.display.set_caption('Calculator')
black = (0,0,0)
yellow = (255, 255, 0)
gray = (181, 181, 181)
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)
orange = (255,165,0)

canvas.fill(black)



def clearscreen():
    canvas.fill(black)
    for i in range(1,6):
        circlexy = (i*(width//5.2)-25, 3*(height//8)+40)
        circleRadius = 33
        borderWidth = 0 
        pygame.draw.circle(canvas, orange, circlexy, circleRadius, borderWidth)


    for x in range(0,3):
        for i in range(0,3):
            font = pygame.font.Font('freesansbold.ttf', 40)
            text = font.render(str((i+1)+((3*x))), True, white)
            textRect = text.get_rect()
            textRect.center = ((2*i+1)*(width//6), ((x+4)*(height // 8))+40)
            canvas.blit(text,textRect)

    text = font.render(str(0), True, white)
    textRect = text.get_rect()
    textRect.center = (3*(width//6), (7*(height // 8))+40)
    canvas.blit(text,textRect)
    pygame.display.update()

    pygame.draw.line(canvas, white, (15,height//2+10), (width-15,height//2+10), 3)


    pygame.draw.line(canvas, white, (15,(5*(height//8))+10), (width-15,(5*(height//8))+10), 3)


    pygame.draw.line(canvas, white, (15,(6*(height//8))+10), (width-15,(6*(height//8))+10), 3)


    pygame.draw.line(canvas, white, (15,(7*(height//8))+10), (width-15,(7*(height//8))+10), 3)


    pygame.draw.line(canvas, white, (width//3,height//2+10), (width//3, height), 3)
    pygame.display.update()

    pygame.draw.line(canvas, white, (2*(width//3),height//2+10), (2*(width//3), height), 3)


    rectg1 = (width//7 - 45, 2*(height//8)+20, 80,50)
    pygame.draw.rect(canvas, gray, rectg1, 0, 5)


    rectg2 = ((2*(width//7)-7), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg2,  0, 5)


    rectg3 = ((3*(width//7)-15), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg3,  0, 5)




    rectg4 = ((4*(width//7)-22), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg4,  0, 5)
    

    rectg5 = ((5*(width//7)-27), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg5,  0, 5)


    rectg6 = ((5*(width//7)+18), 2*(height//8)+20,80,50)
    pygame.draw.rect(canvas, gray, rectg6,  0, 5)

    pygame.draw.rect(canvas, orange, pygame.Rect((5*(width//7)+18), 7*(height//8)+20,80,50),  0, 5)





    pygame.display.update()

    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render('Ans    .    (     )    π   Del', True, black)
    textRect = text.get_rect()
    textRect.center = (width//2, 2*(height//8)+45)
    textRect.right = width-30
    canvas.blit(text,textRect)
    pygame.display.update()





    font = pygame.font.Font('freesansbold.ttf', 50)
    textplus = font.render('+', True, black)
    textRectplus = textplus.get_rect()
    textRectplus.center = (1*(width//10)+10, 3*(height//8)+38)
    canvas.blit(textplus,textRectplus)
    pygame.display.update()
    

    text = font.render('-', True, black)
    textRect = text.get_rect()
    textRect.center = (3*(width//10)+6, 3*(height//8)+38)
    canvas.blit(text,textRect)
    pygame.display.update()



    text = font.render('x', True, black)
    textRect = text.get_rect()
    textRect.center = (5*(width//10)+3, 3*(height//8)+38)
    canvas.blit(text,textRect)
    pygame.display.update()



    text = font.render('÷', True, black)
    textRect = text.get_rect()
    textRect.center = (7*(width//10), 3*(height//8)+38)
    canvas.blit(text,textRect)
    pygame.display.update()

    text = font.render('=', True, black)
    textRect = text.get_rect()
    textRect.center = (6*(width//7)+5, 7*(height//8)+45)
    canvas.blit(text,textRect)
    pygame.display.update()


    font = pygame.font.Font('freesansbold.ttf', 20)

    text = font.render('More', True, black)
    textRect = text.get_rect()
    textRect.center = (9*(width//10)-2, 3*(height//8)+43)
    canvas.blit(text,textRect)
    pygame.display.update()

    




clearscreen()
coordinatelst = []
keypresslst = []
keypress2lst = []
operationslst = []
prevnumend = 0
equals = False
count = -1
count1 = -1
running = True
operator = False
num1 = ''
num2 = ''
ans = 0
anslst = []


while running:

    rectg1 = (width//7 - 45, 2*(height//8)+20, 80,50)
    pygame.draw.rect(canvas, gray, rectg1, 0, 5)


    rectg2 = ((2*(width//7)-7), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg2,  0, 5)


    rectg3 = ((3*(width//7)-15), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg3,  0, 5)


    rectg4 = ((4*(width//7)-22), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg4,  0, 5)
    

    rectg5 = ((5*(width//7)-27), 2*(height//8)+20,35,50)
    pygame.draw.rect(canvas, gray, rectg5,  0, 5)


    rectg6 = ((5*(width//7)+18), 2*(height//8)+20,80,50)
    pygame.draw.rect(canvas, gray, rectg6,  0, 5)

    

    for event in pygame.event.get():
    
        
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            coordinatelst.append((pygame.mouse.get_pos()))
            count = count+1
            count1 = count1+1
            
            sqx = (coordinatelst[count][0] - ((width//5.2)-25))**2
            sqy = (coordinatelst[count][1] - (3*(height//8)+40))**2

            sqx1 = (coordinatelst[count][0] - (2*(width//5.2)-25))**2

            sqx2 = (coordinatelst[count][0] - (3*(width//5.2)-25))**2

            sqx3 = (coordinatelst[count][0] - (4*(width//5.2)-25))**2

            sqx4 = (coordinatelst[count][0] - (5*(width//5.2)-25))**2


            if equals == True:
                clearscreen()
                keypresslst = []
                num1 = ''
                num2 = ''
                ans = 0
                prevnumend = 0
                operationslst = []
                count1 = 0
                equals = False

            
            if coordinatelst[count][0]>0 and coordinatelst[count][0]<width//3 and coordinatelst[count][1]>height//2+10 and coordinatelst[count][1]<(5*(height//8))+10:
                

                keypresslst.append('1')

            elif coordinatelst[count][0]>width//3 and coordinatelst[count][0]<2*(width//3) and coordinatelst[count][1]>height//2+10 and coordinatelst[count][1]<(5*(height//8))+10:
                

                keypresslst.append('2')

            elif coordinatelst[count][0]>2*(width//3) and coordinatelst[count][0]<width and coordinatelst[count][1]>height//2+10 and coordinatelst[count][1]<(5*(height//8))+10:

                keypresslst.append('3')

            elif coordinatelst[count][0]>0 and coordinatelst[count][0]<width//3 and coordinatelst[count][1]>5*(height//8)+10 and coordinatelst[count][1]<(6*(height//8))+10:
                

                keypresslst.append('4')

            elif coordinatelst[count][0]>width//3 and coordinatelst[count][0]<2*(width//3) and coordinatelst[count][1]>5*(height//8)+10 and coordinatelst[count][1]<(6*(height//8))+10:
                

                keypresslst.append('5')

            elif coordinatelst[count][0]>2*(width//3) and coordinatelst[count][0]<width and coordinatelst[count][1]>5*(height//8)+10 and coordinatelst[count][1]<(6*(height//8))+10:
                

                keypresslst.append('6')

            elif coordinatelst[count][0]>0 and coordinatelst[count][0]<width//3 and coordinatelst[count][1]>6*(height//8)+10 and coordinatelst[count][1]<(7*(height//8))+10:

                keypresslst.append('7')

            elif coordinatelst[count][0]>width//3 and coordinatelst[count][0]<2*(width//3) and coordinatelst[count][1]>6*(height//8)+10 and coordinatelst[count][1]<(7*(height//8))+10:

                keypresslst.append('8')

            elif coordinatelst[count][0]>2*(width//3) and coordinatelst[count][0]<width and coordinatelst[count][1]>6*(height//8)+10 and coordinatelst[count][1]<(7*(height//8))+10:

                keypresslst.append('9')

            elif coordinatelst[count][0]>width//3 and coordinatelst[count][0]<2*(width//3) and coordinatelst[count][1]>7*(height//8)+10 and coordinatelst[count][1]<(8*(height//8))+10:

                keypresslst.append('0')
                    

            elif math.sqrt(sqx + sqy) < 33:
                keypresslst.append('+')
                operationslst.append(count1)

            elif math.sqrt(sqx1 + sqy) < 33:
                keypresslst.append('-')
                operationslst.append(count1)

            elif math.sqrt(sqx2 + sqy) < 33:
                keypresslst.append('x')
                operationslst.append(count1)

            elif math.sqrt(sqx3 + sqy) < 33:
                keypresslst.append('÷')
                operationslst.append(count1)



            

            elif coordinatelst[count][0]>(width//7 - 45) and coordinatelst[count][0]<(width//7 + 35) and coordinatelst[count][1]>2*(height//8)+20 and coordinatelst[count][1]<(8*(height//8))+70:

                if len(anslst)==0:
                    pass
                else:
                    keypresslst.append(anslst[len(anslst)-1])
                
                    

            elif coordinatelst[count][0]>(2*(width//7)-7) and coordinatelst[count][0]<(2*(width//7)+28) and coordinatelst[count][1]>2*(height//8)+20 and coordinatelst[count][1]<(8*(height//8))+70:

                keypresslst.append(".")

            elif coordinatelst[count][0]>(3*(width//7)-15) and coordinatelst[count][0]<(3*(width//7)+20) and coordinatelst[count][1]>2*(height//8)+20 and coordinatelst[count][1]<(8*(height//8))+70:

                keypresslst.append("")

            elif coordinatelst[count][0]>(4*(width//7)-22) and coordinatelst[count][0]<(4*(width//7)+13) and coordinatelst[count][1]>2*(height//8)+20 and coordinatelst[count][1]<(8*(height//8))+70:

                keypresslst.append("")

            elif coordinatelst[count][0]>(5*(width//7)-27) and coordinatelst[count][0]<(5*(width//7)+8) and coordinatelst[count][1]>2*(height//8)+20 and coordinatelst[count][1]<(8*(height//8))+70:

                keypresslst.append("3.1415")

            elif coordinatelst[count][0]>(5*(width//7)+18) and coordinatelst[count][0]<(5*(width//7)+98) and coordinatelst[count][1]>2*(height//8)+20 and coordinatelst[count][1]<2*(height//8)+70:

                if len(keypresslst)>0:
                    keypresslst.pop(len(keypresslst)-1)
                    count1=count1-2
                

            elif coordinatelst[count][0]>(5*(width//7)+18) and coordinatelst[count][0]<(5*(width//7)+98) and coordinatelst[count][1]> 7*(height//8)+20 and coordinatelst[count][1]< 7*(height//8)+70:
                for z in range(0,len(operationslst)):
                    num1 = ''
                    num2 = ''

                    if z > 0:
                        num1 = ans
                    else:

                        for i in range(prevnumend,operationslst[z]):
                            num1 = num1+keypresslst[i]
                        try:
                            num1 = Decimal(num1)
                            if num1 % 2 == 0 or (num1 + 1) % 2 == 0:
                                num1 = int(num1)

                        except InvalidOperation:
                            check = False




                    operator = keypresslst[operationslst[z]]
                    if len(operationslst)>0 and (z+1)!= len(operationslst):
                        prevnumend = operationslst[z+1]
                    else:
                        prevnumend = len(keypresslst)


                
                    for x in range (operationslst[z]+1, prevnumend):
                        num2 = num2+keypresslst[x]
                    try:
                        num2 = Decimal(num2)
                        if num2 % 2 == 0 or (num2 + 1) % 2 == 0:
                            num2 = int(num2)

                    except InvalidOperation:
                        check = False
                        

                    
                    if operator == 'x':
                        ans = num1 * num2

                    if operator == '+':
                        ans = num1 + num2

                    if operator == '-':
                        ans = num1 - num2

                    if operator == '÷':
                        ans = num1 / num2

                if (ans + 1) % 2 == 0 or (ans % 2) == 0:
                    ans = int(ans)
                else:
                    ans = round(ans,3)
                print("Your answer is: ", ans)
                keypresslst.append('=')
                keypresslst.append(ans)
                anslst.append(str(ans))
                equals = True



            screen = ''
            clearscreen()


            for i in keypresslst:
                screen = screen+str(i)

                
           
            font = pygame.font.Font('freesansbold.ttf', 50)
            text = font.render(screen, True, white)
            textRect = text.get_rect()
            textRect.center = (width-30, (height//6))
            textRect.right = width-30
            
            
            canvas.blit(text,textRect)
            pygame.display.update()

            
            
            


pygame.quit()
