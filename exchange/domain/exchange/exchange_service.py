from .external_exchange_service import ExternalExchangeService
from exchange.domain.wallet import WalletService


class ExchangeService:

    @staticmethod
    def buy_currency(user_id, currency, amount):
        dollar_balance, currency_balance = WalletService.buy_currency(user_id, currency, amount)
        ExternalExchangeService.place_order(currency, amount)
        return dollar_balance, currency_balance
