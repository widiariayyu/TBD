from pymongo import MongoClient
import re
MONGO_HOST = 'mongodb://localhost/'
MONGO_DB = 'db_new'

def get_json(collection_name):
    client = MongoClient(MONGO_HOST)
    db = client[MONGO_DB]
    collection = db[collection_name]
    return collection

def save_json(collection_name):
    client = MongoClient(MONGO_HOST)
    db = client["db_bersih"]
    collection = db[collection_name]
    return collection


def main(collection_name):
    # get json data from MongoDB
    data = get_json(collection_name)
    data_details = data.find()
    db = save_json(collection_name)
    tweetcon = 0
    # data_lower ={}
    # data_lower['text'] = i['text'].lower()
    key = ['slot', '#2019PilihJokowi','land','tanah', 'room', 'available','rent', 'sale', 'jual','tiktok', 'property','standbye','vasektomi','indihome',
                'expensive','astungkara','listrik','uwu','bengkel','sungai','furukawa','ambulan','plastik','sinyal','resort','hotel','cv','cosmetics','scrubs'
                'lowongan kerja','prabowo','pijat','jokowi','butter','skin','lotion','skin','sell','bengkuang','avocado','sandals','shop','#guesthouse',
                '#kontraktor','kontraktor','wax','arrival','soap','soap','soak','bath','pores','buy','open','selingan','store','property','belanja','pln','tiket',
           'apply','paket','tlpn','#zumbalovers','murah','ttd-nya','lentera']

    keyWords = []
    for i in range(1, len(key)):
        keyWords.append(key[i].lower())

    for i in data_details:
        data = {}
        if 'text' in i :
            text = i['text'].lower()
            print ("ada text")
        elif 'full_text' in i :
            text = i['full_text'].lower()


        if(text.find('tanah lot')) != -1 and (text.find('#bali')) != -1:

            tweetcon += 1
            data['created_at'] = i['created_at']
            data['id'] = i['id']
            data['text'] = text
            data['retweet_count'] = i['retweet_count']
            data['favorite_count'] = i['favorite_count']
            db.insert(data)


        elif (text.find('tanah lot'))!= -1 and (text.find('bali')) != -1 :

            tweetcon += 1
            data['created_at'] = i['created_at']
            data['id'] = i['id']
            data['text'] = text
            data['retweet_count'] = i['retweet_count']
            data['favorite_count'] = i['favorite_count']
            db.insert(data)
            print(data)


        elif (text.find('#tanahlot')) != -1 :

            tweetcon += 1
            data['created_at'] = i['created_at']
            data['id'] = i['id']
            data['text'] = text
            data['retweet_count'] = i['retweet_count']
            data['favorite_count'] = i['favorite_count']
            db.insert(data)


        # elif (text.find('batukaru')) != -1 and (text.find('gunung')) != -1 :
        #     val_t = re.sub(''.join(keyWords), "", text)
        #     print(val_t)
        #
        #     tweetcon += 1
        #     data['created_at'] = i['created_at']
        #     data['id'] = i['id']
        #     data['text'] = val_t
        #     data['retweet_count'] = i['retweet_count']
        #     data['favorite_count'] = i['favorite_count']
        #     db.insert(data)
        #
        # elif (text.find('#bedugul')) != -1 :
        #     val_t = re.findall(''.join(keyWords),"", text)
        #     print(val_t)
        #
        #     tweetcon += 1
        #     data['created_at'] = i['created_at']
        #     data['id'] = i['id']
        #     data['text'] = val_t
        #     data['retweet_count'] = i['retweet_count']
        #     data['favorite_count'] = i['favorite_count']
        #     db.insert(data)
        else:
            print('null')

    print(tweetcon)

if __name__ == "__main__":
    main("tanahlot")