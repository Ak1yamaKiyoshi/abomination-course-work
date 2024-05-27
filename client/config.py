import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    api_acces_token = os.getenv("AUTH_API_KEY")
    api_base_url = "http://127.0.0.1:8000/"  

