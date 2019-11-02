import requests
import os
import logging

logger = logging.getLogger(__name__)


def download_file(file_url, file_name, folder = './'):
    full_filename = os.path.join(folder, file_name)

    res = requests.get(file_url, allow_redirects=True)
    open(full_filename, 'wb').write(res.content)



