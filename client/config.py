import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    api_acces_token = os.getenv("AUTH_API_KEY")
    api_base_url = "http://127.0.0.1:8000"  

class DefaultValues:
    username = "None"
    fullname = "None"
    sex = "Male"
    age = 25
    city = "None"
    description = "No description provided."
    phone_number = "+11234567890"
    hobby = "None"
    alcohol = "None"
    smoking = "None"
    sport = "None"
    zodiac_sign = "None"
    height = 175
    why_here = "None"
    marital_status = "None"