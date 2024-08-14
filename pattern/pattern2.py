def pattern1(x):

	for j in range(2 *x+1):
		if(j == x):
			print('+',end = '')
		else:
			print(' ', end = '')
	print()		


	for i in range(x-1):
		for j in range(2 *x+1):
			if j == (x-1) - i  or j == x + i+1:
				print('+', end = '')
			else:
				print(' ', end = '')
		print()
	
	for j in range(2 *x+1):
		if(j == 0) or (j == 2*x):
			print('+',end = '')
		else:
			print(' ', end = '')
	print()		

	for i in range(x-2,-1,-1):
		for j in range(2 *x+1):
			if j == (x-1) - i  or j == x + i+1:
				print('+', end = '')
			else:
				print(' ', end = '')
		print()

	for j in range(2 *x+1):
		if(j == x):
			print('-',end = '')
		else:
			print(' ', end = '')
	print()

