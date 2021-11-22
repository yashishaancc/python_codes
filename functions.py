import module
print(module.power(65536))
import module as m
print(m.fibonacci(1000))
from module import power
print(power(1024))
from module import power as p
print(p(256))
from module import *
print(fibonacci(100))
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name = 'willie')
describe_pet('willie')
describe_pet('willie', animal_type = 'dog')
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')
mid = ''
if mid:
	print(mid)
else:
	print(len("Empty"[:-1]))
def returned(n):
	if n == 0:
		return
	if n == 1:
		return 42
	if n == 2:
		return "abcd"
	if n == 3:
		return [1, 2, "c"]
	elif n == '4' or n == 5:
		return {1: 2, 'c': 5}
n = int(input("Enter a number: "))
print(returned(n))
def make_pizza(size, *toppings):
	# Next line is a docstring comment
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + str(topping))
make_pizza(20)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese', 42)
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location = 'princeton',
                             field = 'physics')
print(user_profile)