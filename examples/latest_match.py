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


client = MongoClient()
client = MongoClient('localhost', 27017)

db = client.dotaBase
collection = db.matches

# Some path fiddling to make sure we can access the module
sys.path.append(abspath(join(abspath(dirname(__file__)), "..")))

from dota2py import api

key = os.environ.get("DOTA2_API_KEY")
if not key:
    raise NameError("Please set the DOTA2_API_KEY environment variable")
api.set_api_key(key)

# Get all the most recent match played by the player 'acidfoo'
account_id = [46939344, 75284629]

# Get a list of recent matches for the player
# matches = api.get_match_history(account_id=account_id[0])["result"]["matches"]
my_matches_bucket = []

# details = api.get_match_details(match_id=)

#my_matches_bucket.append(matches)

# details = api.get_match_details(match_id=1729103401)
details = api.get_match_details(match_id=1729103400)

# print details
# print details
# db.nema.insert(details)


# print details
# this is for 1000
# matchesList = range(1729103401-1000,1729103401)
# matchesList = range(1729103401-1000,1729103401)

def insert_Match_Detail(n):
	details_bucket = []
	for p in n:
		details = api.get_match_details(match_id=p)
		details_bucket.append(details)
		db.nemaBIG.insert(details)
		print len(details_bucket)


# grab_Match_Detail(matchesList)

#grab all teams and heros associated with them

#grab hero_id attach win or lose then attach match_number

# collectionss = db.nemaBIG
# dictionaryy = collectionss.to_mongo()



def find_players_in_game():
	# collection = db.nemaBIG
	agg_data = db.nemaBIG.aggregate([{"$match" : {"player[0].hero_id" : "$by_user"}}]);
		

find_players_in_game()


	# newCollection = json.load(collection)
	# db.nemaBIG.Map_reduce(map_function, reduce_function,query='{hero_id}')

	# match_number = 0
	# team_heroes = dict()
	# for n in matches
	# 	count = count + 1


	

# 	# db.zipcodes.aggregate( [
# 	#    { $hero: { _id: "$hero_id", totalPop: { $sum: "$pop" } } },
# 	#    { $winorlose: { totalPop: { $gte: 10*1000*1000 } } }
# 	# ])



# find_players_in_game()














		 
