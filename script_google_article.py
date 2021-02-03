import json
import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
import datetime

#as we have 100 search by day we limit it with a counter

counter_search = 0
max_search = 90

GOOGLE_CSE_API_KEY = 'AIzaSyDhtfF-kW4OFi35o8jMqFndEkzJHMGazQk'

#Possible argument : https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list

cr = 'countryBE' #limit result to belgiul
cx = '271692d39282923bf' #search engine id
num = 15 # because I don't need hundred of result
lr = 'lang_fr' # or lang_nl
q = 'Proposition de résolution visant à soutenir un Traité contraignant des Nations Unies sur les "Entreprises et Droits de l\'homme" et une initiative européenne sur le devoir de vigilance'


URL = 'https://customsearch.googleapis.com/customsearch/v1?'
PARAMS ={'cr':'countryBE',
         'cx':'271692d39282923bf',
         'num':10,
         'lr':'lang_fr',
         'key': GOOGLE_CSE_API_KEY,
         'q':'Proposition de résolution visant à soutenir un Traité contraignant des Nations Unies sur les "Entreprises et Droits de l\'homme" et une initiative européenne sur le devoir de vigilance',}
#we need to take all the point that does not have article linked to it first


r = requests.get(url = URL, params = PARAMS)

data = r.json()
json_formatted_str = json.dumps(data, indent=2)

print(r)
print("-------------------------------------")
print(data)
print("-------------------------------------")
print(json_formatted_str)

#GET https://customsearch.googleapis.com/customsearch/v1?cr=countryBE&cx=271692d39282923bf&lr=lang_fr&num=15&q=test%20recherche&key=[YOUR_API_KEY] HTTP/1.1
