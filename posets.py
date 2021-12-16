def is_partial_order(n, grid):
	for i in range(n):
		for j in range(n):
			for k in range(n):
				if grid[i][j] and grid[j][k] and not grid[i][k]:
					return False
			if i != j and grid[i][j] and grid[j][i]:
				return False
	return True
def number_of_posets(n, grid, itr):
	if  itr == n*n:
		if is_partial_order(n, grid):
			c[0] += 1
	elif itr//n == itr%n:
		grid[itr//n][itr%n] = 1
		number_of_posets(n, grid, itr+1)
	else:
		for i in range(2):
			grid[itr//n][itr%n] = i
			number_of_posets(n, grid, itr+1)
ip = 'Enter n <= 4 to find number of partial orders of a set with n elements: '
n = int(input(ip))
c = [0]
grid = [[] for i in range(n)]
for i in range(n):
	grid[i] = [0 for i in range(n)]
number_of_posets(n, grid, 0)
print(f'number of posets of a set with {n} elements are: {c[0]}')