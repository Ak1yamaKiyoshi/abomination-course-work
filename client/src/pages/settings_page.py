
import streamlit as st
from src.api_client.api import APIClient
from src.data_manager.client_data_manager import ClientDataManager

def display_profile(profile_pic, user_data1, user_data2, invid, closed_info):
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
            st.write(f"Phone number: {closed_info['number']}")

        clicked = st.button("Accept", key=f"but_ankete_id:{user_data1['ankete_id']}")
        if clicked:
            APIClient().delete_invitation(invid)

import numpy as np
    

def settings_page():

    manager = ClientDataManager()
    apiclient = APIClient()
    for writing in apiclient.search_invitation(manager.ankete_id):
        try:
            openinfo = apiclient.get_open_info(writing['from_id'])
            keywords = apiclient.get_keywords(writing['from_id'])
            profilepic = apiclient.get_profile_picture(writing['from_id'])
            profilepic = np.array(eval(profilepic))
            closed_info = apiclient.get_closed_info(writing['from_id'])
            
            display_profile(profilepic,  keywords, openinfo, writing['invitation_id'], closed_info)
            st.markdown(f"""Message to you: {writing['description']}""")
        except Exception as e:
            print(e)