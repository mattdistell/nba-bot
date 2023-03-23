import sunau
import praw


r = praw.Reddit('bot1')
subreddit = r.subreddit("nbadiscussion")



# for submission in subreddit.hot(limit=5):
# 	print("Title:", submission.title)
# 	print("Text:", submission.selftext)
# 	print("Score:", submission.score)
# 	print("---------------------------------\n")


from praw.models import MoreComments

url = "https://www.reddit.com/r/testingzz___zzzz_z/comments/11zx8ij/testtesttest/"

submission = r.submission(url = url)

submission.comments.replace_more(limit=None)
# for comment in submission.comments.list():
#     print(comment.body)
#     print("\n")


submission.reply("test comment pt 2.")