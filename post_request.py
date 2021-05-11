import requests
import json
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
          "--api_key",
          type=str,
          required=True,
          help="Your API Keys",
      )
      
parser.add_argument(
          "--lat",
          type=str,
          required=True,
          help="Your API Keys",
      )

parser.add_argument(
          "--lon",
          type=str,
          required=True,
          help="Your API Keys",
      )
parser.add_argument(
          "--model",
          type=str,
          required=True,
          help="Your API Keys",
      )

if len(sys.argv[1:]) == 0:
     parser.print_help()
     parser.exit()

args = parser.parse_args()

#API Endpoint
API_ENDPOINT = "https://api.windy.com/api/point-forecast/v2"

#Richiesta in JSON
source_code = {
      'lat': args.lat,
      'lon': args.lon,
      'model': args.model,
      'parameters': ['wind', 'dewpoint', 'rh', 'pressure'],
      'levels': ['surface', '800h', '300h'], 
      'key': args.api_key
      }

#Mando post request
headers = {'content-type': 'application/json'}
r = requests.post(url = API_ENDPOINT, data=json.dumps(source_code), headers=headers)

# Leggo risposta
pastebin_url = r.text
print("Responso del server:"+"  "+pastebin_url)
