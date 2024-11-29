from enum import Enum, unique

from exchange.domain.currency import Currency


# Add currencies here
@unique
class Currencies(Enum):
    ABAN = Currency(code='ABAN', price=4)
