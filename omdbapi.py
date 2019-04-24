import requests
import json
import sys
movie=sys.argv[1]
url = 'http://www.omdbapi.com'
params = dict(
    apikey='8d6012',
)
params['t']=movie
resp = requests.get(url=url, params=params)
req = resp.json()
try:
  print("Movie is :" +req['Title'])
except:
  print ("Movie not found")
try:
  print("Rotten Tomatoes Rating is :" +req['Ratings'][1]['Value'])
except:
  print ("Rotten Tomatoes Rating not found ")
