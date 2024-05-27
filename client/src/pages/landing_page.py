
import streamlit as st

from streamlit_cookies_controller import CookieController
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth
from src.data_manager.client_data_manager import ClientDataManager


def landing_page():
    manager = ClientDataManager()
    st.write("jhe;l")
