import requests
import streamlit as st
from config import Config
from typing import Optional

import base64

class APIClient:
    def __init__(self):
        self.base_url = Config.api_base_url
        self.access_token = Config.api_acces_token
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})

    def authenticate(self, login, password)->Optional[int]:
        endpoint = f"{self.base_url}/login/"
        data = {"login": login, "password": password}
        response = requests.post(endpoint, json=data)
        res_data = response.json()
        success =res_data.get("success", False)
        if success:
            return res_data['ankete_id']
        else:
            return None

    def get_open_info(self, ankete_id):
        endpoint = f"{self.base_url}/open-info/{ankete_id}"
        response = requests.get(endpoint, json={})
        print(response)
        if response.status_code == 201:
            return response.json()

    def post_open_info(self, ankete_id, username, full_name,sex,age,city,description):
        endpoint = f"{self.base_url}/open-info/"
        headers={'Content-Type': 'application/octet-stream'}
        data = {
            "ankete_id": ankete_id,
            "username": username,
            "full_name": full_name,
            "sex": sex,
            "age": age,
            "city": city,
            "description": description
        }

        response = requests.get(endpoint, json=data, headers=headers)
        return response.status_code == 201

    def get_closed_info(self, ankete_id):
        endpoint = f"{self.base_url}/closed-info/{ankete_id}"
        response = requests.get(endpoint, json={})
        return response.json()

    def post_closed_info(self, ankete_id, phone_number) -> bool:
        endpoint = f"{self.base_url}/closed-info/"
        data = {"ankete_id": ankete_id, "number": phone_number}
        response = requests.post(endpoint, json=data)
        return response.status_code == 201
    
    def put_closed_info(self, ankete_id, phone_number) -> bool:
        endpoint = f"{self.base_url}/closed-info/{ankete_id}"
        data = {"ankete_id": ankete_id, "number": phone_number}
        response = requests.post(endpoint, json=data)
        return response.status_code == 200

    def register(self, login, password):
        endpoint = f"{self.base_url}/ankete/"
        data = {"login": login, "password": password}
        response = requests.post(endpoint, json=data)
        res_data = response.json()
        ankete_id = res_data.get("ankete_id")
        if not ankete_id:
            return None
        else: return ankete_id
