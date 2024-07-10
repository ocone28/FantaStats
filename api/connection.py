from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# Accesso a un database
db = client['Fantacalcio']

# Accesso a una collezione
collection = db['Calciatori']

collection2 = db['Statistiche']
