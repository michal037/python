# https://github.com/michal037

class Singleton:
	def __new__(cls, *_, **__):
		self = object.__new__(cls)
		cls.__new__ = lambda *a, **b: self
		return self

	def singleton(self):
		self.__class__.__new__ = lambda *c, **d: self

### EXAMPLE 1 ### EXAMPLE 1 ### EXAMPLE 1 ### EXAMPLE 1 ### EXAMPLE 1 ##########

class MyClass(Singleton):
	def __init__(self, a, *args, **kwargs):
		self.val = a
		print(f'a = {a}')

		for arg in args:
			print(f'next arg = {arg}')
		
		for key, value in kwargs.items():
			print(f'{key} = {value}')
		
		print()

a = MyClass(1, 2, 3, hi='hello', it='works')
b = MyClass(4, 5, 6, cc='hello', dd='works')

# Proof that it's the same object.
print(f'{{a.val, b.val}} = {{{a.val}, {b.val}}}') # {4, 4}
print(f'(a is b) = {a is b}') # True
print()

### EXAMPLE 2 ### EXAMPLE 2 ### EXAMPLE 2 ### EXAMPLE 2 ### EXAMPLE 2 ##########

class Test(Singleton):
	# Assuming that we are overriding the __new__ magic method,
	# we have to manually trigger .singleton() method.
	def __new__(cls):
		self = object.__new__(cls)
		self.value = 'hi'
		return self

t1 = Test()
t2 = Test()
print(f'(t1 is t2) = {t1 is t2}') # False


t2.singleton()
# From now, the constructor always returns reference to the same object.
t3 = Test()
print(f'(t2 is t3) = {t2 is t3}') # True