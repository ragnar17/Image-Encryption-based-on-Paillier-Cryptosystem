def expoMod(base,exponent,mod):
	ans = 1
	while(exponent != 0 ):
		if((exponent&1)):
			ans = ans*base
			ans = ans%mod
		base = (base*base)%mod
		exponent >>= 1
	return ans

def invMod(a,m):
	m0 = m
	y,x = 0,1
	#Base Case
	if(m==1):
		return 0
	while(a > 1):
		q = a//m
		t = m
		m = a%m
		a = t
		t = y
		y = x - q*y
		x = t
	if(x < 0):
		x += m0
	return x