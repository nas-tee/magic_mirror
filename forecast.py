import datetime

import forecastio

api_key= os.environ['MAGIC_MIRROR_APIKEY']
lat= os.environ['MAGIC_MIRROR_LATITUDE']
lng= os.environ['MAGIC_MIRROR_LONGITUDE']

current_time = datetime.datetime.now()
#generate a forecast
forecast = forecastio.load_forecast(api_key, lat, lng, time=current_time)

#define variables from forecast
byHour = forecast.hourly()
byMinute = forecast.minutely()
byNow = forecast.currently()

#check datapoint times
print(byNow.time)

