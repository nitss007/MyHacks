import requests
import json
param = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = ["https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=505&date=06-05-2021",
"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=506&date=05-05-2021"]
for u in url:
    print( "--------------------------------------")
    print( "testing for "+u )
    r = requests.get (url = u, headers = param)
    # print(r.text)
    # print(r.request.headers)
    data = r.json()
    hospitals = data['centers']
    for elem in hospitals:
     for se in elem['sessions']:
       if(se['min_age_limit'] ==18 & se['available_capacity'] > 10):
         print(json.dumps(elem, indent = 3))
         break
