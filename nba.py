from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import PlayerProfileV2
from nba_api.stats.static import players
import pandas



# # Find players by full name.
# players.find_players_by_full_name('james')

# # Find players by first name.
# lebron = players.find_players_by_first_name('lebron')

# # Find players by last name.
# players.find_players_by_last_name('^(james|love)$')

# players.get_players()

# print(lebron)

# ##jokic player id
# career = PlayerProfileV2(player_id='203999') 
# # print(career)
# df = career.get_data_frames()
# # print(df[0])

# df[0]['ppg'] = df[0]['PTS']/df[0]['GP']
# df[0]['rpg'] = df[0]['REB']/df[0]['GP']
# df[0]['apg'] = df[0]['AST']/df[0]['GP']
# # print(df[0]['ppg'])
# # print(df[0]['rpg'])
# # print(df[0]['apg'])





####        In this secton of code, the goal is to get a name and a year

print("NBA Player and Year: ")
x = input()

nameAndYear = x.split(" ")

# print(nameAndYear)

name = " ".join(nameAndYear[0:2])

seasonId = [nameAndYear[2]]

print(seasonId)

##print(name)

year = nameAndYear[2]

##print(year)
##     After we get a name and year, we want to get the player_id for that specific name




####        Name and year ------> player ID

# x = players.find_players_by_full_name('lebron james')

xTest = players.find_players_by_full_name(name)

# print(x[0].get("id"))
print(xTest[0].get("id"))

inputID = xTest[0].get("id")


inputCareer = PlayerProfileV2(player_id=inputID) 
inputDF = inputCareer.get_data_frames()

print(type(inputDF[0].dtypes))

input_DF_regular_season = inputDF[0]

print(input_DF_regular_season)

input_DF_regular_season['SEASON_ID'] = input_DF_regular_season['SEASON_ID'].astype(pandas.StringDtype())


print(input_DF_regular_season.dtypes)
print(seasonId)

dfByYear = input_DF_regular_season[input_DF_regular_season['SEASON_ID'].str.contains(seasonId[0])]
print(dfByYear)

# print(dfByYear)

dfByYear['ppg'] = dfByYear['PTS']/dfByYear['GP']
dfByYear['rpg'] = dfByYear['REB']/dfByYear['GP']
dfByYear['apg'] = dfByYear['AST']/dfByYear['GP']


print(str(round(dfByYear['ppg'], 2)))
print(str(round(dfByYear['rpg'], 2)))
print(str(round(dfByYear['apg'], 2)))