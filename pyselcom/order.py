import requests
import json
import random
import string
import pytz
from pytz import timezone
from datetime import datetime, timedelta
from config import Config

config = Config()

#create a random numbers with digits only
def random_number(digits_count):
    string_one = ''.join((random.choice(string.digits) for x in range(digits_count)))

    sam_list = list(string_one)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


eastern = timezone('Africa/Dar_es_Salaam')

#create a signatuure
def compute_signature(parameters, signed_fields, request_timestamp, api_secret):
    pass


class OrderMinimal(object):

    def __init__(
            self, 
            vendor: str = None, 
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

        self._vendor = vendor
        self._buyer_email = buyer_email
        self._buyer_name = buyer_name
        self._buyer_phone = buyer_phone
        self._amount = amount
        self._currency = currency
        self._redirect_url = redirect_url
        self._cancel_url = cancel_url
        self._webhook = webhook
        self._buyer_remarks = buyer_remarks
        self._merchant_remarks = merchant_remarks
        self._no_of_items = no_of_items
        self._header_colour = header_colour
        self._link_colour = link_colour
        self._button_colour = button_colour
        self._expiry = expiry


        @property
        def vendor(self):

            return  self._vendor

        @vendor.setter
        def vendor(self, vendor: str):

            if None:
                return "Vendor ID is required"
            
            self._vendor = vendor
        

        @property
        def buyer_email(self):

            return  self._buyer_email

        @buyer_email.setter
        def vendor(self, buyer_email: str):

            if None:
                return "Buyer email is required"
            
            self._buyer_email = buyer_email
        

        @property
        def buyer_name(self):

            return  self._buyer_name

        @buyer_name.setter
        def buyer_name(self, buyer_name: str):

            if None:
                return "Buyer name is required"
            
            self._buyer_name = buyer_name
    
        @property
        def buyer_phone(self):

            return  self._buyer_phone

        @buyer_phone.setter
        def buyer_phone(self, buyer_phone: str):

            if None:
                return "Buyer Phone is required"
            
            self._buyer_phone = buyer_phone
        

        @property
        def amount(self):

            return  self._amount

        @amount.setter
        def amount(self, amount: str):

            if None:
                return "amount is required"
            
            self._amount = amount
        


    def order_minimal_request(buyer_email, buyer_name, buyer_phone, amount):

        #making request to create a new minimal order in selcom API
        url = f'https://apigw.selcommobile.com/{config.MINIMAL_ORDER_REQUEST_URL}'

        payload_data = {}



        payload = json.dumps({
            "vendor": config.VENDOR,
            "order_id": random_number(10),
            "buyer_email": buyer_email,
            "buyer_name": buyer_name,
            "buyer_phone": buyer_phone,
            "amount": int(amount),
            "currency": "TZS",
            "no_of_items": 1,
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