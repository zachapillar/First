file=open("AOC_day_1_input.txt")
file=file.read()
file=file.split()

code=file
print(code)
currently_reading=0
code_length=len(code)
dial=list(range(100))
actual_code=0
dial_position=50

def dial_changer(direction, distance, current_dial_position):
	if direction=="L":
		current_dial_position-=distance
	else:
		current_dial_position+=distance
	return current_dial_position

while currently_reading<code_length:
	direction=code[currently_reading][:1]
	distance=int(code[currently_reading][1:])
	dial_position=dial_changer(direction, distance, dial[dial_position])%100
#	if dial_position>0:
#		dial_position%=100
	currently_reading+=1
	print(dial_position)
	if dial[dial_position]==0:
		actual_code+=1

print(actual_code)