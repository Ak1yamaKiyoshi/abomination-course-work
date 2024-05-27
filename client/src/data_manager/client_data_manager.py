

import streamlit as st

from streamlit_cookies_controller import CookieController
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth
from src.api_client.api import APIClient

import time

from datetime import datetime, timedelta
now = datetime.now()
one_month_later = now + timedelta(days=30)


""" 
is_logged_in: bool
ankete_id: int
has_open_data
"""

class AnketeOpenData:
    def __init__(self,filled=None, username="", fullname="", sex="", age="", city="", description="") -> None:
        self.filled = filled
        self.username = username 
        self.fullname  = fullname
        self.sex = sex
        self.age = age
        self.city = city
        self.description = description


class ClientDataManager:
    def __init__(self) -> None:
        self.controller = CookieController()
        self.api_client = APIClient()

    @property
    def is_logged(self):
        res = self.get_data('is_logged_in')
        st.write(res)
        if res: return True
        else: return False

    @property
    def ankete_id(self):
        return self.get_data("ankete_id")

    @property 
    def open_data(self):
        res=  self.api_client.get_open_info(self.ankete_id)
        print("opendata" ,res)
        if res is not None:
            return AnketeOpenData(filled=True,
                username=res['username'],
                fullname=res['full_name'],
                sex=res['sex'],
                age=res['age'],
                city=res['city'],
                description=res['description'])
        return AnketeOpenData()

    def update_open_data(self, ankete_open_data: AnketeOpenData):
        res = self.api_client.post_open_info(
            self.ankete_id,
            ankete_open_data.username,
            ankete_open_data.fullname,
            ankete_open_data.sex,
            ankete_open_data.age,
            ankete_open_data.city,
            ankete_open_data.description,
        )
    


    def logout(self):
        self.set_data("is_logged_in", False)
        self.set_data("ankte_id", -1)

    def login(self, login_str, password_str):
        ankete_id = self.api_client.authenticate(login_str, password_str)

        if ankete_id is not None:
            self.set_data("is_logged_in", True)
            self.set_data("ankete_id",ankete_id)
            return True
        return False

    def register(self, login_str, password_str):
        ankete_id = self.api_client.register(login_str, password_str)
        if ankete_id:
            self.set_data("is_logged_in", True)
            self.set_data("ankete_id",ankete_id)
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
