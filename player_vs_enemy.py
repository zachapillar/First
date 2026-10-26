import random


maximum_health=100
base_block=5
base_damage=8
base_heal=3
healing_multiplier=1
damage_multiplier=1
block_multiplier=1
enemy_number=1
block=0
enemy_random_damage=0
enemy_random_healing=0
enemy_random_block=0
enemy_options=["heal", "attack", "block"]
relic_bar=["bob"]

exercising=0
penner_going=0
penner_multiplier=1
penner_count=0
extra_healing=0
battering_ram=0
defense_offense=0
spiked_shield=0


player_health=100
enemy_health=30
turn_count=0
multiplier=0
option_chosen=0
upgrade_options={"wall o' steel": "block x1.5", "vial of testosterone": "damage x1.5", "salt": "healing x1.5", "apple": "healing+1", "wooden shield": "block+2", "brick": "damage+3", "fruit plate": "maximum health+25", "exercise regimen": "-3 damage, +1 damage per turn", "penner nib": "every 10th attack does x3 damage", "weighted blanket": "end of fight healing +10", "battering ram": "decrease enemies block each turn by 5", "a good defense is a good offense": "block=1/2attack. overides all other block", "spiked shield": "whenever you full block, enemy loses 5hp"}

while enemy_number<10:
	turn_count=0
	exercising_gains=0
	relics=list(upgrade_options.keys())
	options=dict(random.sample(list(upgrade_options.items()), 3))
	relic_options=list(options.keys())
	
	while multiplier!=1 and multiplier!=2 and multiplier!=3:
		multiplier=int(input(f"You beat enemy number {enemy_number-1}, which of these three upgrades would you like? {options}"))
	
	match relic_options[multiplier-1]:
		case "wall o' steel":
			block_multiplier*=1.5
		case "vial of testosterone":
			damage_multiplier*=1.5
		case "salt":
			healing_multiplier*=1.5
		case "apple":
			base_heal+=1
		case "wooden shield":
			base_block+=2
		case "brick":
			base_damage+=3
		case "fruit plate":
			maximum_health+=25
		case "exercise regimen":
			exercising=1
			base_damage-=3
		case "penner nib":
			penner_going=1
		case "weighted blanket":
			extra_healing=10
		case "battering ram":
			battering_ram=1
		case "a good defense is a good offense":
			defense_offense=1
		case "spiked shield":
			spiked_shield=1

	relic_bar.append(upgrade_options.pop(relic_options[multiplier-1]))
	print(relic_bar)
		
	multiplier=0
	
	while player_health>0 and enemy_health>0:
		if turn_count%2==0:
			enemy_doing=[random.randint(0, 2), random.randint(0, 2)]
			if enemy_doing[0]==0:
				enemy_random_healing=random.randint(1+enemy_number, 3+enemy_number)
			elif enemy_doing[0]==1:
				enemy_random_damage=random.randint(1+enemy_number, 5+enemy_number)
			elif enemy_doing[0]==2:
				enemy_random_block=random.randint(1+enemy_number, 4+enemy_number)

			if enemy_doing[1]==0:
				enemy_random_healing+=random.randint(1+enemy_number, 3+enemy_number)
			elif enemy_doing[1]==1:
				enemy_random_damage+=random.randint(1+enemy_number, 5+enemy_number)
			elif enemy_doing[1]==2:
				enemy_random_block+=random.randint(1+enemy_number, 4+enemy_number)
			enemy_doing=[3, 3]
			if battering_ram==1:
				enemy_random_block-=5
				if enemy_random_block<0:
					enemy_random_block=0

			if exercising==1:
				exercising_gains=turn_count/2
			block_option=int(base_block*block_multiplier)
			attack_option=int((base_damage+exercising_gains)*damage_multiplier*penner_multiplier)
			heal_option=int(base_heal*healing_multiplier)
			if defense_offense==1:
				block_option=int(attack_option/2)
			move_options=[f"block {block_option}", f"attack {attack_option}", f"heal {heal_option}"]

			print(f"the enemy is attacking for {enemy_random_damage} damage, blocking for {enemy_random_block}, and healing for {enemy_random_healing}")
			print(move_options)
			while option_chosen!=1 and option_chosen!=2 and option_chosen!=3:
				option_chosen=int(input("choose one, two, or three:"))
			if option_chosen==1:
				block=block_option
			elif option_chosen==2:
				if enemy_random_block<attack_option:
					enemy_health-=(attack_option-enemy_random_block)
					if penner_going==1:
						penner_count+=1
						penner_multiplier=1
						print(f"your penner nib is on {penner_count}")
						if penner_count==10:
							penner_count=0
							penner_multiplier=3
				else:
					if penner_going==1:
						penner_count+=1
						penner_multiplier=1
						print(f"your penner nib is on {penner_count}")
						if penner_count==10:
							penner_count=0
							penner_multiplier=3
			elif option_chosen==3:
				player_health+=heal_option
				if player_health>maximum_health:
					player_health=maximum_health
			
			enemy_random_block=0
			option_chosen=0
			if enemy_health<1:
				enemy_random_damage=0
				enemy_random_healing=0
		
		else:
			enemy_health+=enemy_random_healing
			if block<enemy_random_damage:
				player_health-=(enemy_random_damage-block)
			else:
				if spiked_shield==1 and enemy_random_damage>0:
					enemy_health-=5

			block=0
			enemy_random_damage=0
			enemy_random_healing=0
			
			print(f"your health is: {player_health}")
			print(f"enemy health is: {enemy_health}")
		turn_count+=1
	
	
	if player_health>0:
		player_health+=int(maximum_health/5+extra_healing)
	if player_health>maximum_health:
		player_health=maximum_health
	enemy_health=25*(enemy_number+1)
	if player_health<1:
		enemy_number=10
	enemy_number+=1

if player_health>0:
	print("You slayed the beasts!")
else:
	print("You died.")