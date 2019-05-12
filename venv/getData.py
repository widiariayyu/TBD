import tweepy
import json
import datetime
import requests
import time


def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        main()

    except requests.ConnectionError:
        print("no internet connection wait for 1 second")
        time.sleep(1)
        check_internet()


def print_to_json(city, data, urutan):
    file = "json/%s_%d.txt" %(city,urutan)
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def main():
    consumer_key = 'JcNZJOVGAJss79kj7zbsJxenT'
    consumer_secret = 'r5RmPPco1Il1cyR3X9zK8X8vZfj7GFGOoEW8LLc9zjeV7CvJJK'
    access_token = '773408577759408128-Kqt5lVCDZg8Fvd8xjOEBVrg7jg2qmfQ'
    access_token_secret = 'P88vafPYYjaoEkeQlTYNz6yWk26pdExcyfuiOWEXNAZ0V'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    cities = ['sangeh']
    count = 0

    for city in cities:
        data = []
        counter = 0
        urutan = 1
        try:
            for status in tweepy.Cursor(api.search, q=city, since='2019-03-08', until='2019-03-15').items():
                # Process a single status
                x = status
                data.append(x._json)
                counter = counter+1
                count = count + 1
                print(count)
                if counter == 2000:
                    print("Urutan = %d"%urutan)
                    print_to_json(city, data, urutan)
                    data = []
                    counter = 0
                    urutan = urutan + 1
            print("Urutan = %d" % urutan)
            print_to_json(city, data, urutan)

        except:
            print("something run not right")
            print("re running...")
            time.sleep(1)

if __name__ == "__main__":
    check_internet()





# for city in cities:
#     data = {}
#     counter = 0
#     for status in tweepy.Cursor(api.search, city).items():
#         x = status
#         id = x.id
#         text = x.text
#
#         if x.user.location != "":
#             location = x.user.location
#         else:
#             location = "null"
#
#         data[counter] = {}
#         data[counter]["id"] = id
#         data[counter]["created_at"] = str(x.created_at)
#         data[counter]["text"] = text
#         data[counter]["location"] = location
#         counter = counter + 1
#         print(counter)
#
#     print_to_json(city, data, 1)