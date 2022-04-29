import requests
import config 
from client import UpdateClient
from requests.auth import HTTPBasicAuth



import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.

import http.client as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


if __name__ == "__main__":

    client = UpdateClient() 
    response = client.get_updates()

    update_download_url = response.get('downloadURL', None)

    if update_download_url is not None:
        update = client.download_update(update_download_url)

        print(update)
    else:
        print("no update information found")



