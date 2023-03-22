from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import PlayerProfileV2
from nba_api.stats.static import players

# Find players by full name.
players.find_players_by_full_name('james')

# Find players by first name.
lebron = players.find_players_by_first_name('lebron')

# Find players by last name.
players.find_players_by_last_name('^(james|love)$')

players.get_players()

# print(lebron)

##jokic player id
career = PlayerProfileV2(player_id='203999') 
# print(career)
df = career.get_data_frames()
# print(df[0])

df[0]['ppg'] = df[0]['PTS']/df[0]['GP']
df[0]['rpg'] = df[0]['REB']/df[0]['GP']
df[0]['apg'] = df[0]['AST']/df[0]['GP']
# print(df[0]['ppg'])
# print(df[0]['rpg'])
# print(df[0]['apg'])





####        In this secton of code, the goal is to get a name and a year

print("NBA Player and Year: ")
x = input()

nameAndYear = x.split(" ")

# print(nameAndYear)

name = " ".join(nameAndYear[0:2])

##print(name)

year = nameAndYear[2]

##print(year)
##     After we get a name and year, we want to get the player_id for that specific name




####        Name and year ------> player ID

# x = players.find_players_by_full_name('lebron james')

xTest = players.find_players_by_full_name(name)

# print(x[0].get("id"))
print(xTest[0].get("id"))



