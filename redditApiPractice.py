import sunau
import praw


from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import PlayerProfileV2
from nba_api.stats.static import players




r = praw.Reddit('bot1')
subreddit = r.subreddit("nbadiscussion")



# for submission in subreddit.hot(limit=5):
# 	print("Title:", submission.title)
# 	print("Text:", submission.selftext)
# 	print("Score:", submission.score)
# 	print("---------------------------------\n")


from praw.models import MoreComments

identifer = "!nbastat"



url = "https://www.reddit.com/r/testingzz___zzzz_z/comments/11zx8ij/testtesttest/"

submission = r.submission(url = url)

calls = []
names = []

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    containsIdentifier= False
    print(comment.body)
    print("\n")
    if identifer in comment.body:
        calls.append(comment.body)
        commentArray = comment.body.split(" ")
        name = " ".join(commentArray[1:3])
        print(commentArray)
        print(name)
        xTest = players.find_players_by_full_name(name)
        playerId = xTest[0].get("id")
        print(playerId)
        career = PlayerProfileV2(player_id=playerId)
        # print(career)
        df = career.get_data_frames()
        print(df[0])
        df[0]['ppg'] = df[0]['PTS']/df[0]['GP']
        df[0]['rpg'] = df[0]['REB']/df[0]['GP']
        df[0]['apg'] = df[0]['AST']/df[0]['GP']
        print(df[0]['ppg'])
        print(df[0]['rpg'])
        print(df[0]['apg'])






