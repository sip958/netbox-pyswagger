from __future__ import print_function

import os
import sys

import pynetbox
from netbox_pyswagger.client import Client


server_url = os.getenv('NETBOX_SERVER')
if not server_url:
    sys.exit('NETBOX_SERVER not found in enviornment')


netbox_token = os.getenv('NETBOX_TOKEN')
if not netbox_token:
    sys.exit('NETBOX_TOKEN not found in environment')


netbox = Client.from_pynetbox(
    pynetbox.api(url=server_url, token=netbox_token))
