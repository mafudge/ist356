import requests

'''
curl -X 'POST' \
  'https://cent.ischool-iot.net/api/azure/entityrecognition' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: ea044c96950db6cc0fab7ae1' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'text=The%20Dallas%20Cowboys%20are%20a%20far%20better%20team%20than%20the%20New%20York%20Giants%20this%20year.%20The%20Giants%20have%20not%20won%20a%20conference%20game%20yet.'
'''
url = "https://cent.ischool-iot.net/api/azure/entityrecognition"
headers = {
    "accept": "application/json",
    "X-API-KEY": "ea044c96950db6cc0fab7ae1",
    "Content-Type": "application/x-www-form-urlencoded",
}
data = {
    "text": "The Dallas Cowboys are a far better team than the New York Giants this year. The Giants have not won a conference game yet."
}
response = requests.post(url, headers=headers, data=data)
response.raise_for_status()
data = response.json()
for d in data['results']['documents'][0]['entities']:
    print(d['text'], d['category'])
