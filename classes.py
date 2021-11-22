class Restaurant():
	def __init__(self, name, cuisine_type):
		self.name = name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print("\nRestaurant's name is " + self.name + ".")
		print("Restaurant's cuisine type is " + self.cuisine_type + ".")
	def open_restaurant(self):
		print("\nRestaurant " + self.name + " is open.")
rest = Restaurant("misthan", 'great')
rest2 = Restaurant("surat", 'great')
rest3 = Restaurant("misthan", 'great')
print(rest.name)
print(rest.cuisine_type)
rest.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()
rest.open_restaurant()
from random import randint
string = str(randint(1,10**100000))
print(string)
birthday = '26110'
if birthday in string:
	print("YES")
else:
	print("NO")
message = "I really like dogs dogs."
print(message.replace('dog', 'cat').split())
print(message)
c = 1;d = 2
print(c);print(d)