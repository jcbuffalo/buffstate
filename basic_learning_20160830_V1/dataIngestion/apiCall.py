#Using Weather: http://openweathermap.org/current

#Example API Call: api.openweathermap.org/data/2.5/weather?zip=94040,us
#API Key: 2d303cc0ab371210c685f422b4d96733

#Need library from: http://docs.python-requests.org/en/master/
import requests

# Make a get request to get the local weather
response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=14225,us&APPID=2d303cc0ab371210c685f422b4d96733")
print(response.content)
# Print the status code of the response.
print(response.status_code)