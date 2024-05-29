import streamlit as st

from streamlit_cookies_controller import CookieController
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth
from src.data_manager.client_data_manager import ClientDataManager
from streamlit.web.server.server import Server
from src.data_manager.client_data_manager import AnketeOpenData
from config import Config
from config import DefaultValues
import re
import numpy as np
import codecs
import sys

import base64
from PIL import Image
from io import BytesIO
import io

import chardet 
def image_to_base64_string(image_file):
    # Read the image file
    with open(image_file.name, "rb") as image_file:
        # Encode the image to base64
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

def to_bytes(s):
    if type(s) is bytes:
        return s
    elif type(s) is str or (sys.version_info[0] < 3 and type(s) is unicode):
        return codecs.encode(s, 'utf-8')
    else:
        raise TypeError("Expected bytes or string, but got %s." % type(s))

def profile_page():
    manager = ClientDataManager()
    if not manager.is_logged_in:
        login_field = st.text_input("Ваш логін")
        password_field = st.text_input("Ваш пароль")
        st.button("Вхід", on_click=lambda: manager.login(login_field, password_field))
        st.button("Реєстрація", on_click=lambda: manager.register(login_field, password_field))

    st.write("Ваш профіль")
    if manager.is_logged_in:
        open_data = manager.open_data or DefaultValues()
        closed_data = manager.get_closed_info() or {"number": DefaultValues.phone_number}
        keywords_data = manager.get_keywords() or {
            "hobby": DefaultValues.hobby,
            "alcohol": DefaultValues.alcohol,
            "smoking": DefaultValues.smoking,
            "sport": DefaultValues.sport,
            "zodiac_sign": DefaultValues.zodiac_sign,
            "height": DefaultValues.height,
            "why_here": DefaultValues.why_here,
            "marital_status": DefaultValues.marital_status,
        }

        #            submitted = st.form_submit_button("Submit")

        with st.form("profile_form"):    
            
            npstring = manager.get_profile_picture()
            if npstring:                
                image = np.array(eval(npstring))
                st.image(image, caption='Profile picture', use_column_width=True)

            uploaded_file = st.file_uploader("Choose a profile picture", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                img_array = np.array(image)
                
                st.image(image, caption='Profile picture', use_column_width=True)
                manager.update_profile_picture(str(img_array.tolist()))

            
            username = st.text_input("Ім'я або псевдонім", value=open_data.username)
            fullname = st.text_input("Повне Ім'я", value=open_data.fullname)
            sex_options = ["Male", "Female"]
            sex = st.radio("Стать", sex_options, index=sex_options.index(open_data.sex))
            age = st.number_input("Багато років?", value=int(open_data.age), min_value=16, max_value=120, key="age_open_info")
            city = st.text_input("Місто проживання", value=open_data.city)
            description = st.text_area("Опис анкети", value=open_data.description)
            phone_number = st.text_input("Номер телефону (видно тільки тим, кому ви надіслали лайк.)", value=closed_data.get("number", DefaultValues.phone_number), help="Enter a valid phone number in the format +123456789")

            st.markdown("---")
            st.subheader("Трошки деталей про вас")
            hobby = st.text_input("Ваші хобі: ", value=keywords_data.get("hobby", DefaultValues.hobby))
            alcohol_options = ["Non-drinker", "Social drinker", "Heavy drinker", DefaultValues.alcohol]
            alcohol = st.selectbox("Відношення до алкоголю: ", alcohol_options, index=alcohol_options.index(keywords_data.get("alcohol", DefaultValues.alcohol)))

            smoking_options = ["Non-smoker", "Social smoker", "Heavy smoker", DefaultValues.smoking]
            smoking = st.selectbox("Relation to smoking:", smoking_options, index=smoking_options.index(keywords_data.get("smoking", DefaultValues.smoking)))
            sport_options = ["None", "Occasional", "Regular", DefaultValues.sport]
            sport = st.selectbox("Sport", sport_options, index=sport_options.index(keywords_data.get("sport", DefaultValues.sport)))
            zodiac_sign_options = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", DefaultValues.zodiac_sign]
            zodiac_sign = st.selectbox("Знак зодіаку: ", zodiac_sign_options, index=zodiac_sign_options.index(keywords_data.get("zodiac_sign", DefaultValues.zodiac_sign)))
            height = st.number_input("Зрістt", value=int(keywords_data.get("height", DefaultValues.height)), min_value=140, max_value=250, key="height_keywords")
            why_here = st.text_area("Чому ви тут?", value=keywords_data.get("why_here", DefaultValues.why_here))
            marital_status_options = ["Single", "Married", "Divorced", "Widowed", DefaultValues.marital_status]
            marital_status = st.selectbox("Marital Status", marital_status_options, index=marital_status_options.index(keywords_data.get("marital_status", DefaultValues.marital_status)))

            submitted = st.form_submit_button("Submit")

            if submitted:
                if not re.match(r'^\+\d{10,15}$', phone_number):
                    st.error("Please enter a valid phone number in the format +123456789")
                    st.stop()

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
                manager.update_keywords(hobby, alcohol, smoking, sport, zodiac_sign, height, why_here, marital_status)
                st.success("Профіль успішно оновлено!")

        st.markdown("---")

        st.button("Вихід", on_click=lambda: manager.logout())