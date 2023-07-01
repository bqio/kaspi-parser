from offer import Offer
from offerlist import OfferList
from session import session

URL_OFFER_LIST = "https://kaspi.kz/yml/offer-view/offers/{}"
URL_TITLE = "https://kaspi.kz/yml/product-view/pl/filters?text={}"

class KaspiShop:
    def __init__(self, city_id: int) -> None:
        self.city_id = city_id
    
    def get_product_offer_list(self, product_id: int) -> OfferList:
        payload = {
            "cityId": self.city_id,
            "id": product_id,
            "limit": 60,
            "page": 0,
            "sort": True,
            "installationId": -1
        }
        response = session.post(URL_OFFER_LIST.format(product_id), json=payload)
        json = response.json()
        offers = []
        for offer in json.get('offers'):
            offers.append(Offer(offer))
        return OfferList(offers)
    
    def get_product_title(self, product_id: int) -> str:
        response = session.get(URL_TITLE.format(product_id))
        json = response.json()
        return json.get('data').get('cards')[0].get('title')