import requests
import json

url = "http://localhost:5051/v1/schemata"

payload = json.dumps({
  "id": "<uuid>",
  "title": "<string>",
  "author": {
    "login": "<string>",
    "roles": [
      "NannyModerator",
      "Guest"
    ],
    "mediumPictureUrl": "<string>",
    "smallPictureUrl": "<string>",
    "status": "<string>",
    "rating": {
      "enabled": "<boolean>",
      "quality": "<integer>",
      "quantity": "<integer>"
    },
    "online": "<dateTime>",
    "name": "<string>",
    "location": "<string>",
    "registration": "<dateTime>"
  },
  "type": "Private",
  "specifications": [
    {
      "id": "<uuid>",
      "title": "<string>",
      "required": "<boolean>",
      "type": "String",
      "minValue": "<integer>",
      "maxValue": "<integer>",
      "maxLength": "<integer>",
      "values": [
        {
          "value": "<string>",
          "modifier": "<integer>"
        },
        {
          "value": "<string>",
          "modifier": "<integer>"
        }
      ]
    },
    {
      "id": "<uuid>",
      "title": "<string>",
      "required": "<boolean>",
      "type": "List",
      "minValue": "<integer>",
      "maxValue": "<integer>",
      "maxLength": "<integer>",
      "values": [
        {
          "value": "<string>",
          "modifier": "<integer>"
        },
        {
          "value": "<string>",
          "modifier": "<integer>"
        }
      ]
    }
  ]
})
headers = {
  'X-Dm-Auth-Token': '<string>',
  'X-Dm-Bb-Render-Mode': '<string>',
  'Content-Type': 'application/json',
  'Accept': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
