from stations_challenge import *

stationA = SubwayStation(station_name='1st Street', location="1st Street and Main St.", lines=['A1','C2','H3','L5'])
stationB = SubwayStation(station_name='Maple Ave.', location="Maple Ave and 17th St.", lines=['C3','N4','H3','L1'])
stationC = BusStation(station_name='Dayton RTA', location="3rd Street and Main St.", routes=['Dayton', 'Indianapolis', 'Lexington'])
stationD = BusStation(station_name='Chicago RTA', location="2nd Street and Main Ave.", routes=['New York', 'Denver', 'Atlanta'])

SubwayStation.show_info(stationA)
SubwayStation.show_info(stationB)

BusStation.show_info(stationC)
BusStation.close_station(stationC)
BusStation.show_info(stationC)

BusStation.show_info(stationD)
