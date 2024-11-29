from django.db import transaction
from exchange.domain.currency import Currency
from exchange.domain.wallet import Wallet, Balance


class WalletService:

    @staticmethod
    def buy_currency(user_id, currency: Currency, amount: float):
        if amount <= 0:
            raise ValueError('Amount must be positive')
        dollar_amount = currency.get_dollar_value(amount)
        wallet = Wallet.objects.get(user_id=user_id)
        if wallet.dollar_balance < dollar_amount:
            raise AssertionError('Insufficient funds')

        with transaction.atomic():
            wallet.dollar_balance -= dollar_amount
            balance, created = Balance.objects.get_or_create(
                wallet=wallet,
                currency=currency.code,
                defaults={'balance': amount}
            )
            if not created:
                balance.balance += amount
            balance.save()
            wallet.save()

        return wallet.dollar_balance, balance.balance
