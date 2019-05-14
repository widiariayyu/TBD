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


def main():
    # get json data from MongoDB

    tweetcon = 0
    # data_lower ={}
    # data_lower['text'] = i['text'].lower()
    key = ['slot', '#2019PilihJokowi', 'room', 'available','rent', 'sale', 'jual', 'Jual','tiktok', 'property','standbye','vasektomi','indihome',
                'Expensive','astungkara','listrik','uwu','bengkel','sungai','furukawa','ambulan','plastik','sinyal','resort','hotel','CV','Cosmetics','scrubs'
                'lowongan kerja','prabowo','pijat','jokowi','butter','skin','lotion','skin','sell','Bengkuang','Avocado','sandals','Shop','shop','#guesthouse',
                '#kontraktor','kontraktor','wax','arrival','soap','Soap','soak','Bath','pores','buy','open','selingan','store','belanja','Pln','tiket',
           'apply','paket','tlpn','#zumbalovers','murah','lentera','sewa','commuter','printing','lamaran','koyoke','nyuzilen','yoichi','#rt']


    dict_hashtag = {
        # 'batukaru': ['batukaru', '#batukaru', 'temple'],
        # 'bedugul':['#bedugul','bedugul bali','bedugul #bali','kebun bedugul','wisata','bedugul'],
        # 'beratan':['#beratan','beratan lake','beratan bali','beratan #bali','#beratanlake','tourism','beratan temple'],
        # 'besakih':['#besakih','besakih bali','besakih #bali','besakih temple','wisata','besakih pura','besakih'],
        # 'brokenbeach': ['#brokenbeach', 'broken beach bali', 'broken beach #bali', 'broken beach nusapenida', 'wisata', 'holiday', 'tourism'],
        # 'candidasa': ['#candidasa', 'candidasa bali', 'candidasa beach #bali', 'candidasa beach','puri candidasa'],
        # 'crystalbay': ['#crystalbay', 'crystalbay bali', 'crystalbay #bali', 'crystalbay beach', 'crystalbay nusapenida'],
        # 'gwk': ['garuda wisnu kencana','#gwk','gwk bali'],
        # 'kelingkingbeach': ['#kelingkingbeach', 'kelingking beach bali', 'kelingking beach #bali', 'kelingking beach',
        #                'kelingking beach nusapenida'],
        # 'kemenuhpark': ['#kemenuh', 'kemenuh park', 'kemenuh #bali', 'kemenuh ubud','kemenuh butterfly'],
        # 'kertalangu': ['#kertalangu', 'kertalangu budaya', 'kertalangu', 'kertalangu desa',
        #             'kertalangu bali'],
        # 'kuta':['#kuta','kuta beach','kuta bali','#kutabeach','kuta #bali','holiday','tourism','vacation','trip','pantai kuta'],
        # 'lempuyang': ['#lempuyang', 'lempuyang','lempuyang temple', 'lempuyang #bali', 'lempuyang bali','pura lempuyang'],
        # 'nusapenida': ['#nusapenida', 'nusa penida', 'nusa penida #bali', 'nusa penida bali', 'nusapenida','travel'],
        # 'sangeh':['sangeh bali','sangeh #bali','#sangeh','sangeh monkey','sangeh monyet','sangeh monkey forest'],
        # 'sanur':['sanur bali','sanur','sanur #bali','#sanur','sanur pantai','sanur beach','#sanurbeach'],
        # 'sukawati':['sukawati bali','sukawati #bali','#sukawati','sukawati market','pasar sukawati','sukawati'],
        # 'taman ayun':['taman ayun','pura taman ayun','temple taman ayun'],
        'tanahlot':['tanah lot','#tanahlot','pura tanah lot','tanah lot temple','tanah lot bali','tanah lot #bali','tanahlot'],
        # 'ubud':['ubud bali','#ubud','ubud #bali','ubud'],
        # 'ubudmonkey':['ubud monkey','ubud monkey bali','ubud monkey #bali','ubud monyet','monkeyforest ubud','monkey forest ubud','monkey forest bali','monkey forest'],
        # 'uluwatu':['uluwatu bali','uluwatu #bali','uluwatu pura','uluwatu temple','#uluwatu','uluwatu']
    }


    for collection_name in dict_hashtag:
        print(collection_name+"\n")
        data = get_json(collection_name)
        data_details = data.find()
        db = save_json(collection_name)


        for tweets in data_details:
            if 'text' in tweets:
                text_lower = tweets['text'].lower()
            elif 'full_text' in tweets:
                text_lower = tweets['full_text'].lower()

            lower_key = [i.lower() for i in key]

            sts = True
            for lower_stopw in lower_key:

                if lower_stopw in text_lower:
                    sts = False
                    # print('False')
                    break


            if sts == True:
                for text_filter in dict_hashtag[collection_name]:
                    print(text_filter)
                    if text_filter in text_lower and "rt @" not in text_lower:

                        data = {}
                        data['created_at'] = tweets['created_at']
                        data['id'] = tweets['id']
                        data['text'] = text_lower
                        data['retweet_count'] = tweets['retweet_count']
                        data['favorite_count'] = tweets['favorite_count']
                        db.insert(data)
                    # if text_filter in text_lower and "rt @" not in text_lower:
                    #     data = {}
                    #     data['created_at'] = tweets['created_at']
                    #     data['id'] = tweets['id']
                    #     data['text'] = text_lower
                    #     data['retweet_count'] = tweets['retweet_count']
                    #     data['favorite_count'] = tweets['favorite_count']
                    #     db.insert(data)
                    #     break


if __name__ == "__main__":
    main()