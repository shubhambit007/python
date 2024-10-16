import random
def display_grid(d):
	row=3
	col=3
	
	print('.'+'-'*3+'.'+'-'*3+'.'+'-'*3+'.')
	for i in range(row):
		print('|',end='')
		for j in range(col):
			print(f'{d[i][j]}'.center(3),end='|')
		print()
		print('.'+'-'*3+'.'+'-'*3+'.'+'-'*3+'.')
			
	return 0

def check(d,p):

	if p=='X':
		if d[0][0]==d[0][1]==d[0][2]=='X' or d[0][0]==d[1][0]==d[2][0]=='X' or d[0][0]==d[1][1]==d[2][2]=='X' or d[1][0]==d[1][1]==d[1][2]=='X' or d[0][1]==d[1][1]==d[2][1]=='X' or d[2][0]==d[2][1]==d[2][2]=='X' or d[2][2]==d[1][2]==d[0][2]=='X':
			return True
	else:
		if d[0][0]==d[0][1]==d[0][2]=='O' or d[0][0]==d[1][1]==d[2][2]=='O' or d[1][0]==d[1][1]==d[1][2]=='O' or d[0][1]==d[1][1]==d[2][1]=='O' or d[2][0]==d[2][1]==d[2][2]=='O' or d[2][2]==d[1][2]==d[0][2]=='O':
			return True
	return False

def enter_values(d,player):
	z1=random.randint(0,1)
	p=player[z1]
	if p=='X':
		while True:
			print('player {}:'.format(p))
			x=int(input("enter x co-ordinate:"))
			y=int(input("enter y co-ordinate:"))
			initialize(x,y,d,p)
			if check(d,p):
				print('player {} wins'.format(p))
				break
			print('player {}:'.format('O'))
			x=int(input("enter x co-ordinate:"))
			y=int(input("enter y co-ordinate:"))
			initialize(x,y,d,'O')
			if check(d,'O'):
				print('player {} wins'.format('O'))
				break
		else:
			while True:
				print('player {}:'.format('O'))
				x=int(input("enter x co-ordinate:"))
				y=int(input("enter y co-ordinate:"))
				initialize(x,y,d,'O')
				if check(d,'O'):
					print('player {} wins'.format(p))
					break
				print('player {}:'.format(p))
				x=int(input("enter x co-ordinate:"))
				y=int(input("enter y co-ordinate:"))
				initialize(x,y,d,p)
				if check(d,p):
					print('player {} wins'.format('O'))
					break
			
def initialize(x,y,d,z1):
	while True:
		if d[x][y]=='':
			d[x][y]=z1
			display_grid(d)
			break;
		else:
			print('position is already filled try to fill other')
	
z=9
d=[['','',''],['','',''],['','','']]
display_grid(d)

player=['X','O']
enter_values(d,player)
	

#print('|{}|{}|{}|'.format(d[i][0],d[i][1],d[i][2]))
