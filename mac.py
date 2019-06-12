import requests

import json

import sys

movie=sys.argv[1]

url = 'https://macaddress.io/'

params = dict(

    apikey='at_7ubl6OxM0uII0hA3LqeScDxTvTlPh',
    output='json'
)

resp = requests.get(url=url, params=params)

req = resp.json()

try:

  print("MacAddress is :" +req['search'])
 except:

  print ("Mac Address not found")

try:

  print("Company Name is:" +req['vendorDetails']['companyName'])

except:

  print ("Company Name not found not found ")
