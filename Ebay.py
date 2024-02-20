import asyncio
import json
import os
from urllib.request import urlopen

import requests
from dotenv import load_dotenv
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

import imports


apiKey = asyncio.run(imports.get_ebay_auth_token(os.environ.get("CLIENT_ID"), os.environ.get("CLIENT_SECRET")))
print(apiKey)

headers = {'Authorization': "Bearer " + apiKey}




#url = "https://api.ebay.com/buy/browse/v1/item_summary/search?q=CyberJudge"


url1 = """https://api.ebay.com/buy/browse/v1/item_summary/search?q=CyberJudge Booster Box
&SECURITY-APPNAME=""" + apiKey + """
&category_ids=261044
&limit=100
&auto_correct=KEYWORD&limit=4
&filter=price:[50..100],priceCurrency:USD
&fieldgroups=ASPECT_REFINEMENTS
&fieldgroups=EXTENDED,MATCHING_ITEMS&aspect_filter=categoryId:261044
&sort=price"""


#apiResult = requests.get(url1, headers=headers)
#print(apiResult)
#parseddoc = apiResult.json()

#print(apiResult.text)


class Ebay(object):
    def __init__(self, apiKey):
        self.apiKey = apiKey
        
    def search(self):
        pass
    
    def parse(self):
        pass

EbayAPI = Ebay(apiKey)

EbayAPI.search()
