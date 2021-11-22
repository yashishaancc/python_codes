from math import sqrt
print("Okay,lets begin our WONDERFUL game");
print("In what range would you like to think of a number?");
print("Enter 3 for 0-7 and 4 for 0-15 and 5 for 0-31 and so on:");
num=0;
n = int(input())
print("Now think of a number in your chosen range");
for i in range(n):
    k = 0
    print("\x1b[32m")
    for j in range(int(2**n)):
        if j//int(2**i) % 2 == 1:
            print(j, end = "\t")
            k += 1
            if k%int(sqrt(2**(n-1))) == 0:
                print("\n")
    print("\x1b[0mDoes your number belong to the above given set of numbers?");
    c = input("Enter Y for YES,N for NO:  ");
    if c == 'Y' or c == 'y':
        num += 2**i
print("I know that if you think your number in your chosen range then,");
print("The number you think is \x1b[32m\x1b[5m" + str(num) + "\a");