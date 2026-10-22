deck=["1", 
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10", 
"10",
"10",
"10",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10", 
"10",
"10",
"10",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10", 
"10",
"10",
"10",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10",
"10",
"10",
"10"]
import random

item_moving=random.choice(deck)
dealers_hand=[item_moving]
dealers_hand=list(map(int, dealers_hand))
deck.remove(item_moving)
item_moving=random.choice(deck)
dealers_hand.append(item_moving)
dealers_hand=list(map(int, dealers_hand))
deck.remove(item_moving)

item_moving=random.choice(deck)
your_hand=[item_moving]
your_hand=list(map(int, your_hand))
deck.remove(item_moving)

print(f"the dealer has a {dealers_hand[0]} showing, you have a {your_hand}")
hand_total=sum(your_hand)
dealers_hand_total=sum(dealers_hand)
hit_stand="o"
busted=0

while hand_total<22 and hit_stand!="s":
	hit_stand=input(f"your hand total is {hand_total}, press h to hit, and s to stand:")
	if hit_stand=="h":
		item_moving=random.choice(deck)
		your_hand.append(item_moving)
		print(your_hand)
		your_hand=list(map(int, your_hand))
		deck.remove(item_moving)
		hand_total=sum(your_hand)
		if hand_total>21:
			print(f"you busted with a total of {hand_total}")
			busted=1
	elif hit_stand=="s":
		if 1 in your_hand and hand_total<12:
				hand_total+=10
		while dealers_hand_total<17:
			item_moving=random.choice(deck)
			dealers_hand.append(item_moving)
			print(dealers_hand)
			dealers_hand=list(map(int, dealers_hand))
			deck.remove(item_moving)
			dealers_hand_total=sum(dealers_hand)
			if "1" in dealers_hand and dealers_hand_total<12:
				dealers_hand_total+=10
			if dealers_hand_total>21:
				print(f"the dealer busted with a total of {dealers_hand_total}")
				busted=1

if busted!=1:
	print(f"the dealers hand was {dealers_hand}, totaling up to {dealers_hand_total}, and your_hand is {your_hand}, totaling up to {hand_total}. That means:")
	if hand_total>dealers_hand_total:
		print("your hand is better! You win!")
	elif dealers_hand_total>hand_total:
		print("your hand is worse, you lose. ):")
	elif dealers_hand_total==hand_total:
		print("your hands are equal, that's a push.")


