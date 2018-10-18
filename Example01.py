import requests
import urllib3
import json

urllib3.disable_warnings()

CONTROLLER_IP = "sandboxapicem.cisco.com"
payload = {
  "username": "devnetuser",
  "password": "Cisco123!"
}
url = "https://" + CONTROLLER_IP + "/api/v1/ticket"
header = {
  "content-type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)

if (not response):
  print("No data returned!")
else:
  r_json = response.json()
  print(r_json)
  ticket = r_json["response"]["serviceTicket"]
  print("Ticket: " + ticket)