import random

block=0
boss_random_damage=0
boss_random_healing=0
boss_random_block=0
boss_options=["heal", "attack", "block"]
boss_doing=[random.randint(0, 2), random.randint(0, 2)]

if boss_doing[0]==0:
	boss_random_healing=random.randint(3, 6)
elif boss_doing[0]==1:
	boss_random_damage=random.randint(3, 13)
elif boss_doing[0]==2:
	boss_random_block=random.randint(4, 8)

if boss_doing[1]==0:
	boss_random_healing+=random.randint(3, 6)
elif boss_doing[1]==1:
	boss_random_damage+=random.randint(3, 13)
elif boss_doing[1]==2:
	boss_random_block+=random.randint(4, 8)

player_health=100
boss_health=200
turn_count=0
move_options=["block 10", "attack 15", "heal 5"]

while player_health>0 and boss_health>0:
	if turn_count%2==0:
		print(f"the boss is attacking for {boss_random_damage} damage, blocking for {boss_random_block}, and healing for {boss_random_healing}")
		print(move_options)
		option_chosen=int(input("choose one, two, or three:"))
		if option_chosen==1:
			block=10
		elif option_chosen==2:
			if boss_random_block<15:
				boss_health-=(15-boss_random_block)
			else:
				pass
		elif option_chosen==3:
			player_health+=5
		
		boss_random_block=0
	
	else:
		boss_health+=boss_random_healing
		if block<boss_random_damage:
			player_health-=(boss_random_damage-block)
		else:
			pass

		block=0
		boss_random_damage=0
		boss_random_healing=0
		boss_doing=[random.randint(0, 2), random.randint(0, 2)]
		
		if boss_doing[0]==0:
			boss_random_healing=random.randint(3, 6)
		elif boss_doing[0]==1:
			boss_random_damage=random.randint(3, 13)
		elif boss_doing[0]==2:
			boss_random_block=random.randint(4, 8)

		if boss_doing[1]==0:
			boss_random_healing+=random.randint(3, 6)
		elif boss_doing[1]==1:
			boss_random_damage+=random.randint(3, 13)
		elif boss_doing[1]==2:
			boss_random_block+=random.randint(4, 8)
		

		print(player_health)
		print(boss_health)
	
	turn_count+=1


if player_health>0:
	print("You slayed the beast!")
else:
	print("You died.")