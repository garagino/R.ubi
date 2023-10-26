import json
import requests
from decouple import config


class GptApi:
    def __init__(self) -> None:
        self.__token = config('TOKEN')
        self.__link = 'https://api.openai.com/v1/chat/completions'
        self.__model = 'gpt-3.5-turbo'
    
    def __create_body_and_header(self, message=None):
        self.headers = {'Authorization': f'Bearer {self.__token}', 'Content-Type': 'application/json'}
        self.body_message = {
            'model': self.__model,
            'messages': [{'role': 'user', 'content': message}]
        }

        self.body_message = json.dumps(self.body_message)
    
    def send_prompt(self, message:str):        
        self.__create_body_and_header(message)

        self.request = requests.post(self.__link, headers=self.headers, data=self.body_message)

        self.response = self.request.json()

        return self.response
    
    def get_body_and_header(self):
        self.__create_body_and_header()

        return {'header': self.headers,
                'body': self.body_message}
