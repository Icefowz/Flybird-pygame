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
pipe_gap = 100













#------------------------GAME FUNCTION--------------------------------



def create_pipe():
    height_top = random.randint(50, HEIGHT - pipe_gap - 50)
    pipe_top = pygame.Rect(WIDTH, 0, pipe_width, height_top)
    pipe_bottom = pygame.Rect(WIDTH, height_top + pipe_gap,
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




#------------------------MAIN GAME LOOP-------------------------------
global bird_Y
bird_X = 50
bird_Y = HEIGHT // 2
bird_velocity = 0
bird_index = 0
bird_animation_timer = 0
gravity = 0.5
jump_strengt = -5




pipes = [create_pipe()]








running = True 
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strengt
    bird_velocity += gravity
    bird_Y += bird_velocity
    bird_animation_timer += 1
    
    if bird_animation_timer % 5 == 0:
        bird_index = (bird_index + 1 ) % len(bird_sprites)
    
    bird_image_current = bird_sprites[bird_index]

    bird_rect = bird_image_current.get_rect(center =(bird_X, int(bird_Y)))
    screen.blit(bird_image_current, bird_rect)

    draw_pipes(pipes)
    #add random pipes
    if pipes [-1][0].x < WIDTH - 200:
        pipes.append(create_pipe())         
    pygame.display.update()
    clock.tick(30)
pygame.quit()
