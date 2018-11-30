from pymongo import MongoClient
file = 'user_follow'
readPath = '/Users/alfonso/workplace/googleSync/yelp_dataset_sql/' + file + '.txt'
writePath = '/Users/alfonso/workplace/googleSync/yelp_dataset_sql/' + file + '_lv.txt'

dbName = 'yelpdb'

client = MongoClient('mongodb://localhost:27017/')
db = client[dbName]


def read4txt():
    i = 0
    with open(readPath, 'r') as f:
        for sql in f:
            userid = sql.split('(')[2].split(',')[0].replace("'", '')

            if db.userids.find_one({'uid': hash(userid)}) is not None:
                write2txt(sql)

            i += 1
            if i % 100000 == 0:
                print('now is ' + str(i))


def write2txt(sql: str):
    with open(writePath, 'a') as f:
        f.write(sql)

read4txt()
