import requests
import csv
import json
from datetime import datetime
from dateutil import tz

lat=['19.0735','19.0380','28.7041']
lon=['72.8995','72.8538','77.1025']
file_name=['somaiya.csv','dharavi.csv','delhi.csv'] 

for i in range(0,3):

	p1='https://api.breezometer.com/air-quality/v2/current-conditions?lat='
	p2=lat[i]
	p3='&lon='
	p4=lon[i]
	p5='&key=234f6676c510445d9047048a13aa1e7b&features=local_aqi,health_recommendations,pollutants_concentrations'
	http=p1+p2+p3+p4+p5 
	req = requests.get(http)
	data = req.json() 

	globe=[]

	if(data["data"]["data_available"]==True):
	
		#date-time conversion
		from_zone = tz.gettz('UTC')
		to_zone = tz.tzlocal()
		time=data["data"]["datetime"]
		utc = datetime.strptime(time,'%Y-%m-%dT%H:%M:%SZ')
		utc = utc.replace(tzinfo=from_zone)
		central = utc.astimezone(to_zone)
		date=central.strftime('%d-%m-%Y')
		time=central.strftime('%H:%M:%S')
		globe.append(date)
		globe.append(time)

		#air_quality
		aqi=data["data"]["indexes"]["ind_cpcb"]["aqi"]
		category=data["data"]["indexes"]["ind_cpcb"]["category"]
		color=data["data"]["indexes"]["ind_cpcb"]["color"]
		dominant=data["data"]["indexes"]["ind_cpcb"]["dominant_pollutant"]
		globe.append(aqi)
		globe.append(category)
		globe.append(color)
		globe.append(dominant)

		#pollutant_concentrations
		#co
		co=data["data"]["pollutants"]["co"]["concentration"]["value"]
		co_units=data["data"]["pollutants"]["co"]["concentration"]["units" ]
		globe.append(co)
		globe.append(co_units)
		#no2
		no2=data["data"]["pollutants"]["no2"]["concentration"]["value"]
		no2_units=data["data"]["pollutants"]["no2"]["concentration"]["units" ]
		globe.append(no2)
		globe.append(no2_units)
		#o3
		o3=data["data"]["pollutants"]["o3"]["concentration"]["value"]
		o3_units=data["data"]["pollutants"]["o3"]["concentration"]["units" ]
		globe.append(o3)
		globe.append(o3_units)
		#pm10
		pm10=data["data"]["pollutants"]["pm10"]["concentration"]["value"]
		pm10_units=data["data"]["pollutants"]["pm10"]["concentration"]["units" ]
		globe.append(pm10)
		globe.append(pm10_units)
		#pm25
		pm25=data["data"]["pollutants"]["pm25"]["concentration"]["value"]
		pm25_units=data["data"]["pollutants"]["pm25"]["concentration"]["units" ]
		globe.append(pm25)
		globe.append(pm25_units)
		#so2
		so2=data["data"]["pollutants"]["so2"]["concentration"]["value"]
		so2_units=data["data"]["pollutants"]["so2"]["concentration"]["units" ]
		globe.append(so2)
		globe.append(so2_units)

		#print(globe)

		#health_recommendations
		active=data["data"]["health_recommendations"]["active"]
		children=data["data"]["health_recommendations"]["children"]
		elderly=data["data"]["health_recommendations"]["elderly"]
		general_pop=data["data"]["health_recommendations"]["general_population"]
		heart=data["data"]["health_recommendations"]["heart_diseases"]
		lung=data["data"]["health_recommendations"]["lung_diseases"]
		pregnant=data["data"]["health_recommendations"]["pregnant_women"]
		globe.append(active)
		globe.append(children)
		globe.append(elderly)
		globe.append(general_pop)
		globe.append(heart)
		globe.append(lung)
		globe.append(pregnant)

		with open(file_name[i],'a',newline="") as f:
        		writer = csv.writer(f)
writer.writerow(globe)

print("Done successfully")

#print(json.dumps(data, indent=4, sort_keys=True))