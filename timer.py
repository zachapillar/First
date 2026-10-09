import time
start=time.time()
user_input=input("press enter after ten seconds")
end=time.time()
total=end-start
print(f"You did it in: {total:.2f} seconds")