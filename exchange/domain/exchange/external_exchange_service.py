from django.core.cache import cache

from exchange.domain.currency import Currency

min_purchase_amount_in_dollars = 10
ACCUMULATED_AMOUNT = 'ACCUMULATED_AMOUNT'
redis_client = cache.client.get_client()


class ExternalExchangeService:

    @staticmethod
    def place_order(currency: Currency, amount: float):
        current_amount = redis_client.hincrbyfloat(ACCUMULATED_AMOUNT, currency.code, amount)
        current_amount_in_dollars = currency.get_dollar_value(current_amount)
        if current_amount_in_dollars >= min_purchase_amount_in_dollars:
            ExternalExchangeService._buy_from_exchange(currency.code, current_amount_in_dollars)
            redis_client.hset(ACCUMULATED_AMOUNT, currency.code, 0)

    @staticmethod
    def _buy_from_exchange(currency: str, amount: float):
        print(f"Buying {amount} dollars of {currency}")
        # http call to the external exchange
        # if is successful:
        return True
        # else raise exception
