import pymongo
import os
from dataclasses import dataclass

@dataclass   ## TO IMPORT THE DATA CORRECTLY

class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()


mongo_client = pymongo.MongoClient(env_var.mongo_db_url)   #creation of object
