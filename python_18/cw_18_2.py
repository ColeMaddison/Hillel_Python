import requests
KEY = '34dd32882c0b1cba14ec21d407478769'
URL = "https://api.darksky.net/forecast/{}/".format(KEY)
CURR_LOCATION_URL = "https://api.ipdata.co?api-key=test"

class Forecast(object):
    def request_to_api(self, params_str=''):
        location = self.get_current_location()
        lat_lon_str = ",".join((str(location[0]),str(location[1])))
        return requests.get("{}{}?units=si&{}".format(URL, lat_lon_str, params_str))

    def get_current_location(self):
        r = requests.get(CURR_LOCATION_URL)
        j = r.json()
        lat = j['latitude']
        lon = j['longitude']
        return (lat, lon)

    def get_current_temperature(self):
        get_forecast = self.request_to_api()
        return get_forecast.json()['currently']['temperature']

weather = Forecast()
print(weather.get_current_temperature())