class Config(object):

    """
    |--------------------------------------------------------------------------
    | API Key
    |--------------------------------------------------------------------------
    | Merchant API Key allocated by Selcom
    """
    API_KEY = ''

    """
    |--------------------------------------------------------------------------
    | API Secret
    |--------------------------------------------------------------------------
    | Merchant API Secret allocated by Selcom
    """
    API_SECRET = ''

    """
    |--------------------------------------------------------------------------
    | Vendor ID
    |--------------------------------------------------------------------------
    | Vendor/Merchant ID allocated by Selcom
    """
    VENDOR = ''

    """
    |--------------------------------------------------------------------------
    | Selcom Base URL
    |--------------------------------------------------------------------------
    | Selcom base url for the API
    """
    SELCOM_BASE_URL = 'https://apigw.selcommobile.com/'

    """
    |--------------------------------------------------------------------------
    | Webhook URL
    |--------------------------------------------------------------------------
    | Merchant webhook url that will be listening callbacks from Selcom, It must accept POST request
    | Eg: https://shop.co.tz/checkout/webhook
    """
    WEBHOOK_URL = ''

    """
    |--------------------------------------------------------------------------
    | Redirect URL
    |--------------------------------------------------------------------------
    | Merchant page url that the customer should be redirected after payment process is complete
    | Eg: https://shop.co.tz/checkout/redirect
    """
    REDIRECT_URL = ''

    """
    |--------------------------------------------------------------------------
    | Cancel URL
    |--------------------------------------------------------------------------
    | Merchant page url that the customer should be redirected when payment process canceled by the buyer
    | Eg: https://shop.co.tz/checkout/cancel
    """
    CANCEL_URL = ''

    """
    |--------------------------------------------------------------------------
    | Colors
    |--------------------------------------------------------------------------
    | Colors for the merchant pay,ment page
    """
    COLORS = {
        'header': '',
        'link': '',
        'button': '',
    }


#Configuration for creating a new order for processing payments (Including card payments)
class CreateOrderConfig(Config):
    REQUEST_URL = 'v1/checkout/create-order'


#Configuration for creating a new minimal order for processing payments (does not support card payments)
class CreateOrderConfig(Config):
    REQUEST_URL = 'v1/checkout/create-order-minimal'