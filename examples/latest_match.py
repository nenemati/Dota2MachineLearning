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

pd.options.display.max_columns = 200


# Some path fiddling to make sure we can access the module
sys.path.append(abspath(join(abspath(dirname(__file__)), "..")))

from dota2py import api

key = os.environ.get("DOTA2_API_KEY")
if not key:
    raise NameError("Please set the DOTA2_API_KEY environment variable")
api.set_api_key(key)

#with open("heroes.json") as heroes:
    # something
def insert_Match_Detail(matches):
	details_bucket = []
	for match in matches:
		details = api.get_match_details(match_id=match)
		details_bucket.append(details)
		db.nemaBIG.insert(details)

def return_filtered_matched():
    bucket = []
    #grabbing data from
    data = db.nemaBIG.find({"$and": [{"result.game_mode": { "$nin": [0,6,7,8,9,10,11,13,14,15,17,18,19,20,21] }}, {"result.error": {"$exists": 0}} ]})
    # Data is a Cursor object. Need to add to List.
    for d in data:
        bucket.append(d)
    return bucket

def parse_the_df(raw_data):

    for match in raw_data:
        # Counter for player
        count = 1
        # loop through players information
        del match["_id"]
        for player_info in match["result"]["players"]:
          match["result"]["player_"+ str(count) +"_hero_id"] = player_info["hero_id"]

          count = count + 1

        # Delete players column
        del match["result"]["players"]


    encodedJson = json.dumps(raw_data)
    data = json.loads(encodedJson)

    # Normalize json to work with DataFrame
    return json_normalize(data)

def calculate_win_rate(hero_id, radiant, dire, radiant_win):
    if hero_id in radiant and radiant_win:
        # Win on Radiant side
        return 1
    elif hero_id in dire and not radiant_win:
        # Win on Dire side
        return 1
    elif hero_id not in radiant and hero_id not in dire:
        # Not in game
        return 0
    elif hero_id in radiant and not radiant_win:
        # Radiant loss
        return -1
    elif hero_id in dire and radiant_win:
        # Dire loss
        return -1

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
    raw_data = return_filtered_matched()

    # Get raw dataframe that needs additional manipulation aka all our mongo data
    normalized_dataframe = parse_the_df(raw_data)
    # Restructure dataframe
    df = normalized_dataframe[[
        'result.match_id',
        'result.radiant_win',
        'result.player_1_hero_id',
        'result.player_2_hero_id',
        'result.player_3_hero_id',
        'result.player_4_hero_id',
        'result.player_5_hero_id',
        'result.player_6_hero_id',
        'result.player_7_hero_id',
        'result.player_8_hero_id',
        'result.player_9_hero_id',
        'result.player_10_hero_id'
    ]]
    # print normalized_dataframe
    for index, row in df.head().iterrows():
        radiant = [
            row['result.player_1_hero_id'],
            row['result.player_2_hero_id'],
            row['result.player_3_hero_id'],
            row['result.player_4_hero_id'],
            row['result.player_5_hero_id']
        ]
        dire = [
            row['result.player_6_hero_id'],
            row['result.player_7_hero_id'],
            row['result.player_8_hero_id'],
            row['result.player_9_hero_id'],
            row['result.player_10_hero_id']
        ]
        for hero_id in range(1, 10):
            print calculate_win_rate(hero_id, radiant, dire, row['result.radiant_win'])
            print hero_id
            print row['result.radiant_win']
            print row['result.match_id']
        # print row['result.match_id'], row['result.radiant_win'] +


main()
