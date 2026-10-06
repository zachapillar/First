message=input("message:")
message2=list(message)
translation={
"a": ".- ",
"b": "-... ",
"c": "-.-. ",
"d": "-.. ",
"e": ". ",
"f": "..-. ",
"g": "--. ",
"h": ".... ",
"i": ".. ",
"j": ".--- ",
"k": "-.- ",
"l": ".-.. ",
"m": "-- ",
"n": "-. ",
"o": "--- ",
"p": ".--. ",
"q": "--.- ",
"r": ".-. ",
"s": "... ",
"t": "- ",
"u": "..-",
"v": "...- ",
"w": ".-- ",
"x": "-..- ",
"y": "-.-- ",
"z": "--.. ",
" ": "/ "}
for index, bob in enumerate(message2):
	match bob:
		case ("a"):
			message2[index]=translation["a"]
		case ("b"):
			message2[index]=translation["b"]
		case ("c"):
			message2[index]=translation["c"]
		case ("d"):
			message2[index]=translation["d"]
		case ("e"):
			message2[index]=translation["e"]
		case ("f"):
			message2[index]=translation["f"]
		case ("g"):
			message2[index]=translation["g"]
		case ("h"):
			message2[index]=translation["h"]
		case ("i"):
			message2[index]=translation["i"]
		case ("j"):
			message2[index]=translation["j"]
		case ("k"):
			message2[index]=translation["k"]
		case ("l"):
			message2[index]=translation["l"]
		case ("m"):
			message2[index]=translation["m"]
		case ("n"):
			message2[index]=translation["n"]
		case ("o"):
			message2[index]=translation["o"]
		case ("p"):
			message2[index]=translation["p"]
		case ("q"):
			message2[index]=translation["q"]
		case ("r"):
			message2[index]=translation["r"]
		case ("s"):
			message2[index]=translation["s"]
		case ("t"):
			message2[index]=translation["t"]
		case ("u"):
			message2[index]=translation["u"]
		case ("v"):
			message2[index]=translation["v"]
		case ("w"):
			message2[index]=translation["w"]
		case ("x"):
			message2[index]=translation["x"]
		case ("y"):
			message2[index]=translation["y"]
		case ("z"):
			message2[index]=translation["z"]
		case (". "):
			message2[index]=list(translation.keys())[list(translation.values()).index(". ")]
		case (".. "):
			message2[index]=list(translation.keys())[list(translation.values()).index(".. ")]
		case ("... "):
			message2[index]=list(translation.keys())[list(translation.values()).index("... ")]
		case (".... "):
			message2[index]=list(translation.keys())[list(translation.values()).index(".... ")]
		case (".- "):
			message2[index]=list(translation.keys())[list(translation.values()).index(".- ")]
		case (".-- "):
			message2[index]=list(translation.keys())[list(translation.values()).index(".-- ")]
		case (".--- "):
			message2[index]=list(translation.keys())[list(translation.values()).index(".--- ")]
		case ("..- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("..- ")]
		case (".--. "):
			message2[index]=list(translation.keys())[list(translation.values()).index(".--. ")]
		case (".-. "):
			message2[index]=list(translation.keys())[list(translation.values()).index(".-. ")]
		case ("- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("- ")]
		case ("-- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("-- ")]
		case ("--- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("--- ")]
		case ("--.. "):
			message2[index]=list(translation.keys())[list(translation.values()).index("--.. ")]
		case ("--. "):
			message2[index]=list(translation.keys())[list(translation.values()).index("--. ")]
		case ("-.- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("-.- ")]
		case ("--.- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("--.- ")]
		case ("..-. "):
			message2[index]=list(translation.keys())[list(translation.values()).index("..-. ")]
		case ("...- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("...- ")]
		case ("-.-- "):
			message2[index]=list(translation.keys())[list(translation.values()).index("-.-- ")]
		case (" "):
			message2[index]=translation[" "]
print(message2)
message3="".join(message2)
print(message3)
