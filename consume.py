from urllib import request

import pandas as pd
import requests
import json
import html_to_json

#resp = request.urlopen("https://modelo-prueba.herokuapp.com/")
URL = "https://modelo-prueba.herokuapp.com/result"
DATA = {'a':1, 'b':3, 'c':9}

#r = requests.post(url=URL, data=PARAMS)

r = requests.post(URL,data=DATA)
r_json = html_to_json.convert(r.content)

prob = r_json['html'][0]['body'][0]['h3'][0]['_value']

print(prob)
#print(resp.code)
#print(resp.length)
#print(resp.peek())