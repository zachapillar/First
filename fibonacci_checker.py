nth_number=int(input("check a number between 1-20577:"))
while nth_number not in range(20577):
	nth_number=int(input("that's not between 1-20577 silly, try again:"))
fibonacci1=int(1)
fibonacci2=int(1)
even=int(-1)

if nth_number%10==1:
	stndrdth="st"
elif nth_number%10==2:
	stndrdth="nd"
elif nth_number%10==3:
	stndrdth="rd"
else:
	stndrdth="th"

for bob in range(nth_number-2):
	even=even+1
	if even%2==0:
		fibonacci2=fibonacci1+fibonacci2
	else:
		fibonacci1=fibonacci1+fibonacci2

if even%2==0:
	print(f"the {nth_number}{stndrdth} number of the fibonacci sequence is: {fibonacci2}")
else:
	print(f"the {nth_number}{stndrdth} number of the fibonacci sequence is: {fibonacci1}")