import requests
import os
from twilio.rest import Client

#twilio setup -- to be converted to env variables
#account_sid = os.environ["TWILIO_ACCOUNT_SID"]
#auth_token = os.environ["TWILIO_AUTH_TOKEN"]

account_sid = "AC1a2e909926f462233a69d2ec20f1a229"
auth_token = "ac30eaefd6b71f7139b50f27fc601b6f"


#estuary set up
url = "https://api.estuary.tech/content/add"


payload={}
files=[
  ('data',('file',open('static/result.png','rb'),'application/octet-stream'))
]
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer EST78a8d35e-2d1f-42e5-8207-c784e49b4de0ARY'
}


response = requests.request("POST", url, headers=headers, data=payload, files=files)


response_txt = response.text
print(response_txt)
url_s = (response_txt.find('estuary_retrieval_url'))+ 24
url_e = (response_txt.find('estuaryId')) - 3 - url_s

theUrl= (response_txt[url_s:url_s+url_e:1])

client = Client(account_sid, auth_token)
client.messages.create(
    to="+19259643840",
    from_="+19136758450",
    body=(f'This is a test message {theUrl}')
    )


#ON WEBISTE
### POST Location
### GET retrival_url

#HERE
### GET Location
### POST retrival_url (can be then GET in the webapp to display the image)

