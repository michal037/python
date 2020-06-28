# MIT License
# Copyright (c) 2020, Michal Kozakiewicz, github.com/michal037

import math

def newton(f, df, x0, eps=1e-15, max_iter=100):
	'''
	  We assume that a second derivative exists.

	  Parameters:
	    f        - function returning a double
	    df       - derivative of f
	    x0       - double: point near the solution
<<<<<<< HEAD
	    eps      - double: assumed accuracy (optional); 0 < eps < 1
	    max_iter - integer: maximum number of steps (optional); max_iter > 0
=======
	    eps      - double: assumed accuracy (optional)
	    max_iter - integer: maximum number of steps (optional)
>>>>>>> f7e9857746ad2da992365429edd4604d0aa2f0c1

	  Return:
	    double - approximation of the root of the function
	    None   - newton method fails
	'''

	x = x0

	for _ in range(max_iter):
		fx = f(x)

		# check epsilon for solution
		if math.fabs(fx) <= eps:
			return x
		
		dfx = df(x)

		# derivative is zero = no solution
		if dfx == 0:
			return None
		
		x = x - fx / dfx

	# exceeded maximum iterations = no solution
	return None

if __name__ == '__main__':
	print('f(x)  = math.sin(x) - (x - 1) / 2')
	print('df(x) = math.cos(x) - 0.5')

	f  = lambda x: math.sin(x) - (x - 1) / 2
	df = lambda x: math.cos(x) - 0.5
	print('root:', newton(f, df, 2.5))
