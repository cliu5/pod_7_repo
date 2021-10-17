from stations_challenge import *

station_new= Station(station_name='central', location="1st and main,")
station_new.show_info()
subway_new= SubwayStation(station_name='west', location="west ave", lines=['a', 'b', 'c'])
subway_new.show_info()
busstation_new= BusStation(station_name='east', location= 'east ave', routes=['1','2', '3',])
busstation_new.show_info()