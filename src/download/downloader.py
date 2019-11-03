import requests
import os
import logging

from time import time as timer
from functools import partial
from clint.textui import puts

from multiprocessing.dummy import Pool as ThreadPool

logger = logging.getLogger(__name__)


def download_file(folder, file_obj):
    file_url = file_obj['href']
    file_name = file_obj['name']

    full_filename = os.path.join(folder, file_name)

    puts('\t%s ...' % file_name)

    try:
        res = requests.get(file_url, allow_redirects=True)
        open(full_filename, 'wb').write(res.content)
    except Exception as e:
        return file_url, None, e


def download_thing_files(thing_files, temp_dir):
    logger.debug('Temporary folder: %s' % temp_dir)

    start = timer()

    pool = ThreadPool(max(len(thing_files), 8))
    pool.map(partial(download_file, temp_dir), thing_files)
    pool.close()
    pool.join()

    logger.debug(f"Elapsed Time: {timer() - start}")




