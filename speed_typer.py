import time
file=open("buncha_words.txt")
file=file.read()
file=file.split()
import random
word_list=[(random.choice(file)), (random.choice(file)), (random.choice(file)), (random.choice(file)), (random.choice(file)), (random.choice(file)), (random.choice(file)), (random.choice(file))]
word_list=" ".join(word_list) 
print(word_list)

ready=input("type that as fast as you can. Press enter when you're ready:")
start=time.time()
user_input=input("Go!:")

end=time.time()
total=end-start
if user_input==word_list:
	print(f"You did it in: {total:.2f} seconds")
else:
	print("you messed up somewhere")