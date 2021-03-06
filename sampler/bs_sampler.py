from pymongo import MongoClient
file = 'tips'
readPath = '/Users/alfonso/workplace/googleSync/yelp_dataset_sql/' + file + '.txt'
writePath = '/Users/alfonso/workplace/googleSync/yelp_dataset_sql/' + file + '_lv.txt'

dbName = 'yelpdb'
fld = 'bid'

client = MongoClient('mongodb://localhost:27017/')
db = client[dbName]


def read4txt():
    i = 0
    with open(readPath, 'r') as f:
        for sql in f:
            # print(sql)
            businessid = sql.split('(')[2].split(',')[0].replace("'", '')

            if db.businessids.find_one({fld: hash(businessid)}) is not None:
                write2txt(sql)

            i += 1
            if i % 100000 == 0:
                print('now is ' + str(i))


def write2txt(sql: str):
    with open(writePath, 'a') as f:
        f.write(sql)


def write2db(val: str):
    doc = {fld: val}
    db.userids.insert_one(doc)

read4txt()
