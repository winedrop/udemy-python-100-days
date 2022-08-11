
#   --------------------- iss_position_with_api -----------------------
import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
  
#at this point you will get a response code rather than the json dictionary when you open it in the browser
##print(response)
  
#rather than writing a specific exception for every status/response code you can use this method in requests module
response.raise_for_status()
  
#how to actually get the json data
data = response.json()
print(data)
  
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
  
iss_position = (longitude, latitude)
  
 #response code notes
## 1XX: Hold on
## 2XX: Here You Go, everything is working as intended
## 3XX: Go away, dont have permission
## 4XX: You Screwed Up, thing you are looking for doesn't exist
## 5XX: I Screwed Up, some error with the server, or down
#   --------------------------------------------------------------------

#-----------stuff for sunrise and sunset api--------------------------
#sunrise and sunset api requires lat and lng parameters and other are optional

#fix maxretryerror
requests.adapters.DEFAULT_RETRIES=5

#some lat and lng
MY_LAT = 51.507351
MY_LONG = 20.12352

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()

sun_data = response_sun.json()
print(sun_data)

