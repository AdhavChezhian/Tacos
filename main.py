import pygame
pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width,height))
run = True

# sprites
player = pygame.Rect((300,250,50,50))


# physics variables
moveSpeed = 0.5


while run:

  screen.fill('black')

  pygame.draw.rect(screen, (255,0,0), player)



  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()
  
pygame.quit