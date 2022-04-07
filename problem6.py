def sum_square_difference(n):
	
	sum_of_square = 1**2
	for i in range(2,n+1):
		sum_of_square += i**2 
	
	list = []
	sum = 0
	for i in range(1,n+1):
		sum += i
	sum_square = sum**2
	ssd = sum_square - sum_of_square
	return ssd
print(sum_square_difference(100))
