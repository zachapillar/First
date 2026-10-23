filename=input("please enter a file name:")
file=open(filename)
file=file.read()
file=file.split()
searching_for=input("What would you like to find?")
print(file)
file_length=len(file)
continuing=0
while continuing<file_length:
	if searching_for in file[continuing]:
		print(file[continuing])
	continuing+=1