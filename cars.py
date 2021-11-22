cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	elif car != 'subaru':
		print(car.title())
	else:
		print(car.lower())
age = 19
age2 = 22
print((age < 21) == False)
print((age <= 21) == True)
print(age > 21)
print(age >= 21)
print(age >= 21 and age2 >= 21)
print(age >= 21 or age2 >= 21)
print('audi' not in cars)
print('suzuki' in cars)
lis = []
# if lis is true if lis is not empty
if lis:
	print(lis)
else:
	print("empty".title())
l = [1, 2, 6, 4, 4, 5.0, 5]
l.sort()
print(l)
print(sorted(l,reverse = True))