import json
import tweepy
import time

# print('Tweepy Rocks!!!')

CONSUMER_KEY = 'BgUagDjg64h8kxdXq8t2M5DFA'
CONSUMER_SECRET = 'bY99cvGfcrrkvFmFIuQgESGoYzO9SQ1iAs4AeQw8Kee2F6fQjX'
ACCESS_KEY = '752093014160465920-5jew3zhIOtkJ2KBCDqgoTtjdSHAzcm3'
ACCESS_SECRET = 'OIrAvdKjQu3c9rj344pNl1Oc4HqH2LTjdUuuKDscMH6IY'
bearer_token = r'AAAAAAAAAAAAAAAAAAAAAFOxfgEAAAAAAHKYLhGDb1pKWAXNAEY5OkF%2FNxY%3DKkNu5gjt3lJM67nVH5Lh5FSqDkdOhG9tcW6AErhC7p8v8YjC5R'




#method for mentions
# mentions = api.mentions_timeline()

# for mention in mentions:
#     print(f"{str(mention.id)}: {mention.text}")
#     if '#helloworld' in mention.text.lower():
#         print('found #helloworld')
#         print('responding back...')
#         api.update_status(f"{'@'} {mention.user.screen_name} #Helloworld back to you.")


#method for user timelines
# timeline = api.home_timeline()

# for tweet in timeline:
#     print(f"{tweet.user.name} said {tweet.text}")

# api.update_status("Test tweet from Tweepy Python")

# user = api.get_user(screen_name="dorothy_muhonja")
# print('User details:')
# print(user.name)
# print(user.description)
# print(user.location)


# method for followers
# print('last 20 followers:')
# for follower in user.followers():
#     print(follower.name)


# api.create_friendship(screen_name='realpython')

# updating profile
# api.update_profile(description='Just your everyday human')

#method for likes(marking most recent tweet as liked)
# tweets = api.home_timeline(count=1)
# tweet = tweets[0]
# print(f"Liked tweet {tweet.id} of {tweet.author.name}")
# api.create_favorite(tweet.id)

# method for seeing blocked users
# for block in api.get_blocked_ids():
#     print(block.name)

# search methods
# for tweet in api.search_tweets(q="Python",lang="en", count=10):
#     print(f"{tweet.user.name}:{tweet.text}")

# trend methods
# trend_result = api.get_place_trends(1)

# for trend in trend_result[0]["trends"]:
#     print(trend["name"])

# streaming method
search_terms = ["python", "programming", "coding"]

class MyStreamClient(tweepy.StreamingClient):

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)


#authenticate to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#creating API object
api = tweepy.API(auth)

stream = MyStreamClient(bearer_token=bearer_token)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=["referenced_tweets"])


