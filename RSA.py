import random
import time
from math import gcd

n = 1000

def getPrimeList(n):

	bool_list = [True for i in range(n - 1)]
	for i in range(2, n + 1):
		if(bool_list[i - 2]):
			j = 2
			while i * j <= n:
				bool_list[i * j - 2] = False
				j += 1

	return [i for i in range(2, n + 1) if(bool_list[i - 2])]

def randomPrimeListFrom(a, b): # [a, b]
	return [i for i in getPrimeList(b) if(i >= a)]

def randomPrimeFrom(a, b): # [a, b]
	return random.choice(randomPrimeListFrom(a, b))

# Borders
a = 20#00000
b = 30#00000

# Primes
p = randomPrimeFrom(a, b)

l = randomPrimeListFrom(a, b)
l.remove(p)
q = random.choice(l)

# Euler Function
u = (p - 1) * (q - 1)

print(p)
print(q)
print(u)
e = random.choice(list(filter(lambda it: gcd(it, u) == 1, range(2, u))))
print(e)


def secretExponent(e, u):
    d = 1
    while e * d % u != 1:
        d += 1
    return d

 