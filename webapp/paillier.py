import math
import modOperations as modOp
import rabinMiller
class PublicKey:
	def __init__(self,n,g):
		self.n = n
		self.g = g
		self.n2 = n*n
	def __repr__(self):
		return "Public Key : (%s, %s)" %(self.n,self.g)
class PrivateKey:
	def __init__(self,l,mu):
		self.l = l
		self.mu = mu
	def __repr__(self):
		return "Private Key : (%s, %s)" %(self.l,self.mu)


def L(x,n):
	return (x-1)//n

def generateKeypair(bits,k = 128 ):
	p = rabinMiller.generatePrime(bits,k)
	q = rabinMiller.generatePrime(bits,k)
	while(p==q):
		q = rabinMiller.generatePrime(bits,k)
	# p,q = 463,487 # why?
	p,q = 668474771,940044349
	n = p*q
	phi = (p-1)*(q-1)
	l = phi//math.gcd(p-1,q-1)
	g = n+1
	n2 = n*n
	while(math.gcd(modOp.expoMod(g,l,n2),n)!=1):
		g += 1
	#Inverse mod
	mu = modOp.expoMod(L(modOp.expoMod(g,l,n2),n),phi-1,n)
	return PrivateKey(l,mu), PublicKey(n,g)

def encrypt(pb,msg):
	#generate a prime
	msg = int(msg)
	r = pb.n - 1
	while(math.gcd(r,pb.n)!=1):
		r+=1
	
	cipher = modOp.expoMod(r,pb.n,pb.n2)
	cipher = cipher*(modOp.expoMod(pb.g,msg,pb.n2))
	cipher = cipher%pb.n2
	return cipher

def decrypt(pr,pb,c):
	c = int(c)
	m = L(modOp.expoMod(c,pr.l,pb.n2),pb.n) * pr.mu
	m = m%pb.n
	return m

#Adding plaintext p to a ciphertext
def homomorphicAddP(pb,c,p):
	return (c*modOp.expoMod(pb.g,p,pb.n2))%pb.n2

#Adding two CipherText
def homomorphicAddC(pb,c1,c2):
	return (c1*c2)%pb.n2

def homomorphicMul(pb,c,p):
	return modOp.expoMod(c,p,pb.n2)

#Subtracting a plaintext p from a Ciphertext
def homomorphicSub(pb,c,p):
	enc = encrypt(pb,p)
	inv = modOp.invMod(enc,pb.n2)
	return (c*inv)%pb.n2
#Subtracting a Ciphertext p from a Ciphertext : c1-c2
def homomorphicSubCC(pb,c1,c2):
	inv = modOp.invMod(c2,pb.n2)
	return (c1*inv)%pb.n2

#divide by a constant if divible 
def homomorphicDivision(pb,c,p):
	pdash = modOp.invMod(p,pb.n)
	return modOp.expoMod(c,pdash,pb.n2)
	
