from kaspishop import KaspiShop
from time import sleep

CITY_ID = 710000000

PRODUCT_IDS = [
    100286960,
    107983749,
]

kaspi_shop = KaspiShop(CITY_ID)

for product_id in PRODUCT_IDS:
    product_title = kaspi_shop.get_product_title(product_id)
    print(product_title)