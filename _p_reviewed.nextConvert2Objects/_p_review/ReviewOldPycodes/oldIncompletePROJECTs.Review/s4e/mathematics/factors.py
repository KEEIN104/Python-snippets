# factors.py
# Finding factors

A = int(input('Factors of: '))
print('-----calculating factors------ \nA = %d' %A)

factors = [1,A]
n = 2
while n < A/n:
	if A % n == 0:
		bigfactor = int(A/n)
		smallfactor = n
		factors += [smallfactor, bigfactor]
		n+=1
	else:
		n+=1
		
print('Factors:\n'+str(factors))

'''Computing observation
1) max. 16 digit number
'''
