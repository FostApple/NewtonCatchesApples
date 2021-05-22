import pygame
import random
pygame.init()
wn = pygame.display.set_mode((500,500))

gameon = True
heart = pygame.image.load('heart.png')
newton = pygame.image.load('newton.png')
apple = pygame.image.load('apple.png')
score = 0

font = pygame.font.Font('COMIC.TTF', 50)

gofont = pygame.font.Font('COMIC.TTF', 30)

lives = 3

nx = 240
ny = 450

ax = random.randint(0,490)
ay = 10

while gameon:
  wn.fill((255,255,255))
  pygame.time.delay(20)

  wn.blit(newton, (nx, ny))

  wn.blit(apple, (ax,ay))

  pygame.event.pump()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a]:
    nx -= 15
  if keys[pygame.K_d]:
    nx += 15

  if nx > 475-25:
    nx = 475-25 

  if nx < 0:
    nx = 0 

  ay += (6 + score)
  if ay > 500:
    ax = random.randint(0,490)
    ay = 10
    lives -= 1

  if nx-25 < ax+15 < nx+50+25 and ay > 450:
    score += 1
    ax = random.randint(0,490)
    ay = 10

  text = font.render(str(score), True, (150,0,0))
  wn.blit(text, (450,0))

  if lives == 0:
    gotext = gofont.render('Game Over, your score is ' + (str(score)), True, (150,0,0))
    wn.blit(gotext, (75,200))
    gameon = False

  if lives == 3:
    wn.blit(heart, (5,5))
    wn.blit(heart, (55,5))
    wn.blit(heart, (105,5))

  elif lives == 2:
    wn.blit(heart, (5,5))
    wn.blit(heart, (55,5))

  elif lives == 1:
    wn.blit(heart, (5,5))

  if lives == 0:
    print('You are dead')

  pygame.display.update()

print("Your score is",score)