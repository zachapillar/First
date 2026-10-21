d={}
with open("passwords.txt") as f:
    for line in f:
       (key, val)=line.split()
       d[(key)]=val

account_name=input("enter an account name:")
account_name=account_name.replace(" ", "")
if account_name in d.keys():
	password=input("enter your password:")
	password=password.replace(" ", "")
	if password==d[account_name]:
		print("login successful!")
	elif password!=d[account_name]:
		print("wrong password")
else:
	continue_account=input("that's not currently an account, would you like to make a new account with that name? Press y to continue, or n to cancel:")
	if continue_account=="y":
		password=input(f"you are making an account with the username {account_name}, please enter a password for that account:")
		password=password.replace(" ", "")
		with open("passwords.txt", "a") as myfile:
			myfile.write(f"\n{account_name} {password}")