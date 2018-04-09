from django.db import models
from django.conf import settings


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    rank = models.IntegerField()
    market_cap_usd = models.DecimalField(max_digits=14, decimal_places=2)
    price_usd = models.DecimalField(max_digits=7, decimal_places=2)
    volume_usd_24h = models.DecimalField(max_digits=14, decimal_places=2)
    available_supply = models.DecimalField(max_digits=20, decimal_places=2)
    percent_change_24h = models.DecimalField(max_digits=5, decimal_places=2)

    # optional fields
    price_btc = models.DecimalField(
        max_digits=8, decimal_places=7, null=True, blank=True)
    total_supply = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    max_supply = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True)
    percent_change_1h = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    percent_change_7d = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Cryptocurrency'
        verbose_name_plural = 'Cryptocurrencies'

    def __str__(self):
        return '{} ({})'.format(self.name, self.symbol)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    avatar_picture_name = models.CharField(
        max_length=255, blank=True, default='')

    favorite_coins = models.ManyToManyField(Cryptocurrency)

    def __str__(self):
        return "Profile: {}".format(self.user)
