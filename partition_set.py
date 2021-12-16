def fact(n):
	lis = [1 for i in range(n+1)]
	for i in range(1,n+1):
		lis[i] = i*lis[i-1]
	return lis[n]
def number_of_partitions(string, n, length, min, c, fac):
	if n == 0:
		c[0] += 1
		# for i in range(length):
		# 	print(string[i], end = " ")
		# print()
		num = fac
		# print(f'num = {num}')
		i = 0
		while i < length:
			j = i
			count = 0
			while i < length and string[i] == string[j]:
				count += 1
				num = num//fact(string[i])
				i += 1
			num = num//fact(count)
		c[1] += num
		# print(f'num = {num}')
		return c[1]
	for i in range(min, n+1):
		string[length] = i
		number_of_partitions(string, n-i, length+1, i, c, fac)
ip = 'Enter n <= 40 to find number of partitions of a set with n elements: '
num = input(ip)
num = int(num)
n = num
# for n in range(num+1):
fac = fact(n)
c = [0, 0]
string = [0 for i in range(n)]
number_of_partitions(string, n, 0, 1, c, fac)
# print(f'number of partitions of {n} are: {c[0]}')
print(f'number of partitions of a set with {n} elements are: {c[1]}')