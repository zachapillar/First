import random

random_number=random.randint(1, 100)
random_number=int(random_number)
print(random_number)

user_input=0

while user_input!=random_number:
	user_input=input("Guess_a_number:")
	user_input=int(user_input)
	if random_number<user_input:
		print("too high, guess again")
	elif random_number>user_input:
		print("too low, guess again")
	else:
		print("you did it!")