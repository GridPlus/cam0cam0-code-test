import requests 
import config 
import json 
from requests.auth import HTTPBasicAuth

class UpdateClient:

    def __init__(self):
        self.host_url = config.get_host_url()
        self.host_username = config.get_host_user_name()
        self.host_password = config.get_host_password() 

    def __send_post(self, data):
        headers = {'Content-Encoding': None, 'User-Agent': None, 'Content-Type': 'application/json'}
        response = requests.post(url=self.host_url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(self.host_username, self.host_password))
        return response 

    def get_update_catalog(self):
        """Get the update catalog from the update catalog service"""

        current_gce_version = config.get_current_gce_version()
        current_hsm_version = config.get_current_hsm_version() 
        
        body = [{"AppCode": "GCE", "CurrentVersion": current_gce_version},{"AppCode": "HSM", "CurrentVersion": current_hsm_version}]
        update_information = self.__send_post(body)
        return update_information.json()

    def download_update(self, update_url):
        """Download the raw update content"""

        update_response = requests.get(update_url, auth=HTTPBasicAuth(self.host_username, self.host_password))

        return update_response.content







