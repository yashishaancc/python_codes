class Animal():
	def __init__(self):
		self.living = True
		self.head = 1
	def dead(self):
		self.living = False
	def __repr__(self):
		living_str = "living" if self.living else "dead"
		return f"I am a {living_str} animal"
class Dog(Animal):
	def __init__(self):
		super().__init__()
		self.legs = 4
		self.sound = "Bho"
	def __repr__(self):
		return "I am a dog"
class Cat(Animal):
	def __init__(self):
		super().__init__()
		self.legs = 4
		self.sound = "Meow"
	def __repr__(self):
		print(super().__repr__())
		return "I am a cat"