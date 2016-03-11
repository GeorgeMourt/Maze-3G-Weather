import json,urllib2


while True:
	x=input("Give the longitude:")
	if x<=180 and x>=-180:
		x=str(x)
		break

while True:
	y=input("Give the latitude:")
	if y<=90 and y>=-90:
		y=str(y)
		break
url="http://api.openweathermap.org/data/2.5/weather?lat="+y+"&lon="+x+"&appid=01e7a487b0c262921260c09b84bdb456"
weatherbot=urllib2.urlopen(url)
weatherinfo=json.load(weatherbot)
tempweather=weatherinfo["main"]["temp"]-273.15
currentweather=weatherinfo["weather"][0]["main"]
if currentweather=="Rain":
	print "I'm singing in the rain!"
if tempweather>20:
	print "nice..."
elif tempweather<5:
	print "brrrr"
#key 01e7a487b0c262921260c09b84bdb456