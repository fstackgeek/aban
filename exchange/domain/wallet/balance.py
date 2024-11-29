from django.db import models

from .wallet import Wallet


class Balance(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='balances')
    currency = models.CharField(max_length=10)
    balance = models.FloatField(default=0.0)

    class Meta:
        unique_together = ("wallet", "currency")
