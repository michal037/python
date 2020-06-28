# MIT License
# Copyright (c) 2020, Michal Kozakiewicz, github.com/michal037

import math

def secant(f, a, b, eps=1e-15, max_iter=100):
	'''
	  Darboux's theorem:
	    If the function is continuous at interval [a, b] and f(a) * f(b) < 0,
	    then there exists such r from (a, b), where f(r) == 0.

	  Parameters:
	    f        - function returning a double
	    a        - double: left  end of the interval [a, b]
	    b        - double: right end of the interval [a, b]
	    eps      - double: assumed accuracy (optional); 0 < eps < 1
	    max_iter - integer: maximum number of steps (optional); max_iter > 0

	  Return:
	    double - approximation of the root of the function
	    None   - secant method fails
	'''

	# one end of the interval is the solution
	if f(a) == 0:
		return a	
	if f(b) == 0:
		return b

	# approximation
	for _ in range(max_iter):
		denominator = f(b) - f(a)
		if denominator == 0:
			return None

		c = b - f(b) * ((b - a) / denominator)

		if math.fabs(f(c)) <= eps:
			return c

		a, b = b, c
	
	# exceeded maximum iterations = no solution
	return None

if __name__ == '__main__':
	print('f(x) = math.sin(x) - (x - 1) / 2')
	print('[a, b] = [-3.2, 3.2]')

	f  = lambda x: math.sin(x) - (x - 1) / 2
	print('root:', secant(f, -3.2, 3.2))
