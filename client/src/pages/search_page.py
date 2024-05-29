import streamlit as st
from src.data_manager.client_data_manager import ClientDataManager
from config import DefaultValues
from src.api_client.api import APIClient
import numpy as np
from PIL import Image


from streamlit_modal import Modal
from PIL import Image
import numpy as np
import random as rd


def handle_click(label, ankete_id=None):
    if "expanded" not in st.session_state:
        st.session_state.expanded = {}

    if ankete_id not in st.session_state.expanded:
        st.session_state.expanded[ankete_id] = False

  
             
                
                
def display_profile(profile_pic, user_data1, user_data2):

    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            if profile_pic is not None:
                st.image(profile_pic, use_column_width=True)
        with col2:
            st.subheader("Profile Details")
            st.write(f"Username: {user_data2['username']}")
            st.write(f"Sex: {user_data2['sex']}")
            st.write(f"Age: {user_data2['age']}")
            st.write(f"City: {user_data2['city']}")
            st.write(f"Description: {user_data2['description']}")
            st.write(f"Hobby: {user_data1['hobby']}")
            st.write(f"Alcohol: {user_data1['alcohol']}")
            st.write(f"Smoking: {user_data1['smoking']}")
            st.write(f"Sport: {user_data1['sport']}")
            st.write(f"Zodiac Sign: {user_data1['zodiac_sign']}")
            st.write(f"Height: {user_data1['height']} cm")
            st.write(f"Why Here: {user_data1['why_here']}")
            st.write(f"Marital Status: {user_data1['marital_status']}")


        description = st.text_input("Invite description: ", key=f"des_ankete_id:{user_data1['ankete_id']}")
        clicked = st.button("send", key=f"but_ankete_id:{user_data1['ankete_id']}")
        if clicked:
            send_invitation(user_data1['ankete_id'], description, "1")  
    

def search_keywords(res):
    api_client = APIClient()
    for ankete_ in res:
        ankete_id = ankete_.get('ankete_id')
        profile_pic = api_client.get_profile_picture(ankete_id)
        ankete_open_info = api_client.get_open_info(ankete_id)
        if profile_pic and len(profile_pic) > 1:                
            try:
                image = np.array(eval(profile_pic))
            except:
                image= None
        data_to_display = (image, ankete_, ankete_open_info) 
        yield data_to_display, ankete_id


def send_invitation(ankete_id, description, photo):
    manager = ClientDataManager()
    api_client = APIClient()
    api_client.post_invitation(manager.ankete_id, ankete_id, description)
 
keywords_data = {}
def search_page():
    
        # send_invitation(st.session_state["to_send"])
    global keywords_data, clicked

    manager = ClientDataManager()
    api_client = APIClient()

    st.markdown("# Find your love quicker.")

    show_filters = st.expander("Show Filters")

    with show_filters:
        alcohol_options = ["Non-drinker", "Social drinker", "Heavy drinker", DefaultValues.alcohol]
        alcohol = st.selectbox("Relation to alcohol: ", alcohol_options, index=alcohol_options.index(keywords_data.get("alcohol", DefaultValues.alcohol)))

        smoking_options = ["Non-smoker", "Social smoker", "Heavy smoker", DefaultValues.smoking]
        smoking = st.selectbox("Relation to smoking:", smoking_options, index=smoking_options.index(keywords_data.get("smoking", DefaultValues.smoking)))

        sport_options = ["None", "Occasional", "Regular", DefaultValues.sport]
        sport = st.selectbox("Sport", sport_options, index=sport_options.index(keywords_data.get("sport", DefaultValues.sport)))

        zodiac_sign_options = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", DefaultValues.zodiac_sign]
        zodiac_sign = st.selectbox("Your zodiac sign: ", zodiac_sign_options, index=zodiac_sign_options.index(keywords_data.get("zodiac_sign", DefaultValues.zodiac_sign)))

        height = st.number_input("Height", value=int(keywords_data.get("height", DefaultValues.height)), min_value=140, max_value=250, key="height_keywords")

        marital_status_options = ["Single", "Married", "Divorced", "Widowed", DefaultValues.marital_status]
        marital_status = st.selectbox("Marital Status", marital_status_options, index=marital_status_options.index(keywords_data.get("marital_status", DefaultValues.marital_status)))

    submit_button = st.button("Submit")

    if submit_button:
        keywords_data = {
            "alcohol": alcohol,
            "smoking": smoking,
            "sport": sport,
            "zodiac_sign": zodiac_sign,
            "height": height,
            "marital_status": marital_status
        }

    st.session_state["to_send"] = () 
    st.session_state["send"] = False

    #print(api_client.search_keywords(keywords_data))    
    for ankete, ankete_id in search_keywords(api_client.search_keywords(keywords_data)):    
        display_profile(*ankete)
        