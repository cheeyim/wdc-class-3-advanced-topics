from django.forms import ModelForm
from cryptocoins.models import Cryptocurrency


class CryptocurrencyForm(ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = [
            'name',
            'slug',
            'symbol',
            'rank',
            'market_cap_usd',
            'price_usd',
            'volume_usd_24h',
            'available_supply',
            'percent_change_24h',
        ]
