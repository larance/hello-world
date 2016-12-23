def my_abs(x):
	if x >=0:
		return x
	else:
		return -x

def power(x, n=2):
	s = 1
	while n > 0:
		n = n -1
		s = s * x
	return s

t = power(5)
print(t)
