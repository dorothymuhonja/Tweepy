import json
import tweepy
import time

# print('Tweepy Rocks!!!')

# replace none with your twitter keys and tokens
CONSUMER_KEY = 'None'
CONSUMER_SECRET = 'None'
ACCESS_KEY = 'None'
ACCESS_SECRET = 'None'
bearer_token = r'None'

#authenticate to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#creating API object
api = tweepy.API(auth)


#method for mentions
mentions = api.mentions_timeline()

for mention in mentions:
    print(f"{str(mention.id)}: {mention.text}")
    if '#helloworld' in mention.text.lower():
        print('found #helloworld')
        print('responding back...')
        api.update_status(f"{'@'} {mention.user.screen_name} #Helloworld back to you.")


#method for user timelines
timeline = api.home_timeline()

for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

api.update_status("Test tweet from Tweepy Python")

user = api.get_user(screen_name="dorothy_muhonja")
print('User details:')
print(user.name)
print(user.description)
print(user.location)


# method for followers
print('last 20 followers:')
for follower in user.followers():
    print(follower.name)


api.create_friendship(screen_name='realpython')

# updating profile
api.update_profile(description='Just your everyday human')

#method for likes(marking most recent tweet as liked)
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liked tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)

# method for seeing blocked users
for block in api.get_blocked_ids():
    print(block.name)

# search methods
for tweet in api.search_tweets(q="Python",lang="en", count=10):
    print(f"{tweet.user.name}:{tweet.text}")

# trend methods
trend_result = api.get_place_trends(1)

for trend in trend_result[0]["trends"]:
    print(trend["name"])

# streaming method
search_terms = ["python", "programming", "coding"]

class MyStreamClient(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)


stream = MyStreamClient(bearer_token=bearer_token)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])

tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite()
    tweet.user.follow()

# This code shows how, by using a cursor, you can get not only the first page from your timeline, but also the last 100 tweets:
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said {tweet.text}")


