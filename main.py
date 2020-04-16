import requests

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url) #向html提出get請求

json_content = html_content.json() # 將內容轉為json
print(json_content)

records = json_content.get('records')
location = records.get('location')
print(location)

# for i in range(len(location)):
#    print(location[i])
for l in location:
    lat = l.get('lat')
    lon = l.get('lon')
    locationName = l.get('locationName')
    stationId = l.get('stationId')
    time = l.get('time')

    print(lat, lon, locationName, stationId, time)


# 取得觀測資料
weatherElement = l.get('weatherElement')
for element in weatherElement:
    elementName = element.get('elementName')
    elementValue = element.get('elementValue')
    print(elementName, elementValue)

