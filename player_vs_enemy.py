import random

#Made buffing happen less often. Fixed enemy damage being too high, and buffing being too much.
maximum_health=100
base_block=5
base_damage=8
base_heal=3
healing_multiplier=1
damage_multiplier=1
block_multiplier=1
enemy_number=0
block=0
enemy_random_damage=0
enemy_random_healing=0
enemy_random_block=0
enemy_pool=["angry worms angrier brother", "the mouse of despair", "friendly looking dog", "annoyed librarian", "strangely tall giraffe", "ferocious kitten", "cunning wizard", "cute little fire breathing dragon", "extremely snappy turtle", "fire elemental", "wierdly green sloth", "sleepy polar bear"]

exercising=0
penner_going=0
penner_multiplier=1
penner_count=0
extra_healing=0
battering_ram=0
defense_offense=0
spiked_shield=0
enemy_buffing=0
enemy_buffed_last_turn=0
crutches=0

turn_count=0
multiplier=0
option_chosen=0
starting_character=0
upgrade_options={"wall o' steel": "block x1.5", "vial of testosterone": "damage x1.5", "salt": "healing x1.5", "apple": "healing+1", "wooden shield": "block+2", "brick": "damage+3", "fruit plate": "maximum health+25", "exercise regimen": "-3 damage, +1 damage per turn", "penner nib": "every 10th attack does x3 damage", "weighted blanket": "end of fight healing +10", "battering ram": "decrease enemies block each turn by 5", "a good defense is a good offense": "block=1/2attack. overides all other block", "spiked shield": "whenever you full block, enemy loses 5hp", "crutches": "+5 damage while below 20% max hp"}

while starting_character!="1" and starting_character!="2":
	starting_character=input("choose a starting charecter. 1: Timothee. Timothee takes 1 less damage. 2: Angry worm. The angry worm does 2 extra damage, but blocks 1 less. 3: dr. doctor. You start with 25 more max hp")
match starting_character:
	case "1":
		relic_bar=["Timothee"]
	case "2":
		relic_bar=["Angry worm"]
		base_damage+=2
		base_block-=1
	case "3":
		relic_bar=["dr doctor"]
		maximum_health+=25
player_health=maximum_health

while enemy_number<10:
	
	enemy_strength=0
	turn_count=0
	exercising_gains=0
	relics=list(upgrade_options.keys())
	options=dict(random.sample(list(upgrade_options.items()), 3))
	relic_options=list(options.keys())
	
	while multiplier!="1" and multiplier!="2" and multiplier!="3":
		multiplier=(input(f"You beat enemy number {enemy_number}, which of these three upgrades would you like? {options}"))
	multiplier=int(multiplier)
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
			player_health+=25
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
		case "crutches":
			crutches=1
	
	enemy_number+=1
	enemy_health=25*(enemy_number)
	relic_bar.append(upgrade_options.pop(relic_options[multiplier-1]))
	current_enemy=random.choice(enemy_pool)
	enemy_pool.remove(current_enemy)
	
	multiplier=0
	
	print(f"A challenger approaches! It's {current_enemy}!")
	print(f"your health is: {player_health}")
	print(f"{current_enemy}'s health is: {enemy_health}\n")
	
	while player_health>0 and enemy_health>0:
		if turn_count%2==0:
			buffing_weight=50*(enemy_number/10)
			zero_three_list=[0, 1, 2, 3]
			attacking_weights=[(100-buffing_weight)/3, (100-buffing_weight)/3, (100-buffing_weight)/3, buffing_weight]
			if enemy_buffed_last_turn==0:
				enemy_doing=[random.choices(zero_three_list, weights=attacking_weights, k=1)[0], random.choices(zero_three_list, weights=attacking_weights, k=1)[0]]
			else:
				enemy_doing=[1, random.randint(0, 2)]
				enemy_buffed_last_turn=0
			match enemy_doing[0]:
				case 0:
					enemy_random_healing=random.randint(1+enemy_number, 3+enemy_number)
				case 1:
					enemy_random_damage=random.randint(1+enemy_number, 5+enemy_number)
				case 2:
					enemy_random_block=random.randint(1+enemy_number, 4+enemy_number)
				case 3:
					enemy_buffing+=1
					enemy_buffed_last_turn=1

			match enemy_doing[1]:
				case 0:
					enemy_random_healing+=random.randint(1+enemy_number, 3+enemy_number)
				case 1:
					enemy_random_damage+=random.randint(1+enemy_number, 5+enemy_number)
				case 2:
					enemy_random_block+=random.randint(1+enemy_number, 4+enemy_number)
				case 3:
					enemy_buffing+=1
					enemy_buffed_last_turn=1
			if enemy_random_damage>0:
				enemy_random_damage+=enemy_strength
			enemy_strength+=enemy_buffing*(1+int(enemy_number/4))

			if battering_ram==1:
				enemy_random_block-=5
				if enemy_random_block<0:
					enemy_random_block=0

			if exercising==1:
				exercising_gains=turn_count/2
			if crutches==1 and player_health<(maximum_health/5):
				attack_option=int((base_damage+exercising_gains+5)*damage_multiplier*penner_multiplier)
			else:
				attack_option=int((base_damage+exercising_gains)*damage_multiplier*penner_multiplier)
			block_option=int(base_block*block_multiplier)
			heal_option=int(base_heal*healing_multiplier)
			if defense_offense==1:
				block_option=int(attack_option/2)
			move_options=[f"block {block_option}", f"attack {attack_option}", f"heal {heal_option}"]

			print(f" enemy strength is: {enemy_strength}, random_damage is {enemy_random_damage}, enemy_buffing is {enemy_buffing} enemy_number is {enemy_number}")
			print(f"{current_enemy} is attacking for {enemy_random_damage} damage, blocking for {enemy_random_block}, healing for {enemy_random_healing} and buffing {enemy_buffing} times")
			enemy_buffing=0
			print(move_options)
			while option_chosen!="1" and option_chosen!="2" and option_chosen!="3":
				option_chosen=(input("choose one, two, or three:"))
			option_chosen=int(option_chosen)
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
				if relic_bar[0]=="Timothee":
					player_health+=1
			else:
				if spiked_shield==1 and enemy_random_damage>0:
					enemy_health-=5

			block=0
			enemy_random_damage=0
			enemy_random_healing=0
			
			print(f"your health is: {player_health}")
			print(f"{current_enemy}'s health is: {enemy_health}\n")
		turn_count+=1
	
	if player_health>0:
		player_health+=int(maximum_health/5+extra_healing)
	if player_health>maximum_health:
		player_health=maximum_health
	if player_health<1:
		enemy_number=10

if player_health>0:
	print("You slayed the beasts!")
else:
	print("You died.")