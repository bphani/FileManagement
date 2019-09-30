import pymongo
import json
import os
import logging


with open('./Configs/Configs.json') as f:
    configs = json.load(f)
logging.warning(f"Getting database string ...")

#database_url = os.environ["MongoDbUrl"]
# if database_url is None:
database_url = "mongodb://localhost:27017"
logging.warning(f"Database Url : {database_url}")


mongodb = pymongo.MongoClient(database_url)
database = mongodb[configs["Database"]["Name"]]
files_collection = database[configs["Database"]["Collections"]["Files"]]
