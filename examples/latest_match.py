import sys
from os.path import abspath, join, dirname
import os
import time
import pandas as pd 
import numpy as np 
import json
import pymongo
from pymongo import MongoClient 


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

details = api.get_match_details(match_id=1729103401)

db.nema.insert(details)


# print details
# this is for 1000
# matchesList = range(1729103401-1000,1729103401)
matchesList = range(1729103401-10,1729103401)

def grab_Match_Detail(n):
	details_bucket = []
	for p in n:
		details = api.get_match_details(match_id=p)
		details_bucket.append(details)
		db.larger.insert(details)
		print len(details_bucket)


grab_Match_Detail(matchesList)
		 
