from pymongo import MongoClient
import os
import json

connection = MongoClient()

db = connection['decretazo'] # base de datos con la que trabajamos
decretos = db.decretos #tomamos la coleccion


from os.path import join, getsize
for root, dirs, files in os.walk('json'):
	for filename in files :
		json_data = open(root+'/'+filename)
		jsonDocument = json.load(json_data)
		decretos.insert(jsonDocument)
		json_data.close()
    