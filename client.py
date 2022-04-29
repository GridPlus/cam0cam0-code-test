import requests 
import config 
from requests.auth import HTTPBasicAuth

class UpdateClient:

    def __init__(self):
        self.host_url = config.get_host_url()
        self.host_username = config.get_host_user_name()
        self.host_password = config.get_host_password() 

    def send_post(self, data):
        #headers = {'Accept-Encoding': 'gzip, deflate, br'}
        response = requests.post(url=self.host_url, json=data, auth=HTTPBasicAuth(self.host_username, self.host_password))
        return response 

    def get_updates(self):
        current_gce_version = config.get_current_gce_version()
        current_hsm_version = config.get_current_hsm_version() 

        body = [{"AppCode": "GCE", "CurrentVersion": current_gce_version},{"AppCode": "HSM", "CurrentVersion": current_hsm_version}]

        update_information = self.send_post(body)
        print(update_information.request)


        return update_information.json()

    def download_update(self, update_url):
        update_response = requests.get(update_url, auth=HTTPBasicAuth(self.host_username, self.host_password))

        return update_response.json()







