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
	
#Dungeons and dragons mechanics	
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