from stations_challenge import Station, BusStation, SubwayStation
# Why are the print statements from the stations_challenge file imported and run as well?
'''
Now, it's time to design a few more stations of your own in another script! 

Make a new python script called "station_planning.py"
    -In this script, *import* the classes you made in this challenge file
    -Instantiate 3 more stations of your choosing (at least 1 bus and 1 subway)
    -Feel free to make up names, locations, lines, and routes!
'''
station_1 = Station(station_name='North Central',
                    location='888 West Washington Street')
station_1.show_info()

bus_station_2 = BusStation(station_name='Central Hub',
                           location='123 Main Street', routes=['1', 'A', 'F'])
bus_station_2.show_info()

subway_2 = SubwayStation(station_name='South Central',
                         location='120 West Line Street', lines=['A', 'B'])

subway_2.show_info()
