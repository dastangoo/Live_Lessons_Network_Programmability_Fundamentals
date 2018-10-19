import requests
import urllib3
import json

urllib3.disable_warnings()

CONTROLLER_IP = "sandboxapicem.cisco.com"
GET = "get"
POST = "post"

def getServiceTicket():
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
    ticket = r_json["response"]["serviceTicket"]
  return ticket

def doRestCall(aTicket, command, url, aData=None):
  response_json = None
  payload = None
  if aData != None:
    payload = json.dumps(aData)
  header = {
    "content-type": "application/json",
    "X-Auth-Token": aTicket
  }

  if command == GET:
    r = requests.get(url, data=payload, headers=header, verify=False)
  elif command == POST:
    r = requests.post(url, data=payload, headers=header, verify=False)
  else:
    print("Unknown Command")

  if not r:
    print("No data returned!")
  else:
    response_json = r.json()
    r1 = response_json["response"][0]['hostIp']
    print("Host IP = " + r1)

def main():
  ticket = getServiceTicket()
  if ticket:
    doRestCall(ticket, GET, "https://" + CONTROLLER_IP + "/api/v1/host")
  else:
    print("No service ticket was received. Ending the program!")

main()