#Floor
#Each floor should hold a grid that's dynamically set every time the floor is initialized and a map that is updated whenever a player changes tiles 

#The generatedMap will hold the information the was made when the floor initialized and the user map will contain x's letting the user know where they've
#already been

#Move set 1-4 = first row 5-8 = second row 9-12 = third row 12-15 = fourth row
class Floor(object):
	generatedMap = 0
	userMap = 0
	mounsterCount = 0
	floorNumber = 0
	def __init__(self, floorNumber):
		#Map setup
		self.generatedMap = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
		self.userMap = [["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"],["[ ]", "[ ]", "[ ]", "[ ]"]]
		
		if(floorNumber == 1):
			monsterCount = 2
	
#	def generateMonsters(self):

	def displayMap(self):
		for i in range(0,4):
			print self.userMap[i]
			print "\n"