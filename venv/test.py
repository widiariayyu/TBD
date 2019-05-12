# from pymongo import MongoClient
import re
# MONGO_HOST = 'mongodb://localhost/'
# MONGO_DB = 'db_new'
#
# def get_json(collection_name):
#     client = MongoClient(MONGO_HOST)
#     db = client[MONGO_DB]
#     collection = db[collection_name]
#     return collection
#
# def save_json(collection_name):
#     client = MongoClient(MONGO_HOST)
#     db = client["db_bersih"]
#     collection = db[collection_name]
#     return collection
#
# def main(collection_name):
#     # get json data from MongoDB
#     data = get_json(collection_name)
#     data_details = data.find()
#     db = save_json(collection_name)
#     tweetcon = 0

key = ['slot', '#2019PilihJokowi','land','tanah', 'room', 'available','rent', 'sale', 'jual','tiktok', 'property','standbye','vasektomi','indihome',
                'expensive','astungkara','listrik','uwu','bengkel','sungai','furukawa','ambulan','plastik','sinyal','resort','hotel','cv','cosmetics','scrubs'
                'lowongan kerja','prabowo','pijat','jokowi','butter','skin','lotion','skin','sell','bengkuang','avocado','sandals','shop','#guesthouse',
                '#kontraktor','kontraktor','wax','arrival','soap','soap','soak','bath','pores','buy','open','selingan','store','property','belanja','pln','tiket',
           'apply','paket','tlpn','#zumbalovers','murah','ttd-nya','lentera']

text = 'tanah di uluwatu sangat bagus'
test = re.findall('tanah', text)
text.
print(test)
    #             data.clear()

    # for i in data_details:
    #     data = {}
    #     if 'text' in i:
    #         text = i['text'].lower()
    #         print("ada text")
    #     elif 'full_text' in i:
    #         text = i['full_text'].lower()
    #
    #
    #     if (text.find('bedugul')) != -1 and (text.find('#bali')) != -1:
    #         for dlt in key:
    #             for text in data_details:
    #                 if(str(dlt).lower() in str(data).lower()):
    #                     data_details.remove(data)
    #         print ("array : {}".format(arr_key))
    #         arr_key = ['tanah dijual di pasir', 'uluwatu sangat bagus']