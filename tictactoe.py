#TicTacToe game


import pygame,sys
import numpy as np
pygame.init()

HEIGHT = 600
WIDTH = 600
Line_color = (23,145,135)

Screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
Screen.fill((28,170,156))

pygame.draw.line(Screen,Line_color,(200,0),(200,600),5)
pygame.draw.line(Screen,Line_color,(400,0),(400,600),5)
pygame.draw.line(Screen,Line_color,(0,200),(600,200),5)
pygame.draw.line(Screen,Line_color,(0,400),(600,400),5)

board = np.zeros((3,3))                                                                               
def draw_figure(row,col,player):
	if player ==1:
		pygame.draw.line(Screen,(60,60,60),(col*200+25,row*200+25),((col+1)*200-25,(row+1)*200-25),5)
		pygame.draw.line(Screen,(60,60,60),((col+1)*200-25,row*200+25),((col)*200+25,(row+1)*200-25),5)
	elif player ==2:
		pygame.draw.circle(Screen,(255,255,255),((clicked_col*200+100),(clicked_row*200+100)),70,5)

def mark_square(row,col,player):
	board[row][col] = player
def available_square(row,col):
	return board[row][col]==0
def is_board_full():
	for i in range(3):
		for j in range(3):
			if board[i][j]==0:
				return False
	return True


def check_win(player):
	for i in range(3): #horizontal win
		if board[i][0] ==player and board[i][1]== player and board[i][2]==player:
			draw_horizontal_line(i,player)
			return True
	for  i in range(3):
		if board[0][i] ==player and  board[1][i]== player and board[2][i]==player:
			draw_vertical_line(i,player)
			return True
	if board[0][0]==player and board[1][1]==player and board[2][2]==player:
		des_diagonal_line(player)
		return True
	if board[2][0]==player and board[1][1] == player and board[0][2]==player:
		asc_diagonal_line(player)
		return True 
	return False

	
def draw_vertical_line(col,player):
	if player ==1:
		pygame.draw.line(Screen,(255,255,255),(col*200+100,15),(col*200+100,600-15),10)
	elif player==2:
		pygame.draw.line(Screen,(60,60,60),(col*200+100,15),(col*200+100,600-15),10)
def draw_horizontal_line(row,player):
	if player ==1:
		pygame.draw.line(Screen,(255,255,255),(15,row*200+100),(600-15,row*200+100),10)
	elif player==2:
		pygame.draw.line(Screen,(60,60,60),(15,row*200+100),(600-15,row*200+100),10)
def asc_diagonal_line(player):
	if player ==1:
		pygame.draw.line(Screen,(255,255,255),(600-15,15),(15,600-15),10)
	elif player ==2:
	 	pygame.draw.line(Screen,(60,60,60),(600-15,15),(15,600-15),10)
def des_diagonal_line(player):
	if player ==1:
		pygame.draw.line(Screen,(255,255,255),(15,15),(600-15,600-15),10)
	elif player ==2:
	 	pygame.draw.line(Screen,(60,60,60),(15,15),(600-15,600-15),10)
def restart():
	Screen.fill((28,170,156))
	pygame.display.set_caption('TIC TAC TOE')
	pygame.draw.line(Screen,Line_color,(200,0),(200,600),5)
	pygame.draw.line(Screen,Line_color,(400,0),(400,600),5)
	pygame.draw.line(Screen,Line_color,(0,200),(600,200),5)
	pygame.draw.line(Screen,Line_color,(0,400),(600,400),5)
	for i in range(3):
		for j in range(3):
			board[i][j]=0

game_over = False
player =1

#mainloop
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
			mouseX = event.pos[0] #x coordinate of click
			mouseY = event.pos[1] #y coordinate of click

			clicked_row = int(mouseY//200)
			clicked_col = int(mouseX//200)
			if available_square(clicked_row,clicked_col):
				if player ==1:
					mark_square(clicked_row,clicked_col,1)
					draw_figure(clicked_row,clicked_col,1)
					if check_win(player):
						pygame.display.set_caption('TIC TAC TOE: Player 1 Wins, Press r to play again.')
						game_over=True
					elif is_board_full():
						pygame.display.set_caption('TIC TAC TOE: Its a Tie!, Press r to play again')
					player = 2
				elif player == 2:
					mark_square(clicked_row,clicked_col,2)
					draw_figure(clicked_row,clicked_col,2)
					if check_win(player):
						pygame.display.set_caption('TIC TAC TOE: Player 2 Wins, Press r to play again.')
						game_over = True
					elif is_board_full():
						pygame.display.set_caption('TIC TAC TOE: Its a Tie!, Press r to play again')
					player = 1
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				restart()
				game_over = False
				player =1
	pygame.display.update()