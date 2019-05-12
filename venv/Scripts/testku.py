from pymongo import MongoClient
from pyspark import SparkContext, SparkConf
import json
import datetime
import xlsxwriter

MONGO_HOST = 'mongodb://localhost/'
MONGO_DB = 'new_clean'
def get_json(collection_name):
    client = MongoClient(MONGO_HOST)
    db = client[MONGO_DB]
    collection = db[collection_name]
    return collection

class FileManagement:
    def __init__(self):
        self.array_x = []
        self.array_y = []
        self.array_z = []
        self.array_tot = []


    def main(self,collection_name):
        # get json data from MongoDB
        data = get_json(collection_name)
        data_details = data.find()
        count_jumlah = 0

        # col_name = collection_name.replace("#",'')
        dataHasil =''
        for i in data_details:
            create = str(i['created_at'])
            hasil = create.split(" ")
            # print(hasil)
            if(len(hasil)== 2):

                date = hasil[0].split("-")
                dd = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                final = date[2] + "/" + date[1] + "/" + date[0]
                # print(final)
                # print(dataHasil)
            elif(len(hasil)==6):
                tanggal = hasil[2]
                bulan = hasil[1]
                tahun = hasil[5]
                if(bulan=='Apr'):
                    bulan = 4
                elif(bulan=='Mar'):
                    bulan = 3
                elif (bulan == 'Feb'):
                    bulan = 2

                dd = datetime.date(int(hasil[5]), int(bulan), int(hasil[2]))
                final = tanggal + "/" + dd.strftime("%m") + "/" + tahun
                # print(dd)

            dataHasil += final+ "\n"
        with open('Tweet.txt', 'w', encoding="utf-8") as file:
            file.write(dataHasil)

        print('sukses')

    # def spark_count(self):
    #     # menghitung banyak tweet per tanggal
    #
    #     conf = SparkConf().setAppName("word Count").setMaster("local[3]")
    #     sc = SparkContext(conf=conf)
    #     dataLoc = ""
    #
    #     lines = sc.textFile("Tweet.txt")
    #
    #     wordCounts = lines.countByValue()
    #     print('b')
    #     for word, count in wordCounts.items():
    #         dataLoc += ("{} : {}".format(word, count)) + "\n"
    #         x = str(word)
    #         y = str(count)
    #         self.array_x.append(x)
    #         self.array_y.append(y)
    #         print("x = {0}".format(x))
    #         print("y = {0}".format(y))

    def retweet(self,collection_name):
        data = get_json(collection_name)
        data_details = data.find()

        for tanggal in range(0, len(self.array_x)):
            retweet = 0
            total = 0
            final = ''
            for i in data_details:
                create = str(i['created_at'])
                retweet_data = int(i["retweet_count"])
                hasil = create.split(" ")
                # print(hasil)
                # print(array_x[tanggal])
                if (len(hasil) == 2):

                    date = hasil[0].split("-")
                    dd = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                    final = date[2] + "/" + date[1] + "/" + date[0]
                    # print(final)
                    # print(dataHasil)
                elif (len(hasil) == 6):
                    tanggal = hasil[2]
                    bulan = hasil[1]
                    tahun = hasil[5]
                    if (bulan == 'Apr'):
                        bulan = 4
                    elif (bulan == 'Mar'):
                        bulan = 3
                    elif (bulan == 'Feb'):
                        bulan = 2

                dd = datetime.date(int(hasil[5]), int(bulan), int(hasil[2]))
                final = tanggal + "/" + dd.strftime("%m") + "/" + tahun
                print(retweet_data[tanggal])
        #         print(self.array_x[tanggal])
        #         if (self.array_x[tanggal] == final):
        #             retweet = retweet + retweet_data
        #
        #     total = self.array_y[tanggal] + retweet
        #     self.array_tot.append(total)
        #     self.array_z.append(retweet)
        #
        # for i in range(0, len(self.array_x)):
        #     print(str(self.array_x[i]) + "   " + str(self.array_y[i]) + "   " + str(self.array_z[i]) + "   " + str(self.array_tot[i]))

    def save(self):
        workbook = xlsxwriter.Workbook('uluwatu.xlsx')
        worksheet = workbook.add_worksheet()
        for index, value in enumerate(array_x):
            worksheet.write(index, 0, self.array_x[index])
            worksheet.write(index, 1, self.array_y[index])
            worksheet.write(index, 2, self.array_z[index])
            worksheet.write(index, 3, self.array_tot[index])
            # worksheet.write(index, 2, self.name)
        workbook.close()


if __name__ == "__main__":
    file_management = FileManagement()
    file_management.main("uluwatu")
    # file_management.spark_count()
    file_management.retweet("uluwatu")
    file_management.save()

