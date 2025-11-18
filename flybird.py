from turtle import width
import pygame
import random
pygame.init()


WIDTH = 400
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy bird")
color = (0,0,0)
clock = pygame.time.Clock()


#-------------------------------LOAD IMAGE -----------------------------------

bird_image = pygame.image.load("C:/Users/User/Desktop/Flybird-pygame/bird1.png").convert_alpha()
bird_image = pygame.transform.scale(bird_image, (34, 24))

bird_sprites = [bird_image]

pipe_image = pygame.image.load("C:/Users/User/Desktop/Flybird-pygame/pipe.png").convert_alpha() # adjust resolution 
pipe_width = 70 # width of pipes
pipe_gap = 50


#------------------------GAME FUNCTION--------------------------------



def create_pipe():
    height_top = random.randint(50, HEIGHT - pipe_gap - 50)
    pipe_top = pygame.Rect(WIDTH, 0, pipe_width, height_top)
    pipe_bottom = pygame.rect(WIDTH, height_top, + pipe_gap,
    pipe_width, HEIGHT - (height_top + pipe_gap))
    return(pipe_top, pipe_bottom)


pipe_velocity = 3
def draw_pipes(pipes):
    for pipe in pipes:
        pipe_top, pipe_bottom = pipe
        pipe_top.x -= pipe_velocity
        pipe_bottom.x -= pipe_velocity
        top_image = pygame.transform.flip(pipe_image, False, True)
        screen.blit(top_image, (pipe_top.x, pipe_top.height - top_image.get_height()))
        screen.blit(pipe_image, (pipe_bottom.x, pipe_bottom.y))

running = True 
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(5)
pygame.quit()
