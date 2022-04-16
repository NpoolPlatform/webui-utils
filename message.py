#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json
import os


def main(argv):
    msg_state = {}
    language = {}
    old_msgs = {}
    old_msg = {}

    with open(argv[0]) as msg_src_file:
        lines = msg_src_file.readlines()
        for line in lines:
            msgs = line.split("'")
            for msg in msgs:
                if msg.startswith('MSG_'):
                    msg_state[msg] = 1

    with open(argv[1]) as msg_dst_file:
        old_msgs = json.load(msg_dst_file)
        language = old_msgs['Language']
        for msg in old_msgs['Messages']:
            old_msg = msg
            msg_state[msg['MessageID']] = 2

    print('Language: ', language)
    msgs = old_msgs['Messages']

    for k, v in msg_state.items():
        if v != 2:
            print('Missed item: ', k, v)
            msgs.append({
                'AppID': old_msg['AppID'],
                'LangID': old_msg['LangID'],
                'MessageID': k,
                'Message': 'TO BE FILLED',
                'BatchGet': True
            })


    old_msgs['Messages'] = msgs
    with open('new-' + os.path.basename(argv[1]), 'w') as new_msg_file:
        new_msg_file.write(json.dumps(old_msgs, indent=4))


if __name__ == '__main__':
    main(sys.argv[1:])
