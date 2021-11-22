def power(n):
	return 2**n
def fibonacci(n):
	if n == 0 or n == 1:
		return n
	else:
		fib = [0 for i in range(n+1)]
		fib[1] = 1
		for i in range(2,n+1):
			fib[i] = fib[i-1] + fib[i-2]
		return fib[n]