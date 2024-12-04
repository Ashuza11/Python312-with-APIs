import urllib3
import rich as r

resp = urllib3.request("GET",
                       "https://api.zippopotam.us/us/94530")
result = resp.json()
latitude = result['places'][0]['latitude']
logitude = result['places'][0]['longitude']
r.print(latitude, logitude)

# Now call the sunset api
resp = urllib3.request("GET",
                       f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={logitude}&timezone=CAT&date=today")

result = resp.json()
r.print(result)
