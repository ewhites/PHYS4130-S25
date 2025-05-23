import numpy as np
import math # Used towards square-rooting things.
import scipy as sp # For Legendre polynomial weight and roots

def f(x,c): # The function that we are working with.
	f = math.sin(math.sqrt(100*x))**2
	if c == "Y": f = math.sqrt(128) * (math.sin(x))**5
	return f

def leftpoint(a,b,N,c):
	sum, h = 0, (b-a)/N
	x = a # Setting the left point at x = a.
	for i in range(0,N-1):
		x += h # Iterating by h.
		sum += f(x,c) * h # Adding this new rectangle sum.

	return sum

def rightpoint(a,b,N,c):
	sum, h = 0, (b-a)/N
	x = a + h # Setting the point at x = a + h (the right of the leftpoint rectangle)
	for i in range(0,N-1):
		x += h # Iterating by h.
		sum += f(x,c) * h # Adding this new rectangle sum.

	return sum

def midpoint(a,b,N,c):
	sum, h = 0, (b-a)/N
	x = a + h/2 # Finding the middle between left and right endpoints.
	for i in range(0,N-1):
		x += h # Iterating by h.
		sum += f(x,c) * h # Adding this new rectangle sum.

	return sum

def trapezoid(a,b,N,c):
        sum = (leftpoint(a,b,N,c) + rightpoint(a,b,N,c))/2 # Formula provided by homework.
        return sum

def simpson(a,b,N,c):
        sum = trapezoid(a,b,N,c)/3 + 2*midpoint(a,b,N,c)/3 # Formula provided by homework.
        return sum

def quadrature(a,b,N,c): # Quadrature method!
	roots, weights = sp.special.roots_legendre(N) # Provided on writeup.
	sum = 0
	for i in range(0,N):
		sum += weights[i] * f(((b-a)*roots[i]+a+b)/2,c) # Multiplies the weight by the function evaluated at optimal points. Essentially saying weights * f(x(u)).
		if i == N-1: sum *= (b-a)/2 # Our du-component that we must use from our initial mapping.

	return sum

def usubtest(a,b,x): # Function used to test whether a and b truly map to -1 and 1.
	usub = (2*x-a-b)/(b-a)
	return usub

def answer(L,R,M,T,S,Q): # Just prints the integral values obtained from different methods.
	print("\nThe correct value should be 1.0057025.\n")
	print("The result of the integral, with the left point method, is:", L)
	print("The result of the integral, with the right point method, is:", R)
	print("The result of the integral, with the mid point method, is:", M)
	print("The result of the integral, using the trapezoidal method, is:", T)
	print("The result of the integral, using Simpson's method, is:", S)
	print("The result of the integral, using the quadrature method, is:", Q)
	return

def init(a,b,N): # Initializes variables to correspond to integral values.
	c = "weed goku 69" # Just ignore this LOL.
	L = leftpoint(a,b,N,c)
	R = rightpoint(a,b,N,c)
	M = midpoint(a,b,N,c)
	T = trapezoid(a,b,N,c)
	S = simpson(a,b,N,c)
	Q = quadrature(a,b,N,c)

	return L,R,M,T,S,Q

def methodcheck(a,b): # Used towards creating the Simpson's rule N-table.
	N, correct, error, i = 1, 1.0057025428, 1, 0
	print("") # Ignore this LOL.
	while error > 0.0000005: # For finding 6-significant digits accuracy.
		val = simpson(a,b,N,"weed goku 69") # Calculating value at this N. Ignore weed goku.
		error = abs(correct - val) # Calculating error from actual value.
		print("N: ",N,", VALUE: ",f"{val:.{8}g}",", ERROR: ",f"{error:.{3}g}") # Creates the n-table.
		i += 1 # Iterating i.
		N = 2 ** i # Iterating N = 2^i

	return
