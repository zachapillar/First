score=0
import time
start=time.time()

while score<10:
	bob=input("Go:")
	match bob:
		case a:
			score=score+1
end=time.time()
total=end-start
print(f"Script execution time: {total:.2f} seconds")