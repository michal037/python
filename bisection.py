# MIT License
# Copyright (c) 2020, Michal Kozakiewicz, github.com/michal037

import math

def bisection(f, a, b, eps=1e-17, max_iter=100):
	'''
	  Darboux's theorem:
	    If the function is continuous at interval [a, b] and f(a) * f(b) < 0,
		then there exists such r from (a, b), where f(r) == 0.

	  Parameters:
	    f        - function returning a double
	    a        - double: left  end of the interval [a, b]
	    b        - double: right end of the interval [a, b]
	    eps      - double: assumed accuracy (optional)
	    max_iter - integer: maximum number of steps (optional)

	  Return:
	    double - approximation of the root of the function
		None   - bisection method fails
	'''

	fa = f(a)
	fb = f(b)

	# no solution
	if fa * fb > 0:
		print('bisection method fails!')
		return None
	  
	# one end of the interval is the solution
	if fa == 0:
		return a
	if fb == 0:
		return b

	# calculate the number of steps to the desired epsilon
	iter = math.ceil(math.log2(math.fabs((b - a) / eps)))
	if iter > max_iter:
		iter = max_iter

	# approximation
	for _ in range(iter):
		c = (a + b) / 2
		fc = f(c)

		if   f(a) * fc < 0:
			b = c
		elif f(b) * fc < 0:
			a = c
		elif fc == 0:
			return c
		else:
			print('bisection method fails!')
			return None

	return (a + b) / 2


if __name__ == '__main__':
	print('f(x) = math.sin(x) - (x - 1) / 2')
	print('[a, b] = [-3.2, 3.2]')

	f = lambda x: math.sin(x) - (x - 1) / 2
	print('root:', bisection(f, -3.2, 3.2))
