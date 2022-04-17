#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json
import os


def main(argv):
    language = {}
    msgs = []

    with open(argv[0]) as msg_src_file:
        old_msgs = json.load(msg_src_file)
        langs = old_msgs['Languages']
        for lang in langs:
            if argv[1] == lang['Lang']:
                language = lang
                break
        for msg in old_msgs['Messages']:
            msgs.append({
                'AppID': msg['AppID'],
                'LangID': language['ID'],
                'MessageID': msg['MessageID'],
                'Message': msg['Message'],
                'BatchGet': True
            })

    print('Language: ', language)
    with open(language['Lang'] + '-' + os.path.basename(argv[0]), 'w') as new_msg_file:
        new_msg_file.write(json.dumps({
            'Language': language,
            'Messages': msgs
        }, indent=4))


if __name__ == '__main__':
    main(sys.argv[1:])
