#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
from gdwrap.Gdwrap import Gdwrap

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(CURRENT_DIR, 'keys', 'keys.json')
CREDENTIAL_FILE = os.path.join(CURRENT_DIR, 'keys', 'credential.json')


def main():
    gd = Gdwrap(KEY_FILE, CREDENTIAL_FILE)

    # get config from yaml file
    config = yaml.load(open(os.path.join(CURRENT_DIR, 'config', 'config.yml'), 'r', -1, 'utf-8'))
    page_size = config['file_list']['page_size']
    fields = config['file_list']['fields']
    order_by = config['file_list']['order_by']
    query = config['file_list']['query']

    items = gd.file_list(page_size, fields, order_by, query)
    for item in items:
        print('{0} {1} {2}'.format(item['id'], item['name'], item['webViewLink']))


if __name__ == '__main__':
    main()
