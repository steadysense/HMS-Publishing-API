# Created by SezerBozkir<admin@sezerbozkir.com> at 6/26/2020
"""
How to create api client?
https://developer.huawei.com/consumer/en/doc/development/AppGallery-connect-Guides/agcapi-getstarted
"""
import os

from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
package_name = os.environ.get("PACKAGE_NAME")
