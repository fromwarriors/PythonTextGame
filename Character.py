#Character
from random import randint
class Player():
	def __init__(self, job):
		self.job = job
		self.hitPoints = randint(21,30)
		self.gold = 0
		self.inventory = []
		
		#make stats more job specific later on
		self.strength = randint(10,20)
		self.dexterity = randint(5,10)
		self.intelligence = randint(5,10)
		self.magicPoints = 5 + self.intelligence