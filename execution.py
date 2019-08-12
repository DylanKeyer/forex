import requests
from urllib.parse import urlencode


class Execution(object):
    def __init__(self, domain, access_token, account_id):
        self.domain = domain
        self.access_token = access_token
        self.account_id = account_id
        self.session = self.obtain_connection()

    def obtain_connection(self):
        return requests.Session()

    def execute_order(self, event):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer " + self.access_token
        }
        params = urlencode({
            "instrument" : event.instrument,
            "units" : event.units,
            "type" : event.order_type,
            "side" : event.side
        })
        response = self.session.post(
            self.domain + "/v1/accounts/%s/orders" % str(self.account_id),
            params, headers
        )
        print(response)