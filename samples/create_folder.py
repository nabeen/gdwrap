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
    # In the actual case, recommend uniq folder name.
    config = yaml.load(open(os.path.join(CURRENT_DIR, 'config', 'config.yml'), 'r', -1, 'utf-8'))
    folder_name = config['create_folder']['folder_name']
    parent_folder_id = config['create_folder']['parent_folder_id']

    res = gd.create_folder(folder_name, parent_folder_id)
    print(res)


if __name__ == '__main__':
    main()
