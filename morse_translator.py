code_on_off=input("bonk?:")
code_on_off=int(code_on_off)
message=input("message:")
message_list=list(message)
translation={
"a": ".-",
"b": "-...",
"c": "-.-.",
"d": "-..",
"e": ".",
"f": "..-.",
"g": "--.",
"h": "....",
"i": "..",
"j": ".---",
"k": "-.-",
"l": ".-..",
"m": "--",
"n": "-.",
"o": "---",
"p": ".--.",
"q": "--.-",
"r": ".-.",
"s": "...",
"t": "-",
"u": "..-",
"v": "...-",
"w": ".--",
"x": "-..-",
"y": "-.--",
"z": "--..",
" ": "/"}

if code_on_off==1:
	for index, bob in enumerate(message_list):
		message_list[index]=translation[bob]
else:
	if code_on_off==2:
		message_list=message.split()
		for index, bob in enumerate(message_list):
			message_list[index]=list(translation.keys())[list(translation.values()).index(bob)]

if code_on_off==1: 
	output=" ".join(message_list)
else:
	if code_on_off==2: 
		output="".join(message_list)
print(output)
