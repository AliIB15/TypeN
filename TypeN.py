####################<BY ALIIB15>##########################
#TypeN
def isN(n):
	'''it shows if the number is one of The National Numbers'''
	if n <= 0 or int(n) != n :
		return False
	else:
		return True
		
def isW(n):
	'''it show's if the number is one of National number or is 0'''
	if int(n) != n or n < 0:
		return False
	else:
		return True
		
def isZ(n):
	'''it show's if the Number is one of Z Numbers'''
	if int(n)!=n:
		return False
	else:
		return True 

def isQ(n):
	'''it show's if The Number is one Of Q Number'''
	return n #all Number in Python is from Q  XD <3
	
def isOdd(n):
	if not int(str(n)[len(str(n))-1]) in [0,2,4,6,8]:
		return True
	else:
		return False
		
def isEven(n):
	if int(str(n)[len(str(n))-1]) in [0,2,4,6,8]:
		return True
	else:
		return False

def isprime(n):
	'''it shows if the number is a prime number'''
	primelist = [1,2,3]
	if n in primelist:
		return True
	elif n == 4:
		return False
	else:
		for i in range(2,int(n**1/2)):
			if n%i == 0:
				return False
			else:
				pass
		return True
		
def prime_arrange(n):
	'''it shows the number using it's arrange, it's limit is 7000th'''
	global isprime
	listprime = []
	for i in range(1,n*10):
		if isprime(i):
			listprime.append(i)
		else:
			pass
	return listprime[n-1]
				
def perfect_numbers_arrange(n):
	'''it shows the the perfect number using it's arrange, it limit is 7000th'''
	x = prime_arrange(n) 
	perfect_number = (2**(x-1))*((2**(x))-1)
	return perfect_number
