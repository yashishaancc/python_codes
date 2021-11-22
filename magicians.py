magicians = ['alice', 'david', 14, 'bob', 14, 0.01, "1" + "1", ["a", 3]]
for magician in magicians:
	print(magician)
numbers = list(range(1,6))
print(numbers)
for value in range(1,5):
	print(value)
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
digi = list(range(10))
# This dig is a copy of digits
dig = digits[:]
# This dig is not copy but same as digits
# dig = digits
print(dig)
print(digi)
print(min(digits))
print(max(digits))
print(sum(digits))
print([value**2 for value in range(1,11)])
lis = list(range(1,1001))
print(min(lis))
print(max(lis))
print(sum(lis))
print([i**3 for i in range(1,11)])
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:3])
print(players[2:])
print("Here are last three players of our team:")
for player in players[-3:]:
	print(player.title())
print('A tuple\'s dimension must be >= 2 and they can\'t be changed')
dimensions = (200,50)
dimensions = (400,20)
print(dimensions[0])
foods = ("a", "b", "c", "d", 'e')
for food in foods:
	print(food)