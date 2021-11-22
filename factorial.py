def factorial(n):
	if n==0:
		return 1
	else:
		fac = [1 for i in range(n+1)]
		for i in range(2,n+1):
			fac[i] = i * fac[i-1]
		return fac[n]
def isPrime(n):
	flag = 0
	for i in range(2,n):
		if(n%i == 0):
			flag = 1
	if flag == 1 or n == 1:
		return False
	else:
		return True
for n in range(1,1001):
	if isPrime(n):
		print(n)
for n in range(1):
	num = int(input("Enter number in range 0 to 100000 "
					"whose factorial you want to find:"));
	print(num)
	print(factorial(num))