string = input("Enter numbers to be summed separatred by spaces:\n")
lis = string.split()
addition = 0;
multiplication = 1;
for s in lis:
	addition += int(s)
	multiplication *= int(s)
print("Sum is " + str(addition))
print("Product is " + str(multiplication))