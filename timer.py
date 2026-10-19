import time
total=0
start=time.time()
delayer=1
forwards_backwards=0
attempts=0
user_start=input("your goal is to get 10 seconds. Every time you press enter, it will tell you the time, and then start counting half as fast (most it can be 1/16th speed). If it's past 10, it will start counting backwards. press enter when you're ready:")
while total<9.99 or total>10.01:
	start=time.time()
	user_input=input("press enter after ten seconds:")
	end=time.time()
	if forwards_backwards==0:
		total=total+(end-start)/delayer
	else:
		total=total-(end-start)/delayer
	if total>10:
		forwards_backwards=1
	else:
		forwards_backwards=0
	print(f"You did it in: {total:.2f} seconds")
	if delayer<9:
		delayer*=2
	attempts+=1
print(f"you did it in {attempts} attempts")
