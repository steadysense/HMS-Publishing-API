# Created by SezerBozkir<admin@sezerbozkir.com> at 6/29/2020
import sys
from pathlib import Path
from publishing_api import HmsPublishingApi
from pub_env import client_id, client_secret, package_name
from pprint import pprint

if __name__ == '__main__':
    my_api = HmsPublishingApi(client_id, client_secret, package_name)
    full_path = Path(sys.argv[1])
    file_name = full_path.name
    file_type = full_path.suffix  # apk or aab
    app_info = my_api.upload_app(file_path=full_path,
                                 file_name=file_name,
                                 file_type=file_type)
