from pymongo import MongoClient
from pyspark import SparkContext, SparkConf
import json
import datetime
import xlsxwriter
from TweetPerTanggal import TweetPerTanggal

MONGO_HOST ='mongodb://localhost/'
MONGO_DB ='db_bersih'
def get_json(collection_name):
    client = MongoClient(MONGO_HOST)
    db = client[MONGO_DB]
    collection = db[collection_name]
    return collection
# def save_data(data):
#     with open('data_location.json', 'w') as outfile:
#         json.dump(data, outfile)
#         print("sukses")
#     return data

# def save_json(collection_name):
#     client = MongoClient(MONGO_HOST)
#     db = client["db-tweet"]
#     collection = db[collection_name]
#     return collection

def ubah_format_tanggal(tanggal):
    dt = datetime.datetime.strptime(tanggal, '%a %b %d %H:%M:%S %z %Y')
    return datetime.date.strftime(dt, "%d/%m/%Y")

def cari_index_tanggal(arr, tanggal):
    for i in range(len(arr)):
        if(arr[i].created_at == tanggal):
            return i
    return -1;

def main(collection_name):
    # get json data from MongoDB
    data = get_json(collection_name)
    data_details = data.find()
    count_jumlah = 0

    #variabel
    arr_tweet_per_hari = []
    # col_name = collection_name.replace("#",'')
    dataHasil =''
    for i in data_details:
        create_at = ubah_format_tanggal(str(i['created_at']))
        index = cari_index_tanggal(arr_tweet_per_hari, create_at)
        if(index == -1):
            tweet_baru = TweetPerTanggal(create_at)
            tweet_baru.total_tweet = 1
            arr_tweet_per_hari.append(tweet_baru)
        else :
            arr_tweet_per_hari[index].total_tweet += 1
            arr_tweet_per_hari[index].total_retweet += int(i['retweet_count'])
            arr_tweet_per_hari[index].total_fav += int(i['favorite_count'])

    print_excel(arr_tweet_per_hari)

        # hasil = create.split(" ")
        # print(hasil)
        # if(len(hasil)== 2):
        #
        #     date = hasil[0].split("-")
        #     dd = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        #     final = date[2] + "/" + date[1] + "/" + date[0]
        #     # print(final)
        #     # print(dataHasil)
        # elif(len(hasil)==6):
        #     print(i["created_at"])
        #     tanggal = hasil[2]
        #     bulan = hasil[1]
        #     tahun = hasil[5]
        #     if(bulan=='Apr'):
        #         bulan = 4
        #     elif(bulan=='Mar'):
        #         bulan = 3
        #     elif (bulan == 'Feb'):
        #         bulan = 2
        #
        #     dd = datetime.date(int(hasil[5]), int(bulan), int(hasil[2]))
        #     final = tanggal + "/" + dd.strftime("%m") + "/" + tahun
        #     print(final)
        #     # print(dd)

        # dataHasil += final+ "\n"
    with open('Tweet.txt', 'w', encoding="utf-8") as file:
        file.write(dataHasil)

# def spark_count():
#     # menghitung banyak tweet per tanggal
#     array_x =[]
#     array_y = []
#     conf = SparkConf().setAppName("word Count").setMaster("local[3]")
#     sc = SparkContext(conf=conf)
#     dataLoc = ""
#
#     lines = sc.textFile("Tweet.txt")
#
#     wordCounts = lines.countByValue()
#     for word, count in wordCounts.items():
#         dataLoc += ("{} : {}".format(word, count)) + "\n"
#         x = str(word)
#         y = str(count)
#         array_x.append(x)
#         array_y.append(y)
#         print("x = {0}".format(x))
#         print("y = {0}".format(y))
#
#     workbook = xlsxwriter.Workbook('uluwatu.xlsx')
#     worksheet = workbook.add_worksheet()
#     for index, value in enumerate(array_x):
#         worksheet.write(index, 0, array_x[index])
#         worksheet.write(index, 1, array_y[index])
#         # worksheet.write(index, 2, self.name)
#     workbook.close()


def print_excel(arr):
    workbook = xlsxwriter.Workbook('tanahlot_tweet.xlsx')
    worksheet = workbook.add_worksheet()
    for i in range(len(arr)):
        #file pertama
        worksheet.write(i, 0, arr[i].created_at)
        worksheet.write(i, 1, arr[i].total_tweet)
    workbook.close()

    workbook2 = xlsxwriter.Workbook('tanahlot_retweet_fav.xlsx')
    worksheet2 = workbook2.add_worksheet()

    for i in range(len(arr)):
        #file kedua
        worksheet2.write(i, 0, arr[i].created_at)
        worksheet2.write(i, 1, arr[i].total_retweet)
        worksheet2.write(i, 2, arr[i].total_fav)

    workbook2.close()

if __name__ == "__main__":
    main("tanahlot")
    # spark_count()

