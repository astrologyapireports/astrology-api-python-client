import sdk.ApiReportsClient as sdk
import json

userID = '2'
apiKey = '986e781559edbb32e805d4b135780812'

# make some dummy data in order to call Astrology Api Reports API
data = {
  'day'  : 15,
  'month': 9,
  'year' : 1994,
  'hour' : 12,
  'min'  : 30,
  'lat'  : 28.6139,
  'lon'  : 77.1025,
  'tzone': 5.5
}

# api name which is to be called
resource = 'astro_details'

# instantiate ApiReportsClient class
client = sdk.ApiReportsClient(userID, apiKey)

# Set api response language
client.setLanguage('en')

# call JSON apis
responseData = client.callJsonApi(resource, data)

loaded_json = json.loads(responseData.text)

print(responseData.text)  # <== prints raw json response.
print(loaded_json)  # <== prints json response.
print(json.dumps(loaded_json, indent = 3)) # <== prints fromatted json response.
print(' ')
print('ASCENDANT : ' + loaded_json['data']['ascendant'])  # <== prints single key