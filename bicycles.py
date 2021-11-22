bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('ducati')
bicycles.insert(-1,'bucati')
age = 21
del age
del bicycles[0]
bicycles.remove('ducati')
last = bicycles.pop()
second_last = bicycles.pop(-2)
bicycles.sort()
bicycles.sort(reverse = True)
print(sorted(bicycles))
print(sorted(bicycles, reverse = True))
bicycles.reverse()
print(bicycles[-1])
print(last)
print(len(bicycles))