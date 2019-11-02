import requests
from urllib.parse import urlparse, urljoin, quote_plus
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

thing_base_url = 'https://www.thingiverse.com/thing:{thing_id}'
files_suffix = 'files'

base_url = 'https://www.thingiverse.com/thing:{thing_id}/files'
thing_id = '3182917'


def get_base_domain(url):
    url_details = urlparse(url)
    return '%s://%s' % (url_details.scheme, url_details.netloc)


def get_thing_details(thing):
    base_domain = get_base_domain(base_url)
    thing_url = thing_base_url.format(thing_id=thing)
    thing_files_url = '%s/files' % thing_url

    page = requests.get(thing_files_url)

    if page.status_code != 200:
        print('There was an error while getting info for thing: %s' % thing)
        exit(1)
    else:
        result = {}
        soup = BeautifulSoup(page.text, 'html.parser')

        print('Retrieving thing details...\n')

        result['url'] = thing_url
        result['id'] = thing
        result['name'] = soup.find('h1').get_text('', strip=True)
        result['files'] = list(map(lambda x: {
            'href': urljoin(base_domain, x['href']),
            'name': x.select_one('span span.inline-middle div.truncate').get_text('', strip=True)
            # 'name': x.findAll('span', attrs={'class': 'inline-middle'})
        }, soup.find_all('a', attrs={'class': 'file-download', 'href': True})))

        return result


def display_thing_details(thing_details):
    print('Thing details')
    print('URL: %s' % thing_details['url'])
    print('ID: %s' % thing_details['id'])
    print('Files: %s' % len(thing_details['files']))
