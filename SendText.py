import requests
import os
from dotenv import load_dotenv

class SendText():
    load_dotenv()

    def __init__(self, key, phone, url, time, order, message):
        self.key = key
        self.phone = phone
        self.url = url
        self.time = time
        self.order = order
        self.message = message


        response = requests.post('https://textbelt.com/text', {
            'phone': self.phone,
            'message': self.message,
            'key': self.key
        })
        print("response: ", response.json())

    

