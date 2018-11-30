
use yelpdb

db.businessids.createIndex({"bid":1}, {unique:true})

> use yelpdb
switched to db yelpdb
> db.businessids.createIndex({"bid":1}, {unique:true})
{
	"createdCollectionAutomatically" : true,
	"numIndexesBefore" : 1,
	"numIndexesAfter" : 2,
	"ok" : 1
}


db.userids.createIndex({"uid":1}, {unique:true})



db.businessids.find().pretty()
db.businessids.deleteMany({})

db.userids.find().pretty()
