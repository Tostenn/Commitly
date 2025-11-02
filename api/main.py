from flask import Flask, request, jsonify
from g4f.client import Client
from g4f import models
from json import dumps
import logging
import asyncio
from os import getenv
from random import choice

# 🔒 Patch définitif : désactiver PollinationsAI pour éviter les crashs
import g4f.Provider.PollinationsAI
def disable_pollinations():
    return []
g4f.Provider.PollinationsAI.get_models = staticmethod(disable_pollinations)

# ✅ Timeout + retry global pour requests
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
adapter = HTTPAdapter(
    max_retries=Retry(total=2, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
)
session.mount("http://", adapter)
session.mount("https://", adapter)
requests.get = session.get  # remplace globalement requests.get

# ⚙️ Fix Windows asyncio
from sys import platform
if platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class MessageService:
    DEFAULT_MODEL = models.gpt-4o-mini
    
    client = Client()

    @classmethod
    def get_response(cls, prompt, content):
        if not content:
            return {"error": "Contenu manquant."}, 400

        try:
            response = cls.client.chat.completions.create(
                model=cls.DEFAULT_MODEL,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": dumps(content)}
                ]
            )
            return {"response": response.choices[0].message.content}, 200

        except Exception as e:
            logging.error(f"[MessageService] Erreur: {str(e)}")
            return {"error": "Erreur lors de la génération de réponse."}, 500


class API:
    def __init__(self):
        self.app = Flask(__name__)
        self.routes()

    def routes(self):
        @self.app.route('/commit', methods=['POST'])
        def commit():
            data = request.json
            response = MessageService.get_response(
                prompt=data.get('prompt'),
                content=data.get('content')
            )
            return jsonify(response[0]), response[1]

    def run(self):
        port = int(getenv("PORT", 10000))
        self.app.run(host="0.0.0.0", port=port)
        # self.app.run(port=5050)


api = API()
app = api.app

if __name__ == '__main__':
    api.run()
