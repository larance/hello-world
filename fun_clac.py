def clac(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
nums = [1, 2, 3]
t  = clac(*nums)

print(t)
