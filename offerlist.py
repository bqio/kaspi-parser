from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from offer import Offer

class OfferList:
    def __init__(self, offers: List[Offer]) -> None:
        self.offers = offers

    def get_min_price(self) -> float:
        return self.offers[0].get_price()
    
    def get_price_by_merchant_id(self, merchant_id: str) -> float:
        for offer in self.offers:
            if offer.get_merchant_id() == merchant_id:
                return offer.get_price()
        return None