import pygame
import random
import os

pygame.mixer.init()

pygame.init()
s_width=900
s_heigth=600
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
game_window=pygame.display.set_mode((s_width,s_heigth))
bgimg=pygame.image.load('background.jpg')
bgimg2=pygame.image.load('background2.png')
bgimg3=pygame.image.load('background3.png')
bgimg=pygame.transform.scale(bgimg,(s_width,s_heigth)).convert_alpha()
bgimg2=pygame.transform.scale(bgimg2,(s_width,s_heigth)).convert_alpha()
bgimg3=pygame.transform.scale(bgimg3,(s_width,s_heigth)).convert_alpha()
font=pygame.font.SysFont(None,30)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window,color,snake_l,s1):
    for x,y in snake_l:
        pygame.draw.rect(game_window,color,(x,y,s1,s1))

clock=pygame.time.Clock()

pygame.display.set_caption("Snake Part 1")

def welcome():
    game_exit=False
    while not game_exit:
        game_window.fill((233,220,229))
        game_window.blit(bgimg2,(0,0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    #pygame.mixer.music.load('bg.mp3')
                    #pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)
        
def gameloop():
    game_exit=False
  
    food_x=random.randint(20,s_width-100)
    food_y=random.randint(20,s_heigth-100)
    food_size=10
    game_over=False
    score=0
    s1=20
    fps=30
    velocity_x=0
    velocity_y=0
    snake_l=[]
    snake_length=1
    snake_x=50
    snake_y=50
    if(not os.path.exists("highscoresnake.txt")):
                with open("highscoresnake.txt","w") as f:
                    f.write("0")
    with open("highscoresnake.txt","r") as f:
        highscore=f.read()
    while not game_exit:
        if game_over:
           
            with open("highscoresnake.txt","w") as f:
                        f.write(str(highscore))
            game_window.fill(white)
            game_window.blit(bgimg3,(0,0))
            
            pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    game_exit=True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    game_exit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0
            
                    if event.key==pygame.K_UP: 
                        velocity_x=0
                        velocity_y=-10
                    if event.key==pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y=0
                    if event.key==pygame.K_DOWN:
                        velocity_x=0
                        velocity_y=10
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<15   and abs(snake_y-food_y)<15:
                score+=10
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
                print("SCORE",score)
                food_x=random.randint(20,s_width-100)
                food_y=random.randint(20,s_heigth-100)
                snake_length+=5
                if score>int(highscore):
                    highscore=score
                    
        
            game_window.fill(white)
            game_window.blit(bgimg,(0,0))
            text_screen("Score"+str(score)+" HiScore"+str(highscore),red,5,5)
            
            pygame.draw.rect(game_window,red,(food_x,food_y,food_size,food_size))
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_l.append(head)
            if len(snake_l)>snake_length:
                del snake_l[0]
            if head in snake_l[:-1]:
                game_over=True
            if snake_x<0 or snake_x>s_width or snake_y<0 or snake_y>s_heigth:
                game_over = True
                
            plot_snake(game_window,black,snake_l,s1)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()

