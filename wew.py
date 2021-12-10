import requests
import json
keys = {
    'bitcoin':'AED',
    'aff':'GTQ',
    'dollar':'INR'
}
res = requests.get(f'https://api.fastforex.io/fetch-one?from=AED&to=GTQ&api_key=a8c5d78b71-4bb800ad36-r3wgyn')
print(json.loads(res.content)['result'][keys[base]])
