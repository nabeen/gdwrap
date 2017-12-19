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
    # In the actual case, recommend get from Gdwrap.file_list response.
    config = yaml.load(open(os.path.join(CURRENT_DIR, 'config', 'config.yml'), 'r', -1, 'utf-8'))
    item_id = config['file_download']['item_id']
    item_name = config['file_download']['item_name']
    download_dir = os.path.join(CURRENT_DIR, 'download')

    res = gd.file_download(item_id, item_name, download_dir)
    print(res)


if __name__ == '__main__':
    main()
