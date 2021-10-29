import os
import degiroapi
from dotenv import load_dotenv

# Load .env file
load_dotenv()

from degiroapi.product import Product

username = os.getenv('DEGIRO_USERNAME')
password = os.getenv('DEGIRO_PASSWORD')

degiro = degiroapi.DeGiro()
degiro.login(username, password)


def getGMEprice():
    products = degiro.search_products('GameStop Corp')

    realprice = degiro.real_time_price(Product(products[0]).id, degiroapi.Interval.Type.One_Day)

    return round(float(realprice[0]['data']['lastPrice']), 2), round(float(realprice[0]['data']['relDiff'] * 100), 2)


def getpfizerprice():
    products = degiro.search_products('Pfizer')

    realprice = degiro.real_time_price(Product(products[0]).id, degiroapi.Interval.Type.One_Day)

    return round(float(realprice[0]['data']['lastPrice']), 2), round(float(realprice[0]['data']['relDiff'] * 100), 2)


def getamdprice():
    products = degiro.search_products('Advanced Micro Devices')

    info = degiro.product_info(Product(products[0]).id)

    print(info)

    # realprice = degiro.real_time_price(int(Product(products[0]).id), degiroapi.Interval.Type.One_Day)
	
    # print(Product(products[0]).id)

    # return round(float(realprice[0]['data']['lastPrice']), 2), round(float(realprice[0]['data']['relDiff'] * 100), 2)


def getshellprice():
    products = degiro.search_products('Royal Dutch Shell')
    realprice = degiro.real_time_price(Product(products[0]).id, degiroapi.Interval.Type.One_Day)

    return round(float(realprice[0]['data']['lastPrice']), 2), round(float(realprice[0]['data']['relDiff'] * 100), 2)


getamdprice()