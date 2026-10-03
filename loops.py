first=input("'sup:")
seconds=list(first)
for index, second in enumerate(seconds):
	match second:
		# Match strings that start with "green_" using a guard clause
		case str() as s if s.startswith("a"):
			seconds[index]="z"
		case str() as s if s.startswith("b"):
			seconds[index]="a"
		case str() as s if s.startswith("c"):
			seconds[index]="b"
		case str() as s if s.startswith("d"):
			seconds[index]="c"
		case str() as s if s.startswith("e"):
			seconds[index]="d"
		case str() as s if s.startswith("f"):
			seconds[index]="e"
		case str() as s if s.startswith("g"):
			seconds[index]="f"
		case str() as s if s.startswith("h"):
			seconds[index]="g"
		case str() as s if s.startswith("i"):
			seconds[index]="h"
		case str() as s if s.startswith("j"):
			seconds[index]="i"
		case str() as s if s.startswith("k"):
			seconds[index]="j"
		case str() as s if s.startswith("l"):
			seconds[index]="k"
		case str() as s if s.startswith("m"):
			seconds[index]="l"
		case str() as s if s.startswith("n"):
			seconds[index]="m"
		case str() as s if s.startswith("o"):
			seconds[index]="n"
		case str() as s if s.startswith("p"):
			seconds[index]="o"
		case str() as s if s.startswith("q"):
			seconds[index]="p"
		case str() as s if s.startswith("r"):
			seconds[index]="q"
		case str() as s if s.startswith("s"):
			seconds[index]="r"
		case str() as s if s.startswith("t"):
			seconds[index]="s"
		case str() as s if s.startswith("u"):
			seconds[index]="t"
		case str() as s if s.startswith("v"):
			seconds[index]="u"
		case str() as s if s.startswith("w"):
			seconds[index]="v"
		case str() as s if s.startswith("x"):
			seconds[index]="w"
		case str() as s if s.startswith("y"):
			seconds[index]="x"
		case str() as s if s.startswith("z"):
			seconds[index]="y"
		case _: 
			print("error")
message = "".join(seconds)
print(message)
