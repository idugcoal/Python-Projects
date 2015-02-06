import nflgame

class Team(object):
	def __init__(self, name):
		self.name = name
	def display(self):
		print self.name
	def getName(self):
		return self.name

def main():
	teams = nflgame.teams
	nfl = []
	
	for team in teams:
			tmp = Team(team[0])
			tmp.display()
			nfl.append(tmp)

	for team in nfl:
		games = nflgame.games(2013, home=team.getName(), away=team.getName())
		for game in games:
			print game.nice_score()

if __name__ == "__main__":
	main()