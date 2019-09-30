import pymongo
import json
import os
import requests
from Classes.Tools import Tools

Decode = Tools.decode
Initer = Tools.initer

dirpath = os.getcwd()

DEBUG = False
with open(os.path.join(dirpath, "./Configs/Configs.json")) as f:
    configs = json.load(f)

if not DEBUG:

    get_database_url = json.loads(
        requests.get("{0}/Services/config/get/FileManagement".format(configs['MicroServiceManagementURl']),
                     verify=False).content)

    if not get_database_url["State"]:
        exit(1)

    get_database_url = json.loads(get_database_url["Description"])

    url = Decode(get_database_url["DatabaseString"],get_database_url["Key"][2:-1])
    print(url)

else:
    url = 'mongodb://localhost:27017'



mongodb = pymongo.MongoClient(url)
database = mongodb[configs["Database"]["Name"]]
files_collection = database[configs["Database"]["Collections"]["Files"]]
