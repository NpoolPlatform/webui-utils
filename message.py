#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json


def main(argv):
    msg_state = {}
    language = ''

    with open(argv[0]) as msg_src_file:
        lines = msg_src_file.readlines()
        for line in lines:
            msgs = line.split("'")
            for msg in msgs:
                if msg.startswith('MSG_'):
                    msg_state[msg] = 1

    with open(argv[1]) as msg_dst_file:
        msgs = json.load(msg_dst_file)
        language = msgs['Language']['Lang']
        for msg in msgs['Messages']:
            msg_state[msg['MessageID']] = 2

    print('Language: ', language)
    for k, v in msg_state.items():
        if v != 2:
            print('Missed item: ', k, v)


if __name__ == '__main__':
    main(sys.argv[1:])
