import streamlit as st

from streamlit_cookies_controller import CookieController
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth
from src.data_manager.client_data_manager import ClientDataManager
from streamlit.web.server.server import Server
from src.data_manager.client_data_manager import AnketeOpenData
from config import Config


def profile_page():
    manager = ClientDataManager()
    if not manager.is_logged_in:
        login_field = st.text_input("Login")
        password_field = st.text_input("Password")
        st.button("Sign in", on_click=lambda: manager.login(login_field, password_field))
        st.button("Sign up", on_click=lambda: manager.register(login_field, password_field))

    st.write("Profile page")
    if manager.is_logged_in:
        open_data = manager.open_data
        closed_data = manager.get_closed_info()
        keywords_data = manager.get_keywords()

        with st.form("profile_form"):
            st.subheader("Open Information")
            username = st.text_input("Username", value=open_data.username)
            fullname = st.text_input("Full Name", value=open_data.fullname)
            sex = st.radio("Sex", ["Male", "Female"], index=0 if open_data.sex.lower() not in ["male", "female"] else ["male", "female"].index(open_data.sex.lower()))
            age = st.number_input("Age", value=int(open_data.age) if open_data.age else 0, min_value=0, max_value=120, key="age_open_info")
            city = st.text_input("City", value=open_data.city)
            description = st.text_area("Description", value=open_data.description)

            st.subheader("Closed Information")
            phone_number = st.text_input("Phone Number", value=closed_data.get("number", "") if closed_data else "")

            st.subheader("Keywords")
            hobby = st.text_input("Hobby", value=keywords_data.get("hobby", "") if keywords_data else "")
            alcohol = st.text_input("Alcohol", value=keywords_data.get("alcohol", "") if keywords_data else "")
            smoking = st.text_input("Smoking", value=keywords_data.get("smoking", "") if keywords_data else "")
            sport = st.text_input("Sport", value=keywords_data.get("sport", "") if keywords_data else "")
            zodiac_sign = st.text_input("Zodiac Sign", value=keywords_data.get("zodiac_sign", "") if keywords_data else "")
            height = st.number_input("Height", value=int(keywords_data.get("height", 0)) if keywords_data and "height" in keywords_data else 0, min_value=0, max_value=300, key="height_keywords")
            why_here = st.text_area("Why Here", value=keywords_data.get("why_here", "") if keywords_data else "")
            marital_status = st.text_input("Marital Status", value=keywords_data.get("marital_status", "") if keywords_data else "")

            submitted = st.form_submit_button("Submit")
            if submitted:
                open_data.username = username
                open_data.fullname = fullname
                open_data.sex = sex
                open_data.age = age
                open_data.city = city
                open_data.description = description
            
                try:
                    manager.update_open_data(open_data)
                except Exception as e:
                    print(e) 
                manager.update_closed_info(phone_number)
                manager.update_keywords(hobby, alcohol, smoking, sport, zodiac_sign, height,  why_here, marital_status)
                st.success("Profile updated successfully!")

        st.markdown("---")

        st.button("Logout", on_click=lambda: manager.logout())