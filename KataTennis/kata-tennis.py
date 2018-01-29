# Here we define a simple assertEqual method.




# Here is the code for the Tennis game.
class TennisGame(object):
	
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.p1GameScore = 0
		self.p2GameScore = 0
		self.p1SetScore = 0
		self.p2SetScore = 0
		self.p1Serve = True
	
	def getGameScore(self):
		
		scores = {
			0: "love",
			1: "fifteen",
			2: "thirty",
			3: "forty"
		}
		
		if self.p1GameScore == self.p1GameScore:
			if self.p1GameScore >= 4:
				return "deuce"
			else:
				return scores.get(self.p1GameScore) + " all"
		
	def getSetScore(self):
		return str(self.p1SetScore) + " - " + str(self.p2SetScore)


# Here are the game tests. 
class TestTennisGame(object):

	def __init__(self):
		self.game = TennisGame("Federer", "Nadal")
		
	def assertEqual(a, b):
    	if(a != b):
        	print("Test Failed. Expected: " + str(a) + " but found: " + str(b))
    	else:
        	print(".")
		
	def testNewGameScore():
		assertEqual(game.getGameScore(), "love all")
		assertEqual(game.getSetScore(), "0 - 0")
	
	def testFirstPoint():
		asser

# This is the code to run the tests

