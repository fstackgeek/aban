from rest_framework import serializers

from exchange.domain.currency import Currencies


class BuyRequestSerializer(serializers.Serializer):
    currency = serializers.CharField(max_length=10)
    amount = serializers.FloatField()
    user_id = serializers.CharField(max_length=50)

    def validate_currency(self, currency):
        try:
            return Currencies[currency].value
        except KeyError:
            raise serializers.ValidationError('Invalid currency')
