import requests
from twilio.rest import Client
import os
import time


#twilio setup -- to be converted to env variables
account_sid = "AC1a2e909926f462233a69d2ec20f1a229"
auth_token = "ac30eaefd6b71f7139b50f27fc601b6f"

#estuary set up
url = "https://api.estuary.tech/content/add"

def send_message(phoneNum="+19259643840", coords="-20,-60"):
    payload={}
    files=[
    ('data',('file',open('static/BeforeImage.png','rb'),'application/octet-stream'))
    ]
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer EST78a8d35e-2d1f-42e5-8207-c784e49b4de0ARY'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response_txt = response.text
    url_s = (response_txt.find('estuary_retrieval_url'))+ 24
    url_e = (response_txt.find('estuaryId')) - 3 - url_s
    BeforeURL= (response_txt[url_s:url_s+url_e:1])
    print(BeforeURL)

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
    print(url_s,url_e)
    AfterURL= (response_txt[url_s:url_s+url_e:1])
    print(AfterURL)


    #Send Message
    client = Client(account_sid, auth_token)
    client.messages.create(
        to=phoneNum,
        from_="+19136758450",
        body=(f'You can view the before and after satelite images for {coords} coordinates deforestation report.\n{BeforeURL}\n\n{AfterURL}')
        )
