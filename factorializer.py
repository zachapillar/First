#import math
#number=int(input("Gimme a number between 0-1558:"))
#print(math.prod(list(range(1, number+1))))

number=int(input("Gimme a number between 0-1558:"))
number=(list(range(1, number+1)))
while len(number)>1:
	number[0]=number[0]*number[1]
	number.remove(number[1])
print(f"{number}")