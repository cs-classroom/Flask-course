from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.csclassroom

db.movies.insert_one({'name': 'Thor: Ragnarok', 'rating': 7.9})
db.movies.insert_one({'name': 'Wonder Woman', 'rating': 7.5})
db.movies.insert_one({'name': 'Logan', 'rating': 8.1})
db.movies.insert_one({'name': 'Despicable Me 3', 'rating': 6.3})

for item in db.movies.find():
    print(item)
