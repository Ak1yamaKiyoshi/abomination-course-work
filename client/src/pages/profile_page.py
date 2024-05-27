
import streamlit as st

from streamlit_cookies_controller import CookieController
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth
from src.data_manager.client_data_manager import ClientDataManager
from streamlit.web.server.server import Server
from src.data_manager.client_data_manager import AnketeOpenData


def profile_page():
    manager = ClientDataManager()
    if not manager.is_logged:
        login_field =  st.text_input("Login")
        password_field = st.text_input("Password")
        st.button("Sign in", 
            on_click=lambda: manager.login(login_field, password_field))
        st.button("Sign up",
            on_click=lambda: manager.register(login_field, password_field))

    st.write("Profile page")
    if manager.is_logged:
        open_data = manager.open_data
        
        with st.form("profile_form"):
            username = st.text_input("Username", value=open_data.username)
            fullname = st.text_input("Full Name", value=open_data.fullname)
            sex = st.radio("Sex", ["Male", "Female"], index=["Male", "Female"].index(open_data.sex) if open_data.sex else 0)
            age = st.number_input("Age", value=int(open_data.age) if open_data.age else 0, min_value=0, max_value=120)
            city = st.text_input("City", value=open_data.city)
            description = st.text_area("Description", value=open_data.description)

            submitted = st.form_submit_button("Submit")
            if submitted:
                open_data.username = username
                open_data.fullname = fullname
                open_data.sex = sex
                open_data.age = str(age)
                open_data.city = city
                open_data.description = description

                manager.update_open_data(open_data)
                st.success("Profile updated successfully!")

        st.markdown("---")
    
        st.button("Logout",
            on_click=lambda: manager.logout())
    
