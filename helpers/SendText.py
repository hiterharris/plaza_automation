import requests
import os
from dotenv import load_dotenv

class SendText():
    load_dotenv()

    def __init__(self, message):
        key = os.environ.get("TEXT_API_KEY")
        phone = os.environ.get("PHONE")
        self.message = message

        response = requests.post('https://textbelt.com/text', {
            'key': key,
            'phone': phone,
            'message': self.message
        })
        
        print("response: ", response.json())