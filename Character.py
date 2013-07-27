#Character
from random import randint
class Player():
	def __init__(self, job):
		self.job = job
		self.hitPoints = randint(10,20)
		self.gold = 0
		self.inventory = []
		
		#make stats more job specific later on
		self.strength = randint(10,20)
		self.dexterity = randint(10,20)
		self.intelligence = randint(10,20)
		self.magicPoints = 10 + intelligence