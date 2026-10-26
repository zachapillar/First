import random


maximum_health=100
base_block=5
base_damage=8
base_heal=3
healing_multiplier=1
damage_multiplier=1
block_multiplier=1
block_option=int(base_block*block_multiplier)
attack_option=int(base_damage*damage_multiplier)
heal_option=int(base_heal*healing_multiplier)
enemy_number=1
block=0
enemy_random_damage=0
enemy_random_healing=0
enemy_random_block=0
enemy_options=["heal", "attack", "block"]
enemy_doing=[random.randint(0, 2), random.randint(0, 2)]

if enemy_doing[0]==0:
	enemy_random_healing=random.randint(1+enemy_number, 4+enemy_number)
elif enemy_doing[0]==1:
	enemy_random_damage=random.randint(1+enemy_number, 6+enemy_number)
elif enemy_doing[0]==2:
	enemy_random_block=random.randint(1+enemy_number, 5+enemy_number)

if enemy_doing[1]==0:
	enemy_random_healing+=random.randint(1+enemy_number, 4+enemy_number)
elif enemy_doing[1]==1:
	enemy_random_damage+=random.randint(1+enemy_number, 6+enemy_number)
elif enemy_doing[1]==2:
	enemy_random_block+=random.randint(1+enemy_number, 5+enemy_number)


player_health=100
enemy_health=30
turn_count=0
multiplier=0
option_chosen=0
move_options=[f"block {block_option}", f"attack {attack_option}", f"heal {heal_option}"]


while enemy_number<10:
	option1, option2, option3 = random.sample(range(0, 7), 3)
	print(option1, option2, option3)
	options=(option1, option2, option3)
	upgrade_options=["block x1.5", "damage x1.5", "healing*1.5", "healing+1", "block+2", "damage+3", "maximum_health+10"]

	while multiplier!=1 and multiplier!=2 and multiplier!=3:
		multiplier=int(input(f"You beat enemy number {enemy_number-1}, which of these three upgrades would you like? {upgrade_options[option1]}, {upgrade_options[option2]}, or {upgrade_options[option3]}"))
	if multiplier==1:
		if option1==0:
			block_multiplier*=1.5
		elif option1==1:
			damage_multiplier*=1.5
		elif option1==2:
			healing_multiplier*=1.5
		elif option1==3:
			base_heal+=1
		elif option1==4:
			base_block+=2
		elif option1==5:
			base_damage+=3
		elif option1==6:
			maximum_health+=10
	if multiplier==2:
		if option2==0:
			block_multiplier*=1.5
		elif option2==1:
			damage_multiplier*=1.5
		elif option2==2:
			healing_multiplier*=1.5
		elif option2==3:
			base_heal+=1
		elif option2==4:
			base_block+=2
		elif option2==5:
			base_damage+=3
		elif option2==6:
			maximum_health+=10
	if multiplier==3:
		if option3==0:
			block_multiplier*=1.5
		elif option3==1:
			damage_multiplier*=1.5
		elif option3==2:
			healing_multiplier*=1.5
		elif option3==3:
			base_heal+=1
		elif option3==4:
			base_block+=2
		elif option3==5:
			base_damage+=3
		elif option3==6:
			maximum_health+=10
		
	block_option=int(base_block*block_multiplier)
	attack_option=int(base_damage*damage_multiplier)
	heal_option=int(base_heal*healing_multiplier)
	multiplier=0
	move_options=[f"block {block_option}", f"attack {attack_option}", f"heal {heal_option}"]

	while player_health>0 and enemy_health>0:
		if turn_count%2==0:
			print(f"the enemy is attacking for {enemy_random_damage} damage, blocking for {enemy_random_block}, and healing for {enemy_random_healing}")
			print(move_options)
			while option_chosen!=1 and option_chosen!=2 and option_chosen!=3:
				option_chosen=int(input("choose one, two, or three:"))
			if option_chosen==1:
				block=block_option
			elif option_chosen==2:
				if enemy_random_block<attack_option:
					enemy_health-=(attack_option-enemy_random_block)
				else:
					pass
			elif option_chosen==3:
				player_health+=heal_option
				if player_health>maximum_health:
					player_health=maximum_health
			
			enemy_random_block=0
			option_chosen=0
		
		else:
			enemy_health+=enemy_random_healing
			if block<enemy_random_damage:
				player_health-=(enemy_random_damage-block)
			else:
				pass

			block=0
			enemy_random_damage=0
			enemy_random_healing=0
			enemy_doing=[random.randint(0, 2), random.randint(0, 2)]
			
			if enemy_doing[0]==0:
				enemy_random_healing=random.randint(1+enemy_number, 4+enemy_number)
			elif enemy_doing[0]==1:
				enemy_random_damage=random.randint(1+enemy_number, 6+enemy_number)
			elif enemy_doing[0]==2:
				enemy_random_block=random.randint(1+enemy_number, 5+enemy_number)

			if enemy_doing[1]==0:
				enemy_random_healing+=random.randint(1+enemy_number, 4+enemy_number)
			elif enemy_doing[1]==1:
				enemy_random_damage+=random.randint(1+enemy_number, 6+enemy_number)
			elif enemy_doing[1]==2:
				enemy_random_block+=random.randint(1+enemy_number, 5+enemy_number)

			print(f"your health is: {player_health}")
			print(f"enemy health is: {enemy_health}")
		turn_count+=1
	
	
	if player_health>0:
		player_health+=100
	if player_health>maximum_health:
		player_health=maximum_health
	enemy_health=30*enemy_number
	if player_health<1:
		enemy_number=10
	enemy_number+=1

if player_health>0:
	print("You slayed the beast!")
else:
	print("You died.")