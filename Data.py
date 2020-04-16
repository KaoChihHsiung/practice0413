class location:
    def __init__(self, location_name= None, lat= None,
                 lon=None, station_id= None, time= None,
                 weather_element=None):
        self.location_name = new_location_name
        self.lat = lat
        self.lon = lon
        self.station_id = station_id
        self.time = time

for item in location:
    lat = item.get('lat')
    lon = item.get('lon')
    locationName = item.get('locationName')
    stationId = item.get('stationId')
    time = item.get('time')
    obsTime = time.get('obsTime')

    def from_json(self, json_data):
        self.lat = json_data.get()