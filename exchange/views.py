from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.domain.currency import Currency
from exchange.domain.exchange import ExchangeService
from exchange.serializers import BuyRequestSerializer

"""
Note:
User management (signup, login, etc.) is ignored for simplicity (because it wasn't in the scope of the task)
The userId is taken in the body of the request. But in the real case, this API would need authentication
and the userId would come from there.
"""


class BuyCurrencyView(APIView):
    exchange = ExchangeService()

    def post(self, request):
        try:
            serializer = BuyRequestSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            user_id = serializer.validated_data["user_id"]
            currency = serializer.validated_data["currency"]
            amount = serializer.validated_data["amount"]

            dollar_balance, currency_balance = self.exchange.buy_currency(user_id, currency, amount)

            return Response(
                ResponseDto(dollar_balance, currency_balance, currency).to_dict(), status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            if isinstance(e, AssertionError) or isinstance(e, ValueError):
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ResponseDto:
    def __init__(self, dollar_balance, currency_balance, currency: Currency) -> None:
        self.dollar_balance = dollar_balance
        self.currency_balance = currency_balance
        self.currency = currency

    def to_dict(self):
        return {"dollar_balance": self.dollar_balance, f"{self.currency.code}_balance": self.currency_balance}
