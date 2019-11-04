import tempfile
import logging

from webscrape import get_thing_details
from download import download_thing_files
from zip import zipdir

logger = logging.getLogger(__name__)


def display_thing_details(thing_details):
    print('\tURL: %s' % thing_details['url'])
    print('\tID: %s' % thing_details['id'])
    print('\tFiles: %s' % len(thing_details['files']))


def get_thing(thing_id):
    try:
        print('Retrieving thing details...\n')

        thing_details = get_thing_details(thing_id)
        display_thing_details(thing_details)

        # Create temp folder
        print('\nDownloading thing files...\n')

        with tempfile.TemporaryDirectory() as tempdir:
            # Download all the thing files...
            download_thing_files(thing_details['files'], tempdir)
            print('\nBuidling %s.zip...' % thing_id)
            zipdir(tempdir, thing_id)
            print('DONE!')
    except Exception as e:
        print(e.message)

