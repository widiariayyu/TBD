import pandas
import tweepy
import jsonpickle
import time
from pymongo import MongoClient
import datetime

#consumer
CONSUMER_KEY = 'JcNZJOVGAJss79kj7zbsJxenT'
CONSUMER_SECRET = 'r5RmPPco1Il1cyR3X9zK8X8vZfj7GFGOoEW8LLc9zjeV7CvJJK'

#token
ACCESS_TOKEN = '773408577759408128-Kqt5lVCDZg8Fvd8xjOEBVrg7jg2qmfQ'
ACCESS_SECRET = 'P88vafPYYjaoEkeQlTYNz6yWk26pdExcyfuiOWEXNAZ0V'

#host mongo
MONGO_HOST = 'mongodb://localhost/'

#API setup
def twitter_auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit_notify=False, wait_on_rate_limit=False, retry_count=5, retry_delay=5)
    print('auth success')
    return api

#limit handler
def limit_handled(cursor):
    backoff_counter = 1
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(60 * backoff_counter)
            backoff_counter += 1
            continue

#get tweet
def get_tweet(db, collection_name, filepath, api, query, max_tweets):

    collection = db[collection_name]

    tweetCount = 0

    with open("./json/"+filepath, 'a+') as f:
        for tweet in limit_handled(tweepy.Cursor(api.search, q=query, since="2019-4-28", until="2019-5-7", tweet_mode='extended').items(max_tweets)):
            if ('sale dijual' not in tweet.full_text) and ('room' not in tweet.full_text):
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                #json.dump(tweet._json, f, indent=2)

                collection.insert(tweet._json)

                tweetCount += 1
                print("Query = {}. Downloaded {} tweets".format(query, tweetCount))

#MAIN
def main():
    #call twitter_auth()
    api = twitter_auth()

    #connect mongodb
    client = MongoClient(MONGO_HOST)
    db = client.db_new

    #read query.txt
    file_query = open("test.txt", "r")
    for i in file_query:
        JSON_DATA = {}
        date_now = datetime.datetime.now()
        query = i.split(",")
        collection_name = query[0]
        collection_name = collection_name.replace('"', '')
        path = (collection_name.rstrip()) + '_{}_{}-{}-{}-{}.json'.format(datetime.date.today(),
                                                                   date_now.hour,
                                                                   date_now.minute,
                                                                   date_now.second,
                                                                   date_now.microsecond)
        for q in query:
            print(q)
            get_tweet(db, collection_name, path, api, q, 1000000)


if __name__ == "__main__":
    main()
