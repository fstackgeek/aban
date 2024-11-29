from django.urls import path

from exchange.views import BuyCurrencyView
urlpatterns = [
    path('buy/', BuyCurrencyView.as_view(), name='buy-currency')
]
