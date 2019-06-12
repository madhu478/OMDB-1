import requests
import json
import sys
try:
 MacAddress=sys.argv[1]
except NameError:
 print("Address not found")
url = 'https://api.macaddress.io/v1'
params = dict(
    apikey='at_7ubl6OxM0uII0hA3LqeScDxTvTlPh',
    output='json'
)                                                                                                                                                                                         
params['search']=MacAddress
resp = requests.get(url=url, params=params)                                                                                                                                               
info = resp.json()                                                                                                                                                                        
try:
  print("Company Name is:" +info['vendorDetails']['companyName'])
except:
  print ("Company Name not found not found ")