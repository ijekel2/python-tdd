
##
## This is a class that models a tennis game.
class TennisGame(object):
	
	def __init__(self, player1Name, player2Name):
		self.player1Name = player1Name
		self.player2Name = player2Name
		self.player1Score = 0
		self.player2Score = 0
		self.translations = {
			0: "love",
			1: "fifteen",
			2: "thirty",
			3: "forty"
		}
	
	## These methods add a point to a player's score.
	def player1ScoresAPoint(self):
		self.player1Score +=1
	
	def player2ScoresAPoint(self):
		self.player2Score +=1
	
	## These are boolean methods to test for certain game scenarios
	def isDeuce(self):
		if(self.player1Score >= 3 and self.player1Score == self.player2Score):
			return True
		else:
			return False
	
	def player1HasAdvantage(self):
		if(self.player1Score >= 4 and (self.player1Score - 1) == self.player2Score):
			return True
		else:
			return False
			
	def player2HasAdvantage(self):
		if(self.player2Score >= 4 and (self.player2Score - 1) == self.player1Score):
			return True
		else:
			return False
			
	def player1Wins(self):
		if(self.player1Score >= 3 and self.player1Score > self.player2Score):
			return True
		else:
			return False
	
	def player2Wins(self):
		if(self.player2Score >= 3 and self.player2Score > self.player1Score):
			return True
		else:
			return False
			
	def isTied(self):
		if(self.player1Score == self.player2Score):
			return True
		else:
			return False
		
	## This method returns the current score of the game.
	def getScore(self):
	
		if(self.isDeuce()):
			return "deuce"
			
		elif(self.player1HasAdvantage()):
			return "advantage, " + self.player1Name
		
		elif(self.player2HasAdvantage()):
			return "advantage, " + self.player2Name	
		
		elif(self.player1Wins()):
			return self.player1Name + " wins!"
		
		elif(self.player2Wins()):
			return self.player2Name + " wins!"
			
		elif(self.isTied()):
			return self.translations.get(self.player1Score) + " all"
			
		else:
			return self.translations.get(self.player1Score) + ", " + self.translations.get(self.player2Score)


##
## This class has testing methods for the TennisGame class. 
class TestTennisGame(object):

	def __init__(self):
		self.game1 = TennisGame("Federer", "Nadal")
		self.game2 = TennisGame("Del Potro", "Djokovic")
		
	def assertEqual(self, a, b):
		if(a != b):
			print("Test Failed. Expected: " + str(a) + " but found: " + str(b))
		else:
			print(".")
		
	## These are the tests for the first game where player 1 wins.
	def testNewGameScore(self):
		self.assertEqual("love all", self.game1.getScore())

	def testPlayer1ScoresFirstPoint(self):
		self.game1.player1ScoresAPoint()
		self.assertEqual("fifteen, love", self.game1.getScore())
	
	def testPlayer2TiesTheGame(self):
		self.game1.player2ScoresAPoint()
		self.assertEqual("fifteen all", self.game1.getScore())
		
	def testDeuce(self):
		self.game1.player1ScoresAPoint()
		self.game1.player1ScoresAPoint()
		self.game1.player2ScoresAPoint()
		self.game1.player2ScoresAPoint()
		self.assertEqual("deuce", self.game1.getScore())
		
	def testPlayer2GainsAdvantage(self):
		self.game1.player2ScoresAPoint()
		self.assertEqual("advantage, Nadal", self.game1.getScore())
	
	def testPlayer1GainsAdvantage(self):
		self.game1.player1ScoresAPoint()
		self.game1.player1ScoresAPoint()
		self.assertEqual("advantage, Federer", self.game1.getScore())
	
	def testPlayer1Wins(self):
		self.game1.player1ScoresAPoint()
		self.assertEqual("Federer wins!", self.game1.getScore())
	
	## These are the tests for the second game where player 2 wins.
	def testPlayer2ScoresFirstPoint(self):
		self.game2.player2ScoresAPoint()
		self.assertEqual("love, fifteen", self.game2.getScore())
	
	def testPlayer2Wins(self):
		self.game2.player2ScoresAPoint()
		self.game2.player2ScoresAPoint()
		self.game2.player2ScoresAPoint()
		self.assertEqual("Djokovic wins!", self.game2.getScore())



##
## This code runs the tests from the TestTennisGame class. 
test = TestTennisGame()

## This is the first test game where player 1 wins.
test.testNewGameScore()
test.testPlayer1ScoresFirstPoint()
test.testPlayer2TiesTheGame()
test.testDeuce()
test.testPlayer2GainsAdvantage()
test.testPlayer1GainsAdvantage()
test.testPlayer1Wins()

## THis is the second test game where player 2 wins.
test.testPlayer2ScoresFirstPoint()
test.testPlayer2Wins()




