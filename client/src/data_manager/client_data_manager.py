import streamlit as st
from config import DefaultValues
from streamlit_cookies_controller import CookieController
from src.api_client.api import APIClient
from datetime import datetime, timedelta
import base64
from io import BytesIO
from PIL import Image

now = datetime.now()
one_month_later = now + timedelta(days=30)

class AnketeOpenData:
    def __init__(self, filled=None, username="", fullname="", sex="", age="", city="", description="", profile_picture=None):
        self.filled = filled
        self.username = username
        self.fullname = fullname
        self.sex = sex
        self.age = age
        self.city = city
        self.description = description
        self.profile_picture = profile_picture

class ClientDataManager:
    def __init__(self):
        self.controller = CookieController()
        self.api_client = APIClient()

    @property
    def is_logged_in(self):
        return self.get_data('is_logged_in')

    @property
    def ankete_id(self):
        return self.get_data("ankete_id")

    @property
    def open_data(self):
        res = self.api_client.get_open_info(self.ankete_id)
        if res is not None:
            return AnketeOpenData(
                filled=True,
                username=res['username'],
                fullname=res['full_name'],
                sex=res['sex'],
                age=res['age'],
                city=res['city'],
                description=res['description'],
            )
        return AnketeOpenData()

    def update_open_data(self, ankete_open_data: AnketeOpenData):

        return self.api_client.put_open_info(
            self.ankete_id,
            ankete_open_data.username,
            ankete_open_data.fullname,
            ankete_open_data.sex,
            ankete_open_data.age,
            ankete_open_data.city,
            ankete_open_data.description,
        )

    def get_closed_info(self):
        return self.api_client.get_closed_info(self.ankete_id)

    def update_closed_info(self, phone_number):
        return self.api_client.put_closed_info(self.ankete_id, phone_number)

    def get_password_restoration(self):
        return self.api_client.get_password_restoration(self.ankete_id)

    def update_password_restoration(self, code):
        return self.api_client.put_password_restoration(self.ankete_id, code)

    def get_keywords(self):
        return self.api_client.get_keywords(self.ankete_id)

    def update_keywords(self, hobby, alcohol, smoking, sport, zodiac_sign, height, why_here, marital_status):
        return self.api_client.put_keywords(
            self.ankete_id,
            hobby,
            alcohol,
            smoking,
            sport,
            zodiac_sign,
            height,
            why_here,
            marital_status
        )


    def update_profile_picture(self, image_str):
        return self.api_client.put_profiel_picture(self.ankete_id, image_str)

    def get_profile_picture(self):
        return self.api_client.get_profile_picture(self.ankete_id)
            
    def get_ankete(self):
        return self.api_client.get_ankete(self.ankete_id)

    def get_invitation_to_ankete(self, invitation_to_ankete_id):
        return self.api_client.get_invitation_to_ankete(invitation_to_ankete_id)

    def post_invitation_to_ankete(self):
        return self.api_client.post_invitation_to_ankete(self.ankete_id)

    def get_invitation(self, invitation_id):
        return self.api_client.get_invitation(invitation_id)

    def post_invitation(self, from_id, to_id, description, photo=None, video=None):
        return self.api_client.post_invitation(from_id, to_id, description, photo, video)

    def logout(self):
        self.set_data("is_logged_in", False)
        self.set_data("ankete_id", -1)

    def login(self, login_str, password_str):
        ankete_id = self.api_client.authenticate(login_str, password_str)

        if ankete_id is not None:
            self.set_data("is_logged_in", True)
            self.set_data("ankete_id", ankete_id)
            return True
        return False


    def register(self, login_str, password_str):
        ankete_id = self.api_client.post_ankete(login_str, password_str)
        self.api_client.post_profile_picture(ankete_id)
        self.api_client.post_open_info(
            ankete_id,
            DefaultValues.username,
            DefaultValues.fullname,
            DefaultValues.sex,
            DefaultValues.age,
            DefaultValues.city,
            DefaultValues.description,
            ""
        )
        self.api_client.post_keywords(
            ankete_id,
            DefaultValues.hobby,
            DefaultValues.alcohol,
            DefaultValues.smoking,
            DefaultValues.sport,
            DefaultValues.zodiac_sign,
            DefaultValues.height,
            DefaultValues.age,
            DefaultValues.why_here,
            DefaultValues.marital_status
        )
        self.api_client.post_closed_info(ankete_id, 0)
        if ankete_id:
            self.set_data("is_logged_in", True)
            self.set_data("ankete_id", ankete_id)
            return True
        return False

    def set_data(self, key, value):
        st.session_state[key] = value
        self.controller.set(key, value, expires=one_month_later)

    def get_data(self, key):
        session_state = st.session_state.get(key)
        try:
            cookies = self.controller.get(key)
        except:
            cookies = None

        if not cookies:
            return session_state
        else:
            return cookies

    def del_data(self, key):
        self.controller.remove(key)