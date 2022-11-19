import re
from urllib import response
from django.conf import settings
import requests
from requests.adapters import HTTPAdapter, Retry

class Paystack:
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    base_url = 'https://api.paystack.co'
    #base_url = 'https://api.paystack.co/transaction/verify/:reference'

    
    def verify_payment(self, ref, *args, **kwargs):
        path = f'transaction/verify/:{ref}'

        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            'content-type': 'application/json',
        }

        url = self.base_url + path
        #response = request.get(url, headers = headers)
  
        # try:
        #     response = requests.get(url, headers = headers,  timeout=5)
        #     if response.status_code == 200:
        #         response_data = response.json()
        #         return response_data['status'], response_data['data']
            
        #     response_data = response.json()
        #     return response_data['status'], response_data['data']
        # except requests.exceptions.ConnectionError as e:
        #     response = "error"


        response = requests.get(url, headers = headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']
