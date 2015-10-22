import sys
from os.path import abspath, join, dirname
import os
import time
import pandas as pd
import numpy as np
import json
import pymongo
from pymongo import MongoClient
import json
import numpy as np
import pandas as pd
from collections import namedtuple
from urllib2 import Request, urlopen
from pandas.io.json import json_normalize


client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.dotabase
collection = db.matches

# Some path fiddling to make sure we can access the module
sys.path.append(abspath(join(abspath(dirname(__file__)), "..")))

from dota2py import api

key = os.environ.get("DOTA2_API_KEY")
if not key:
    raise NameError("Please set the DOTA2_API_KEY environment variable")
api.set_api_key(key)

def insert_Match_Detail(matches):
	details_bucket = []
	for match in matches:
		details = api.get_match_details(match_id=match)
		details_bucket.append(details)
		db.nemaBIG.insert(details)

def return_filtered_matched():
    # data = db.nemaBIG.find({"$and": [{"result.game_mode": { "$nin": [0,6,7,8,9,10,11,14,15,18,19,20,21] }}, {"result.error": {"$exists": 0}} ]})
    data = db.nemaBIG.find()

    for d in data:
        print d

def parse_the_D(raw_data):
    # Counter for player
    count = 1
    
    # loop through players information 
    for player_info in raw_data["results"]["players"]:
      # print player_info
      elevations["results"]["player_"+ count +"_hero_id"] = player_info["hero_id"]

      count = count + 1

    # Delete players column
    del elevations["result"]["players"]
    

    encodedJson = json.dumps(raw_data)
    data = json.loads(encodedJson)

    # Normalize json to work with DataFrame
    return json_normalize(data['result'])


def main():
    # Get all the most recent match played by the player 'acidfoo'
    account_id = [46939344, 75284629]

    # Get a list of recent matches for the player
    my_matches_bucket = []

    matchesList = range(1729103401-10000,1729103401)

    # Insert match data into Mongo
    # Comment the function in to get data into your mongo database
    # insert_Match_Detail(matchesList)
    
    # Get match data from DB into encoded JSON
    return_filtered_matched()
    # print raw_data.count()
    # Get raw dataframe that needs additional manipulation
    # normalized_dataframe = parse_the_d(raw_data)
    # print normalized_dataframe


main()
