class LogParser:

	def __init__(self, file):
		self.file = file

	def getPlayerFromLastGame(self):
		f = open(self.file, 'r')
		lines = f.readlines()
		temp_lines = []
		last_game = ''
		players = []
		for item in lines:
			temp = str(item)
			if 'Lobby' in temp:
				temp_lines.append(temp)
		
		last_game = temp_lines[len(temp_lines)-1]
		a1 = last_game.split(':[U:1:')
		a2 = []
		for i in a1:
			i.split(']')
			a2.append(i)
		
		a3 = a2[1:-1]
		for i in a3:
			players.append(i[0:i.index(']')])
		f.close()
		return players