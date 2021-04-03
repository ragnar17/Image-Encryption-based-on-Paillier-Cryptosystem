import paillier

f = 5
class FloatingPoint:
	def __init__(self, mantissa, exponent):
		self.mantissa = mantissa
		self.exponent = exponent
	def __repr__(self):
		return "(%s, %s)" %(self.mantissa,self.exponent)

def encryptFP(pb, x):
	"""
	x = 3.54 or 23.12 or 23
	returns an obj of type FloatingPoint, after encrypting x with pb
	"""
	e = -f
	x = int(x * (10 ** f))
	if x==0 :
		e = 0
	while x % 10 == 0 and x:
		x = x // 10
		e += 1
	return FloatingPoint(paillier.encrypt(pb, x), e)

def getValue(pr, pb, x):
	"""
	Returns the decryptred value of x in floating point type
	"""
	ret = paillier.decrypt(pr, pb, x.mantissa)
	for _ in range(abs(x.exponent)):
		if x.exponent > 0:
			ret = ret * 10
		else:
			ret = ret / 10
	return ret

def addEncEnc(pb,x, y):
	"""
	Adds 2 FP numbers x, y in their encryptred form & returns the result
	in encrypted form as well.
	"""
	mantissa_x = x.mantissa
	mantissa_y = y.mantissa
	res_exponenet = min(y.exponent, x.exponent)

	if x.exponent < y.exponent:
		mantissa_y = paillier.homomorphicMul(pb,mantissa_y, 10 ** (y.exponent - x.exponent))
	else:
		mantissa_x = paillier.homomorphicMul(pb,mantissa_x, 10 ** (x.exponent - y.exponent))

	res_mantissa = paillier.homomorphicAddC(pb,mantissa_x, mantissa_y)

	return FloatingPoint(res_mantissa, res_exponenet)

def addEncConst(pb,x,y):
	enc_y = encryptFP(pb,y)
	return addEncEnc(pb,x,enc_y)

def multiplyEncPlain(pb,x, y):
	"""
	Multiplies encrypted x with plain text FP y 
	"""
	# rewriting y
	e = -f
	y = int(y * (10 ** f))
	if y==0 :
		e = 0
	while y % 10 == 0 and y:
		y = y // 10
		e += 1

	return FloatingPoint(paillier.homomorphicMul(pb, x.mantissa, y) , x.exponent + e)

def subtractEncEnc(pb,x,y):
	"""
	Unsafe
	Subtract encrypted y from encrypted x
	Do only when the result is positive
	"""
	# rewriting y
	mantissa_x = x.mantissa
	mantissa_y = y.mantissa
	res_exponenet = min(y.exponent, x.exponent)
	if x.exponent < y.exponent:
		mantissa_y = paillier.homomorphicMul(pb,mantissa_y, 10 ** (y.exponent - x.exponent))
	else:
		mantissa_x = paillier.homomorphicMul(pb,mantissa_x, 10 ** (x.exponent - y.exponent))

	res_mantissa = paillier.homomorphicSubCC(pb,mantissa_x, mantissa_y)
	return FloatingPoint(res_mantissa, res_exponenet)


# pr,pb = paillier.generateKeypair(30)

# x = encryptFP(pb, 128)
# print(getValue(pr,pb,x),x)
# y = encryptFP(pb, 2)

