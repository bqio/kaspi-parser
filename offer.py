class Offer:
    def __init__(self, offer: dict) -> None:
        self.offer = offer
    
    def get_price(self) -> float:
        return float(self.offer['price'])

    def get_merchant_name(self) -> str:
        return self.offer['merchantName']
    
    def get_merchant_id(self) -> str:
        return self.offer['merchantId']