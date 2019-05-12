from pymongo import MongoClient
import re
MONGO_HOST = 'mongodb://localhost/'
MONGO_DB = 'new_clean'

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
    key = ['slot', '#2019PilihJokowi','LAND','TANAH', 'room', 'available','rent', 'sale', 'jual', 'Jual','tiktok', 'land', 'property','standbye','vasektomi','indihome',
                'Expensive','astungkara','listrik','uwu','bengkel','sungai','furukawa','ambulan','plastik','sinyal','resort','hotel','CV','Cosmetics','scrubs'
                'lowongan kerja','prabowo','pijat','jokowi','butter','skin','lotion','skin','sell','Bengkuang','Avocado','sandals','Shop','shop','#guesthouse',
                '#kontraktor','kontraktor','wax','arrival','soap','Soap','soak','Bath','pores','buy','open','selingan','store','belanja','Pln','tiket',
           'apply','paket','tlpn','#zumbalovers','murah']

    keyWords = []
    for i in range(1, len(key)):
        keyWords.append(key[i].lower())

    for i in data_details:

        data = {}
        if 'text' in i :
            text = i['text'].lower()
            val_t = re.findall('|'.join(keyWords), text)

            print ("ada text")
        elif 'full_text' in i :
            text = i['full_text'].lower()
            val_t = re.findall('|'.join(keyWords), text)


        if (text.find('#beratan')) != -1 :
            # x = text.find('#beratan')!= -1
            # val_t = re.findall('|'.join(keyWords), text)
            # if x != val_t:

            tweetcon += 1
            data['created_at'] = i['created_at']
            data['id'] = i['id']
            data['text'] = text
            data['retweet_count'] = i['retweet_count']
            data['favorite_count'] = i['favorite_count']
            db.insert(data)
        # else:
        #     print('test')

        elif (text.find('beratan')) != -1 and (text.find('lake')) != -1 :
            # x = text.find('beratan') != -1 and text.find('lake') != -1
            # val_t = re.findall('|'.join(keyWords), text)
            # if x != val_t:

            tweetcon += 1
            data['created_at'] = i['created_at']
            data['id'] = i['id']
            data['text'] = text
            data['retweet_count'] = i['retweet_count']
            data['favorite_count'] = i['favorite_count']
            db.insert(data)
        # else:
        #     print('test')
#         # else:
#         #     print('test')
# #
        elif (text.find('beratan')) != -1 and (text.find('temple')) != -1 :
            # x = text.find('beratan') != -1 and text.find('temple') != -1
            # val_t = re.findall('|'.join(keyWords), text)
            # if x != val_t:

            tweetcon += 1
            data['created_at'] = i['created_at']
            data['id'] = i['id']
            data['text'] = text
            data['retweet_count'] = i['retweet_count']
            data['favorite_count'] = i['favorite_count']
            db.insert(data)
        # else:
        #     print('test')

        elif (text.find('beratan')) != -1 and (text.find('pura')) != -1 :
            # x = text.find('beratan') != -1 and text.find('pura') != -1
            # val_t = re.findall('|'.join(keyWords), text)
            # if x != val_t:

            tweetcon += 1
            data['created_at'] = i['created_at']
            data['id'] = i['id']
            data['text'] = text
            data['retweet_count'] = i['retweet_count']
            data['favorite_count'] = i['favorite_count']
            db.insert(data)
        # else:
        #     print('test')

        # elif (text.find('beratan')) != -1  and (text.find('pura'))  != -1 :
        #     val_t = re.findall('|'.join(keyWords), text)
        #     print(val_t)
        #     if i != val_t:
        #         tweetcon += 1
        #         data['created_at'] = i['created_at']
        #         data['id'] = i['id']
        #         data['text'] = text
        #         data['retweet_count'] = i['retweet_count']
        #         data['favorite_count'] = i['favorite_count']
        #         db.insert(data)
        #         print(text)
        #     else:
        #         print('test')


    else:
        print('null')

    print(tweetcon)

if __name__ == "__main__":
    main("beratan")