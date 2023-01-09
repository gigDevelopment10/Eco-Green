import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from datetime import datetime
import matplotlib.pyplot as plt
import json
from datetime import timedelta
import requests

url = 'https://api.jsonbin.io/b/5dcbbbaff05d9041253ac1a1'
headers = {
 'Content-Type': 'application/json',
 'secret-key': '$2b$10$Pqzvku5aQl0t2OQh..6bAOGEOZraDqFcoJK0wKUOveq5sNyQ0xlPq',
 'versioning':'false'
}


# put everthing that needs to be sent in "data" 
data={}

# for e.g 
# data["name"] = "tushar"
# data["age"] = "21"


# structure of  predictions-json should be   :
# array of 12 objects for 12 hours  where each obj has following attr
# {
#	"data" :[
#				{
#			 	"datetime" : "datetime_timestamp_of_this_predection" ,
#			   "pollutants" : { 
#                               "co" : "concentration e.g 764" ,
#			 					"no2" : "concentration e.g 764" ,
#			                  "o3" : "concentration e.g 764" , 					
#			                    "pm10" : "concentration e.g 764" ,
#							   "pm25" : "concentration e.g 764" ,
#								"so2" : "concentration e.g 764" ,
#							  }
#  	            }
#               {  2nd obj  }
# 
#               {12th obj }
#            ]
# 
# } 


json_data = json.dumps(data)
loaded_r = json.loads(json_data)
#print(type(loaded_r))
#print(type(json_data))

req = requests.put(url, json=loaded_r, headers=headers)
print(req.text) 