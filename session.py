import requests

session = requests.Session()
session.headers.update({
    'Host': 'kaspi.kz',
    'Origin': 'https://kaspi.kz',
    'Referer': 'https://kaspi.kz/shop/p/',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept': 'application/json, text/*',
    'Cookie': 'redirected=true; locale=ru-RU; ssaid=cbfcf860-0b65-11ee-9d37-d925727a2869; test.user.group=58; test.user.group_exp=57; test.user.group_exp2=82',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
})