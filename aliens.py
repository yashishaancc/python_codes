alien = {1: 2, 3: 1}
alien = {}
if alien:
	print(5555)
alien = {2: 3, 2: 3}
empty = alien
alien['color'] = 'green'
alien['points'] = 5
alien[0] = 25
alien[1] = 25
print(alien['color'])
del alien['color']
print(empty)
for k, v in alien.items():
	print("\nkey: " + str(k))
	print("value: " + str(v))
for name in alien.keys():
	print("\n" + str(name))
for name in alien:
	print("\n" + str(name))
if 'colour' not in alien:
	print("Not")
for val in alien.values():
	print(val)
print('\n')
for v in set(alien.values()):
	print(v)
if alien:
	print(5555)