numbers=input("enter a list of numbers with spaces, and no commas:")
numbers=numbers.split()
numbers=map(float, numbers)
numbers=list(numbers)
list_length=len(numbers)
still_going=1

while still_going==1:
	still_going=0
	for index in enumerate(numbers):
		index=index[0]
		if index!=list_length-1:
			next_index=index+1
		if numbers[index]>numbers[next_index]:
			numbers_stored=numbers[index]
			numbers[index]=numbers[next_index]
			numbers[next_index]=numbers_stored
			still_going=1

print(numbers)