from unittest.mock import patch
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from exchange.domain.wallet import Wallet


class BuyCurrencyTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user(username='user', password='Password')
        Wallet.objects.create(user=user, dollar_balance=100)

    def test_successful_purchase(self):
        response = self.client.post('/api/buy/', {
            "currency": "ABAN",
            "amount": 10,
            "user_id": 1
        }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['dollar_balance'], 60)
        self.assertEqual(response.data['ABAN_balance'], 10)

    def test_keeping_accounts_after_multiple_purchases(self):
        for i in range(4):
            response = self.client.post('/api/buy/', {
                "currency": "ABAN",
                "amount": 2,
                "user_id": 1
            }, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['dollar_balance'], 68)
        self.assertEqual(response.data['ABAN_balance'], 8)

    def test_insufficient_funds(self):
        response = self.client.post('/api/buy/', {
            "currency": "ABAN",
            "amount": 100,
            "user_id": 1
        }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Insufficient funds')

    @patch('exchange.domain.exchange.external_exchange_service.ExternalExchangeService._buy_from_exchange')
    def test_external_exchange_batching(self, mock_buy_from_exchange):
        mock_buy_from_exchange.return_value = True
        for i in range(3):
            self.client.post('/api/buy/', {
                "currency": "ABAN",
                "amount": 1,
                "user_id": 1
            }, format='json')
        self.assertEqual(mock_buy_from_exchange.call_count, 1)
        currency_code, amount = mock_buy_from_exchange.call_args[0]
        self.assertEqual(currency_code, 'ABAN')
        self.assertEqual(amount, 12)
