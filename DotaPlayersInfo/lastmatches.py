import urllib.request
import json

class LastMatches:

	def __init__(self, user_id):
		self.losses = 0
		self.wins = 0
		self.data = json.loads(urllib.request.urlopen(urllib.request.Request('https://api.opendota.com/api/players/{}/recentMatches'.format(user_id), headers={'User-Agent': 'Mozilla/5.0'})).read().decode())
		self.profile_info = json.loads(urllib.request.urlopen(urllib.request.Request('https://api.opendota.com/api/players/{}'.format(user_id), headers={'User-Agent': 'Mozilla/5.0'})).read().decode())
		with open('heroes.json') as f:
			self.heroes = json.load(f)['heroes']

	def getDetails(self):
		"""
			Get match detail
			returns:
			list(match_res)- contains Strings 'win' or 'lose'
			list(hero_name) - contains Strings hero name
		"""
		match_res = []
		hero_names = []

		for game in self.data:
			for hero in self.heroes:
				if game['hero_id'] == hero['id']:
					hero_names.append(hero['localized_name'])
	
			if game['radiant_win']:
				if game['player_slot'] <= 128:
					self.wins += 1
					match_res.append('WIN')
				else:
					self.losses += 1
					match_res.append('LOSE')
			else:
				if game['player_slot'] > 128:
					self.wins += 1
					match_res.append('WIN')
				else:
					self.losses += 1
					match_res.append('LOSE')

		return (match_res, hero_names)

	def getProfileName(self):
		"""Get profile name"""
		return self.profile_info['profile']['personaname']

	def getWins(self):
		"""Get wins count"""
		return self.wins
		
	def getLoses(self):
		"""Get losses count"""
		return self.losses