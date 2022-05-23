import requests
import json
import random
import string
from config import Config

config = Config()

#create a random numbers with digits only
def random_number(digits_count):
    string_one = ''.join((random.choice(string.digits) for x in range(digits_count)))

    sam_list = list(string_one)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


class OrderMinimal(object):

    def __init__(
            self, 
            vendor: str = None, 
            order_id: str = None,
            buyer_email: str = None, 
            buyer_name: str = None, 
            buyer_phone: str = None, 
            amount: str = None, 
            currency: str = None, 
            redirect_url: str = None, 
            cancel_url: str = None, 
            webhook: str = None,
            buyer_remarks: str = None,
            merchant_remarks: str = None,
            no_of_items: str = None,
            header_colour: str = None,
            link_colour: str = None,
            button_colour: str = None,
            expiry: str = None,
    ):

        self.vendor = vendor
        self.order_id = order_id
        self.buyer_email = buyer_email
        self.buyer_name = buyer_name
        self.buyer_phone = buyer_phone
        self.amount = amount
        self.currency = currency
        self.redirect_url = redirect_url
        self.cancel_url = cancel_url
        self.webhook = webhook
        self.buyer_remarks = buyer_remarks
        self.merchant_remarks = merchant_remarks
        self.no_of_items = no_of_items
        self.header_colour = header_colour
        self.link_colour = link_colour
        self.button_colour = button_colour
        self.expiry = expiry


    def order_minimal_request():

        #making request to create a new minimal order in selcom API
        url = f'https://apigw.selcommobile.com/{config.MINIMAL_ORDER_REQUEST_URL}'

        payload = json.dumps({
            "vendor": config.VENDOR,
            "order_id": random_number(10),
            "buyer_email": "",
            "buyer_name": "",
            "buyer_phone": "",
            "amount": int(),
            "currency": "TZS",
            "no_of_items": 1,
            "webhook": "",
        })
        headers = {
            'Digest-Method': 'HS256',
            'Digest': "", #compose a signature
            'Authorization': 'SELCOM ',
            'Signed-Fields': '', #signed fields
            'Timestamp': "", #timestamp
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text