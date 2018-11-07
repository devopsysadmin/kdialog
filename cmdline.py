#!python3
from argparse import ArgumentParser
import sys, os
import pyalog

def get_args():
    parser = ArgumentParser()
    parser.add_argument('-e', '--desktop-environment-tool',
                        default='auto',
                        help='Forces desktop environment tool'
                        )
    parser.add_argument('action')
    parser.add_argument('-p', '--parameters', nargs='+')
    return parser.parse_args()


def error(message):
    print(message)
    sys.exit(1)

def array_to_map(array):
    p_map = {}
    for p in array:
        k, _, v = p.partition('=')
        p_map[k] = v
    return p_map

def main():
    args = get_args()
    dialog = pyalog.init(args.desktop_environment_tool)

    actions_map = {
        'msgbox' : dialog.msgbox
    }
    action = actions_map.get(args.action, None)
    if action:
        params_map = array_to_map(args.parameters)
        action(**params_map)
    else:
        error('Unrecognized action')


if __name__ == '__main__':
    main()
