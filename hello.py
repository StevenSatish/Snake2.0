'''
Created on Sep 26, 2023

@author: steve
'''
import pygame
import time
import random
 
pygame.init()
pygame.font.init()
pygame.mixer.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 51, 51)
snakeColor = (0, 204, 0)
blue = (50, 153, 213)
 
dis_width = 800
dis_height = 600

 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake 2.0 by Steven')
pygame.draw.rect(dis, white,[400, 300, 10, 10])
clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10
oldScore = 0

chomp = pygame.mixer.Sound("C:\\Users\\steve\\eclipse-workspace\\SnakeGame\\sounds\\chomp.ogg")
powerUp = pygame.mixer.Sound("C:\\Users\\steve\\eclipse-workspace\\SnakeGame\\sounds\\powerUp.ogg")
levelUp = pygame.mixer.Sound("C:\\Users\\steve\\eclipse-workspace\\SnakeGame\\sounds\\levelUp.ogg")
music = pygame.mixer.music.load("C:\\Users\\steve\\eclipse-workspace\\SnakeGame\\sounds\\backMusic.ogg")
pygame.mixer.music.play(-1)
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 25)
level_up_font = pygame.font.SysFont("bahnschrift", 20)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    global oldScore
    global snake_speed
    global levelUp
    dis.blit(value, [50, 558])
    progress = score % 5
    if (progress == 0 and score > 4):
        newVal = level_up_font.render("Level up! Your snake's speed has increased", True, blue)
        dis.blit(newVal, [300, 560])
    changeScore = oldScore != score
    if (changeScore):
        oldScore += 1
        if (score % 5 == 0 and score != 0):
            snake_speed += 3
            pygame.mixer.Sound.play(levelUp)
    
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snakeColor, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style. render(msg, True, color)
    dis.blit(mesg, [dis_width / 4.6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
 
    x1_change = 0
    y1_change = 0
    
    snake_block = 10
    global snake_speed
    global oldScore
    global skipSpeedUp
 
    snake_List = []
    Length_of_snake = 1
    lastD = 0 #variable to store current direction of snake, 1 for left, 2 for right, 3 for up, 4 for down    
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - 60 - snake_block) / 10.0) * 10.0
    powerx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    powery = round(random.randrange(0, dis_height - 60 - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            pygame.draw.rect(dis, white,[0, 540, 800, 60])
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if lastD != 2:
                        x1_change = -snake_block
                        y1_change = 0
                        lastD = 1
                elif event.key == pygame.K_RIGHT:
                    if lastD != 1:
                        x1_change = snake_block
                        y1_change = 0
                        lastD = 2
                elif event.key == pygame.K_UP:
                    if lastD != 4:
                        y1_change = -snake_block
                        x1_change = 0
                        lastD = 3
                elif event.key == pygame.K_DOWN:
                    if lastD != 3:
                        y1_change = snake_block
                        x1_change = 0
                        lastD = 4
 
        if x1 >= dis_width or x1 < 0 or y1 >= (dis_height - 60) or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white,[0, 540, 800, 60])
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            pygame.mixer.Sound.play(chomp)
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - 60 - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

            
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
gameLoop()