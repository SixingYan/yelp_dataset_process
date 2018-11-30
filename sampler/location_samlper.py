from pymongo import MongoClient

readPath = '/Users/alfonso/workplace/googleSync/yelp_dataset_sql/business_location.txt'
writePath = '/Users/alfonso/workplace/googleSync/yelp_dataset_sql/business_location_lv.txt'
dbName = 'yelpdb'
fld = 'bid'

client = MongoClient('mongodb://localhost:27017/')
db=client[dbName]

def read4txt():
    i = 0
    with open(readPath, 'r') as f:
        for sql in f:
            #print(sql)
            city = sql.split('(')[2].split(',')[1].replace("'", '')
            businessid = sql.split('(')[2].split(',')[0].replace("'", '')
            #print(city)
            #print(businessid)
            #print()
            
            if city == 'Las Vegas':
                write2txt(sql)
                write2db(hash(businessid))
            i += 1
            if i % 100000 == 0:
                print('now is ' + str(i))

def write2txt(sql: str):
    with open(writePath, 'a') as f:
        f.write(sql)
    
def write2db(val:str):
    doc = {fld:val}
    db.businessids.insert_one(doc)

read4txt()

