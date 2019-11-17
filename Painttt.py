import pygame
import sys
import random
import string
import time
from PIL import Image


pygame.init()
 	
WIDHT = 800
HEIGHT = 800
size = (WIDHT,HEIGHT)
Tol_size = (150,800)
Paint_size = (650,800)

game_over = False
RADIUS = 7
SQUARESIZE = 25
#COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (230,14,2)
GREEN = (14,181,28)
BLUE = (24,34,222)
GREY = (186,186,186)
PINK = (230,2,200)
CLEAR_COLOR = (97,86,86)

mouse_state = 0
screen = pygame.display.set_mode(size,pygame.DOUBLEBUF)
screen.fill(WHITE)
bg_surf = pygame.surface.Surface(Paint_size)
bg_surf.fill(WHITE)
screen.blit(bg_surf,(150,0))
tol_surf = pygame.surface.Surface(Tol_size)
tol_surf.fill(GREY)
pygame.display.flip()
font = pygame.font.SysFont('Arial',25)
current_color = BLACK
bg_color = WHITE
bg_num = 0



def file_name_generator(size):
	chars = string.ascii_uppercase + string.digits
	return ''.join(random.choice(chars) for _ in range(size))+'.png'

print(str(file_name_generator(10)))

def button(x,y,h,w,c1,s,):
	global current_color
	mouse_state = pygame.mouse.get_pressed()
	mouse_pos = pygame.mouse.get_pos()
	pygame.draw.rect(s, c1, (x, y, w, h))
	if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y :
		if mouse_state[0] == 1:
			current_color = c1
			#print("clicked")

def bg_button(x,y,h,w,c1,s,):
	global bg_color
	global bg_num
	mouse_state = pygame.mouse.get_pressed()
	mouse_pos = pygame.mouse.get_pos()
	pygame.draw.rect(s, c1, (x, y, w, h))
	if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y :
		if mouse_state[0] == 1:
			bg_color = c1
			#print("clicked")
			bg_num = bg_num + 1
			#print(bg_num)

def cl_button(x,y,h,w,c1,s,):
	global paint_surf
	global bg_color
	mouse_state = pygame.mouse.get_pressed()
	mouse_pos = pygame.mouse.get_pos()
	pygame.draw.rect(s, c1, (x, y, w, h))
	if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y :
		if mouse_state[0] == 1:
			paint_surf.fill(bg_color)
			paint_surf.fill(pygame.SRCALPHA)
			#print("clicked")

def sv_button(x,y,h,w,c1,s,):
	global save_surface
	global bg_surf
	global paint_surf
	file_name = str(file_name_generator(10))
	mouse_state = pygame.mouse.get_pressed()
	mouse_pos = pygame.mouse.get_pos()
	pygame.draw.rect(s, c1, (x, y, w, h))
	if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y :
		if mouse_state[0] == 1:
			save_surface.blit(bg_surf,(0,0))
			save_surface.blit(paint_surf,(0,0))
			pygame.image.save(save_surface,file_name)
			time.sleep(3)
			#print("clicked")


ColorsTextSurface = font.render('COLORS',False,(0,0,0))
BackGroundTextSurface = font.render('BACKGROUND',False,(0,0,0))
ClearTextSurface = font.render('CLEAR',False,(255,255,255))
SaveTextSurface = font.render('SAVE',False,(255,255,255))
paint_surf = pygame.Surface(Paint_size,pygame.SRCALPHA)
save_surface = pygame.Surface(Paint_size)

while not game_over:
	screen.blit(bg_surf,(150,0))
	screen.blit(paint_surf,(150,0))	 
	screen.blit(tol_surf,(0,0))
	tol_surf.blit(ColorsTextSurface,(30,0))
	tol_surf.blit(BackGroundTextSurface,(2,305))
	red_button = button(85,40,50,50,RED,tol_surf)
	black_button = button(20,40,50,50,BLACK,tol_surf)
	blue_button = button(20,105,50,50,BLUE,tol_surf)
	green_button = button(85,105,50,50,GREEN,tol_surf)
	white_button = button(20,170,50,50,WHITE,tol_surf)
	pink_button = button(85,170,50,50,PINK,tol_surf)
	pygame.draw.rect(tol_surf,current_color,(50,240,50,50))
	white_bg_button = bg_button(85,345,50,50,WHITE,tol_surf)
	black_bg_button = bg_button(20,345,50,50,BLACK,tol_surf)
	cl_button1 = cl_button(20,420,50,120,CLEAR_COLOR,tol_surf)
	save_button = sv_button(20,490,50,120,CLEAR_COLOR,tol_surf)
	tol_surf.blit(ClearTextSurface,(45,430))
	tol_surf.blit(SaveTextSurface,(55,495))	
	if bg_num == 1:
		bg_surf.fill(bg_color)
		bg_num = 0
	pygame.display.flip()
	x,y = pygame.mouse.get_pos()
	x=x-150
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_state = 1
		elif event.type == pygame.MOUSEBUTTONUP:
			mouse_state = 0
		if mouse_state == 1:
			pygame.draw.circle(paint_surf,current_color,(x,y), RADIUS)	
			pygame.display.flip()
			

