#Floor
#Each floor should hold a grid that's dynamically set every time the floor is initialized and a map that is updated whenever a player changes tiles 

#The generatedMap will hold the information the was made when the floor initialized and the user map will contain x's letting the user know where they've
#already been

#Move set 1-4 = first row 5-8 = second row 9-12 = third row 12-15 = fourth row
from random import randint
from Character import Player # unused

class Floor(object):
#	PROPERTIES
#	generatedMap
#	userMap
#	mounsterCount
#	floorNumber

    def __init__(self, floorNumber, character):
        #Map setup
        self.generatedMap = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        self.floorNumber = floorNumber
        if(floorNumber == 1):
            self.monsterCount = 2
        
        #monster placement
        for i in range (0, self.monsterCount):
            row = randint(0,4)
            column = randint(0,4)
            while(self.generatedMap[row][column] == column):
                row = randint(0,4)
                column = randint(0,4)
            self.generatedMap[row][column] = 'M'
        
        
