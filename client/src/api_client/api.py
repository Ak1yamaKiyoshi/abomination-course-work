import requests
from typing import Optional
from config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.api_base_url
        self.access_token = Config.api_acces_token
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})

    def authenticate(self, login, password) -> Optional[int]:
        endpoint = f"{self.base_url}/login/"
        data = {"login": login, "password": password}
        response = self.session.post(endpoint, json=data)
        res_data = response.json()
        success = res_data.get("success", False)
        if success:
            return res_data['ankete_id']
        else:
            return None

    # Ankete
    def get_ankete(self, ankete_id):
        endpoint = f"{self.base_url}/ankete/{ankete_id}/"
        response = self.session.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None

    def post_ankete(self, login, password):
        endpoint = f"{self.base_url}/ankete/"
        data = {"login": login, "password": password}
        response = self.session.post(endpoint, json=data)
        res_data = response.json()
        ankete_id = res_data.get("ankete_id")
        if ankete_id:
            return ankete_id
        return None

    # InvitationToAnkete
    def get_invitation_to_ankete(self, invitation_to_ankete_id):
        endpoint = f"{self.base_url}/invitation-to-ankete/{invitation_to_ankete_id}/"
        response = self.session.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None

    def post_invitation_to_ankete(self, ankete_id):
        endpoint = f"{self.base_url}/invitation/"
        data = {"ankete_id": ankete_id}
        response = self.session.post(endpoint, json=data)
        res_data = response.json()
        invitation_id = res_data.get("invitation_id")
        if invitation_id:
            return invitation_id
        return None

    def delete_invitation(self, invitiation_id):
        endpoint = f"{self.base_url}/invitation/{invitiation_id}"
        response = self.session.post(endpoint)
        res_data = response.json()
        return res_data
    
    def search_invitation(self, to):
        endpoint = f"{self.base_url}/invitation/"
        params = {"to_id": to}
        response = self.session.get(endpoint, params=params)

        return response.json()


    # Invitation
    def get_invitation(self, invitation_id):
        endpoint = f"{self.base_url}/invitation/{invitation_id}/"
        response = self.session.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None

    def post_invitation(self, from_id, to_id, description="description", photo="1"):
        endpoint = f"{self.base_url}/invitation/"
        data = {
            "from_id": from_id,
            "to_id": to_id,
            "description": description,
            "photo": photo,
        }
        response = self.session.post(endpoint, json=data)
        
        print(response.content)
        res_data = response.json()
        invitation_id = res_data.get("invitation_id")
        if invitation_id:
            return invitation_id
        return None

    # OpenInfo
    def get_open_info(self, ankete_id):
        endpoint = f"{self.base_url}/open-info/{ankete_id}/"
        response = self.session.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None

    def post_open_info(self, ankete_id, username, full_name, sex, age, city, description, profile_picture=None):
        endpoint = f"{self.base_url}/open-info/"
        data = {
            "ankete_id":ankete_id,
            "username": username,
            "full_name": full_name,
            "sex": sex,
            "age": age,
            "city": city,
            "description": description,
        }
        response = self.session.post(endpoint, json=data)
        return response.status_code == 200

    # ClosedInfo
    def get_closed_info(self, ankete_id):
        endpoint = f"{self.base_url}/closed-info/{ankete_id}/"
        response = self.session.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None

    def post_closed_info(self, ankete_id, phone_number):
        endpoint = f"{self.base_url}/closed-info/"
        data = {"number": phone_number, "ankete_id":ankete_id}
        response = self.session.post(endpoint, json=data)
        return response.status_code == 200

    # PasswordRestoration
    def get_password_restoration(self, ankete_id):
        endpoint = f"{self.base_url}/password-restoration/{ankete_id}/"
        response = self.session.get(endpoint)
        if response.status_code == 200:
            return response.json()
        return None

    def post_password_restoration(self, ankete_id, code):
        endpoint = f"{self.base_url}/password-restoration/"
        data = {"code": code}
        response = self.session.post(endpoint, json=data)
        return response.status_code == 200

    # Keywords
    def search_keywords(self, params):
        endpoint = f"{self.base_url}/keywords/"
        response = self.session.get(endpoint, params=params)

        if response.status_code == 200:
            return response.json()
        return None

    def get_keywords(self, ankete_id):
        endpoint = f"{self.base_url}/keywords/{ankete_id}/"
        response = self.session.get(endpoint)
        
        if response.status_code == 200:
            return response.json()
        return None

    def post_keywords(self, ankete_id, hobby, alcohol, smoking, sport, zodiac_sign, height, age, why_here, marital_status):
        endpoint = f"{self.base_url}/keywords/"
        data = {
            "ankete_id":ankete_id,
            "hobby": hobby,
            "alcohol": alcohol,
            "smoking": smoking,
            "sport": sport,
            "zodiac_sign": zodiac_sign,
            "height": height,
            "age": age,
            "why_here": why_here,
            "marital_status": marital_status,
        }
        response = self.session.post(endpoint, json=data)

        return response.status_code == 200

    # OpenInfo
    def put_open_info(self, ankete_id, username, full_name, sex, age, city, description):
        endpoint = f"{self.base_url}/open-info/{ankete_id}/"
        data = {
            "ankete_id":ankete_id,
            "username": username,
            "full_name": full_name,
            "sex": sex,
            "age": age,
            "city": city,
            "description": description,
        }
        response = self.session.put(endpoint, json=data)
        return response.status_code == 200

    def post_profile_picture(self, ankete_id):
        endpoint = f"{self.base_url}/profile_pictures/"
        data = {"ankete_id":ankete_id, "profile_picture":"_"}
        response = self.session.post(endpoint, json=data)
        return response.status_code == 200
    
    def put_profiel_picture(self, ankete_id, image_str):
        endpoint = f"{self.base_url}/profile_pictures/{ankete_id}/"
        data = {"ankete_id":ankete_id, "profile_picture": image_str}
        response = self.session.put(endpoint, json=data)
        return response.status_code == 200

    def get_profile_picture(self, ankete_id):
        endpoint = f"{self.base_url}/profile_pictures/{ankete_id}/"
        data = {"ankete_id":ankete_id}
        response = self.session.get(endpoint, json=data)
        res = response.json().get("profile_picture", None) # 
        if res and len(res) > 1:
            return res
    
    # ClosedInfo
    def put_closed_info(self, ankete_id, phone_number):
        endpoint = f"{self.base_url}/closed-info/{ankete_id}/"
        data = {"number": phone_number, "ankete_id":ankete_id}
        response = self.session.put(endpoint, json=data)
        return response.status_code == 200

    # PasswordRestoration
    def put_password_restoration(self, ankete_id, code):
        endpoint = f"{self.base_url}/password-restoration/{ankete_id}/"
        data = {"code": code, "ankete_id":ankete_id}
        response = self.session.put(endpoint, json=data)
        return response.status_code == 200



    # Keywords
    def put_keywords(self, ankete_id, hobby, alcohol, smoking, sport, zodiac_sign, height,  why_here, marital_status):
        endpoint = f"{self.base_url}/keywords/{ankete_id}/"
        data = {
            "ankete_id":ankete_id,
            "hobby": hobby,
            "alcohol": alcohol,
            "smoking": smoking,
            "sport": sport,
            "zodiac_sign": zodiac_sign,
            "height": height,
            "why_here": why_here,
            "marital_status": marital_status,
        }
        response = self.session.put(endpoint, json=data)
        return response.status_code == 200