import sunau
import praw


r = praw.Reddit('bot1')
subreddit = r.subreddit("nba")



# for submission in subreddit.hot(limit=5):
# 	print("Title:", submission.title)
# 	print("Text:", submission.selftext)
# 	print("Score:", submission.score)
# 	print("---------------------------------\n")


from praw.models import MoreComments

url = "https://www.reddit.com/r/nbadiscussion/comments/11x1rmo/can_a_below_average_center_still_get_meaningful/"

submission = r.submission(url = url)

submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    print(comment.body)
    print("\n")


