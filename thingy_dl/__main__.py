import os
import sys

from argparse import ArgumentParser

from thingy_dl import get_thing

if __name__ == '__main__':
    import logging.config
    loglevel = os.environ.get('THINGY_DL_LOGLEVEL', 'INFO')
    logging.basicConfig(stream=sys.stdout, level=logging.getLevelName(loglevel))

    arg_parser = ArgumentParser()
    arg_parser.add_argument("thing_id", help='The ID for the thing. Example: https://www.thingiverse.com/thing:XXXXXXX')
    args2 = arg_parser.parse_args()

    thing_id = args2.thing_id
    get_thing(thing_id)
