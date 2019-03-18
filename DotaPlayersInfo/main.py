import urllib.request
import json
import lastmatches
import time
import serverlogparser

# ids = ['80002028', '244766885', '389964937', '102436499',
# 	   '240422235', '150165364', '363408127', '80815314',
# 	   '59859011', '114470818']
path = 'C:/Program Files (x86)/Steam/steamapps/common/dota 2 beta/game/dota/server_log.txt'
ids = serverlogparser.LogParser(path).getPlayerFromLastGame()

print('starting...')
for user_id in ids:
	player = lastmatches.LastMatches(user_id)
	mr, hn = player.getDetails()
	print('profile name: {}'.format(player.getProfileName()))
	for i in range(0, len(hn)):
		if len(hn[i]) < 19:
			while len(hn[i]) < 19:
				hn[i] += " "
		print('   ', hn[i], ' | ', mr[i])
		time.sleep(.007)
	print()
	print('WINS: {0} | LOSSES: {1}'.format(player.getWins(), player.getLoses()), )
	print('----------------------------------------------------------------------')
	if not ids.index(user_id) == len(ids)-1:
		print('processing...')
	print()
print('end')
input()
