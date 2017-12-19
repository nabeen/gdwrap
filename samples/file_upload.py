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
    # In the actual case, recommend Gdwrap.create_folder response and more.
    config = yaml.load(open(os.path.join(CURRENT_DIR, 'config', 'config.yml'), 'r', -1, 'utf-8'))
    folder_id = config['file_upload']['folder_id']
    item_name = os.path.join(CURRENT_DIR, 'upload', config['file_upload']['item_name'])
    mine_type = config['file_upload']['mine_type']

    gd.file_upload(folder_id, item_name, mine_type)


if __name__ == '__main__':
    main()
