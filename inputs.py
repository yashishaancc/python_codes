i = 0
while i <= 10:
	i += 1
	if i % 2 == 0:
		continue
	if i > 8:
		break
	print("In while loop: " + str(i));
string = input("Enter something:")
print(string + "\nBye!")
age = int(input("Enter your age: "))
if age >= 18:
	print("You are eligible to vote")
else:
	print("You are not eligible to vote")
name = input("Enter your name: ")
print("Hi " + name.title() + ".")
color = input("What's your favourite color: ")
print("Oh! Your favourite color is " + color.lower() + ".")
if(color.lower() == 'black'):
	print("\x1b[30m")
if(color.lower() == 'red'):
	print("\x1b[31m")
if(color.lower() == 'green'):
	print("\x1b[32m")
if(color.lower() == 'yellow'):
	print("\x1b[33m")
if(color.lower() == 'purple'):
	print("\x1b[34m")
if(color.lower() == 'pink'):
	print("\x1b[35m")
if(color.lower() == 'blue'):
	print("\x1b[36m")
print("       -----       ");
print("    ---     ---    ");
print("  --           --  ");
print(" -     o   o     - ");
print("-                 -");
print("-        |        -");
print(" -     \\___/     - ");
print("  --           --  ");
print("    ---     ---    ");
print("       -----       ");
print("Bye")