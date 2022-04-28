import requests
import config 
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    current_gce_version = config.getCurrentGCEVersion()
    current_hsm_version = config.getCurrentHSMVersion() 

    request = [{"AppCode": "GCE", "CurrentVersion": "Major.Minor.Fix"}, {"AppCode": "HSM", "CurrentVersion": "Major.Minor.Fix"}]

    print(request)

    uri = config.getHostUrl()
    print(uri)
    response = requests.post(uri, request, auth=HTTPBasicAuth('lattice1', 'codetest'))

    print(response)
    print(response.content) 