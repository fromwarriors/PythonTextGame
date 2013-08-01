#Character
from random import randint
class Player():
	def __init__(self, job):
		self.job = job
		self.hitPoints = randint(21,30)
		self.gold = 0
		self.inventory = []
		
		#make stats more job specific later on
		self.strength = randint(5,10)
		self.dexterity = randint(5,10)
		self.intelligence = randint(5,10)
		self.magicPoints = 5 + self.intelligence
		
		#map
		self.userMap = [["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"]]

	
#Dungeons and dragons mechanics	

#Roll an initial die to see if you can get the attack off then roll for damage
	def attack(self, monsterDexterity, monsterArmor):
		initialRoll = randint(0,20)
		rollToHit = initialRoll + self.dexterity
		critical = false
		if(initialRoll = 20):
			critical = true
		if(rollToHit >= monsterDexterity):
			#If hit commence damage sequence
			if(critical == true):
				return randint(0,6) + randint(0,6) + self.strength - monsterArmor
			else:
				return randint(0,6) + self.strength - monsterArmor
		else:
			print "Missed!"
			return 0
	
#Check the current position if its a valid move, if it is then mark the map where the character currently is and update the map where the 
#character has been and return new position	

	#direction is 'n','w','s','e'
	#position is a tuple row, column
	def move(self, direction, position):
		canMove = True
		if(direction == 'w'):
			if(c == 0):
				canMove = False
			else:
				
	
			
	def newFloor(self):
		self.userMap = [["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"]]

		
	def displayMap(self):
		for i in range(0,4):
			print self.userMap[i]
			print "\n"