n = int(input("Enter a number(0 to 405) to find partitions: "))
a = [[] for i in range(n+1)]
for i in range(n+1):
	a[i] = [1 for j in range(n+1)]
for p in range(1, n+1):
	for i in range(1, p+1):
		a[p][i] = 0
		for j in range(1, i+1):
			if p-i >= j:
				a[p][i] += a[p-i][j]
		if a[p][i] == 0:
			a[p][i] = 1
s = [0 for i in range(n+1)]
for p in range(0, n+1):
	for i in range(1, p+1):
		s[p] += a[p][i]
	if p == 0:
		s[p] += 1
	print(f'number of partitions of {p} are {s[p]}')
# print(f'number of partitions of {n} are {s[n]}')