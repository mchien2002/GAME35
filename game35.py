import pygame
import math
pygame.init()
screen = pygame.display.set_mode((600, 600)) 
running = True

GREEN = (50, 168, 82)
BLACK = (0, 0, 0)
BLUE = (33, 13, 214)
YELLOW = (223, 247, 40)
WHITE = (255, 255, 255)

font1 = pygame.font.SysFont('sans', 50)
font2 = pygame.font.SysFont('sans', 26)
font3 = pygame.font.SysFont('sans', 80)

text_1 = font1.render('1', True, BLACK)
text_2 = font1.render('2', True, BLACK)
text_3 = font1.render('3', True, BLACK)
text_4 = font1.render('4', True, BLACK)
text_5 = font1.render('5', True, BLACK)
computerwin = font1.render('Computer Win !!', True, BLACK)
playerwin = font1.render('Player Win !!', True, BLACK)

text1 = font2.render('Computer', True, BLACK)
text2 = font2.render('Player', True, BLACK)
text_start = font1.render('Start', True, BLACK)
text_reset = font1.render('Reset', True, BLACK)
start1 = False
start2 = False
start = False

Sum = 0
m = 0
n = 0

def computer_number(n, Sum):
	if (Sum == 0 or Sum == 16 or Sum == 29) and n != 3:
		return 3
	if (Sum == 12 or Sum == 25 and n != 5):
		return 5
	if Sum <= 8:
		for i in range(1, 6):
			if i != n and Sum + i == 9:
				return i
	if 9 < Sum < 15:
		for i in range(1, 6):
			if i != n and Sum + i == 15:
				return i
	if 16 < Sum < 22:
		for i in range(1, 6):
			if i != n and Sum + i == 22:
				return i
	if Sum > 22:
		for i in range(1, 6):
			if i != n and Sum + i == 28:
				return i
	if Sum > 29:
		for i in range(1, 6):
			if i != n and Sum + i == 35:
				return i

while running:
	screen.fill(GREEN)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, (100, 100, 100, 50))
	pygame.draw.rect(screen, WHITE, (400, 100, 100, 50))
	pygame.draw.rect(screen, YELLOW, (125, 160, 50, 50))
	pygame.draw.rect(screen, YELLOW, (425, 160, 50, 50))

	pygame.draw.rect(screen, WHITE, (75, 30, 50, 50))#1
	pygame.draw.rect(screen, WHITE, (175, 30, 50, 50))#2
	pygame.draw.rect(screen, WHITE, (275, 30, 50, 50))#3
	pygame.draw.rect(screen, WHITE, (375, 30, 50, 50))#4
	pygame.draw.rect(screen, WHITE, (475, 30, 50, 50))#5

	pygame.draw.rect(screen, WHITE, (250, 300, 100, 100)) # Sum
	pygame.draw.rect(screen, WHITE, (200, 500, 200, 50)) # Who win

	pygame.draw.rect(screen, WHITE, (450, 250, 100, 50)) #Start
	pygame.draw.rect(screen, WHITE, (450, 350, 110, 50))# Reset

	screen.blit(text_start, (450, 250))
	screen.blit(text_reset, (450, 350))
	
	screen.blit(text_1, (75, 30))
	screen.blit(text_2, (175, 30))
	screen.blit(text_3, (275, 30))
	screen.blit(text_4, (375, 30))
	screen.blit(text_5, (475, 30))
	
	screen.blit(text1, (100, 100))
	screen.blit(text2, (400, 100))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if 450 < mouse_x < 550 and 250 < mouse_y < 300:
					start = True
					start1 = True
				if 75 < mouse_x < 125 and 30 < mouse_y < 80:
					if n == 1 or start != True:
						pass
					else:
						m = 1
						start2 = True
				if 175 < mouse_x < 225 and 30 < mouse_y < 80:
					if n == 2 or start != True:
						pass
					else:
						m = 2
						start2 = True
				if 275 < mouse_x < 325 and 30 < mouse_y < 80:
					if n == 3 or start != True:
						pass
					else:
						m = 3
						start2 = True
				if 375 < mouse_x < 425 and 30 < mouse_y < 80:
					if n == 4 or start != True:
						pass
					else:
						m = 4
						start2 = True
				if 475 < mouse_x < 525 and 30 < mouse_y < 80:
					if n == 5 or start != True:
						pass
					else:
						m = 5
						start2 = True
				if 450 < mouse_x < 560 and 350 < mouse_y < 400:
					start1 = False
					start2 = False
					start = False
					Sum = 0
					m = 0
					n = 0

	if start1 == True:
		if Sum < 35:
			n = computer_number(m, Sum)
			Sum += n
			start1 = False
		if Sum == 35:
			whowin = font2.render('Computer Win !!', True, BLACK)
			screen.blit(whowin, (200, 500))
			start1 = True

	if Sum < 35:
		if start2 == True:
			Sum += m
			start2 = False
			start1 = True
	if start == True:
		computer = font1.render(str(n), True, BLUE)
		screen.blit(computer, (125, 160))
		player = font1.render(str(m), True, BLUE)
		screen.blit(player, (425, 160))
		text_Sum = font3.render(str(Sum), True, BLACK)
		screen.blit(text_Sum, (260, 300))

	pygame.display.flip()

pygame.quit()