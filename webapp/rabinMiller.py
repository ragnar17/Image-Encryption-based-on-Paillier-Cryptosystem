import modOperations as modOp
import random

def millerTest(d,n):
	a = random.randint(3,n-2)
	p = modOp.expoMod(a,d,n)
	if(p==1 or p==n-1):
		return True;
	while(d!=n-1):
		p = (p*p)%n
		d *= 2
		if(p == 1):
			return False
		if(p == n-1):
			return True
	return False

def isPrime(n,k = 128):
	if(n <= 4):
		if(n==2 or n==3):
			return True
		else:
			return False
	# n-1 is even , let n-1 = d*(2^r)
	d = n - 1
	while(d%2==0):
		d//=2
	while(k):
		if(millerTest(d,n) == False):
			return False
		k-=1
	return True

def generatePrime(bits,k = 128):
	while(True):
		n = random.randint(2**(bits-1),2**bits-1) | 1
		if(isPrime(n,k)):
			return n