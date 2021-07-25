def factor(x):
	for i in range(1, x+1):
		if x % i == 0:
			yield(i)

def runPoly(coefs, x):
	y = 0
	for e, c in enumerate(coefs[::-1]):
		y += x ** e * c
	return y

def factorPoly(coefs):
	factors = list(factor(coefs[0])) + list(factor(coefs[-1]))
	for row in range(len(factors)):
		factors.append(-factors[row])
	return factors

def zero(coefs, factors):
	for factor in factors:
		sol = runPoly(coefs, factor)

		if sol == 0:
			return factor

def synthetic(numerator, denominator):
	factored = [numerator[0]]
	for row in numerator[1:]:
		factored.append(row + factored[-1] * denominator)
	return factored

div = None
coefs = list(map(int, input('Coefficients: ').split()))
while div != coefs:
	factors = factorPoly(coefs)
	denominator = zero(coefs, factors)
	div = synthetic(coefs, denominator)

	coefs = div

	print(div)
