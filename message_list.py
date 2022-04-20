#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import json
import os


def main(argv):
    msg_state = {}

    with open(argv[0]) as msg_src_file:
        lines = msg_src_file.readlines()
        for line in lines:
            msgs = line.split("'")
            for msg in msgs:
                if msg.startswith('MSG_'):
                    msg_state[msg] = 1
            msgs = line.split("\"")
            for msg in msgs:
                if msg.startswith('MSG_'):
                    msg_state[msg] = 1

    with open('new-' + os.path.basename(argv[0]), 'w') as new_msg_file:
        new_msg_file.write(json.dumps(msg_state, indent=4))


if __name__ == '__main__':
    main(sys.argv[1:])
