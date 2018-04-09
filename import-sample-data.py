import requests
from datetime import datetime
from cryptocoins.models import Cryptocurrency

response = requests.get('https://api.coinmarketcap.com/v1/ticker/')
for doc in response.json():
    doc['slug'] = doc['id']
    del doc['id']

    doc['volume_usd_24h'] = doc['24h_volume_usd']
    del doc['24h_volume_usd']

    doc['last_updated'] = datetime.fromtimestamp(int(doc['last_updated']))

    Cryptocurrency.objects.create(**doc)
