import logging
import requests
from requests.auth import HTTPBasicAuth
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')

# Define constants
HOST = '192.168.1.101'
USER = 'student'
PASS = 'Meilab123'
BASE_URL = f'http://{HOST}/restconf/api/running/'

def get_interfaces(append_url):
    """Fetch network interfaces using RESTCONF API."""
    url = BASE_URL + append_url
    auth = HTTPBasicAuth(USER, PASS)
    headers = {'Accept': 'application/vnd.yang.data+json'}
    
    logging.info(f"URL ==> {url}")
    
    response = requests.get(url, auth=auth, headers=headers)
    
    if response.status_code == 200:
        logging.info(f"Request was successful on {HOST}, Code: {response.status_code}")
        return json.dumps(response.json(), sort_keys=True, indent=4)
    else:
        logging.error(f"Error encountered during request on {HOST}, Code: {response.status_code}")
        return response.text

# Call the function and print the result
print(get_interfaces('interfaces'))
