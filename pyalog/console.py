import logging
from time import time
from os import remove, popen
import re
from pyalog import Output

exe = 'python'
height, width = [int(x) for x in popen('stty size', 'r').read().split() ]


def msgbox(text, **kwargs):
    print('[INFO] %s' %text)


'''
*elements* is list of tuples. Each tuple contains 3 values:
- (str) return value: a string without spaces or special characters
- (str) title: how will be shown in display
- (bool) checked: Determine if this item is checked when radiolist appears
Note: If there are more than one item checked, the last one applies
Ex: [('foo', 'Something nice', False), ('bar', 'Something ugly', True)]
'''
def radiolist(caption, elements, **kwargs):
    lines = (
        '='*width,
        caption,
        '='*width,
        'key\tDescription',
        '-'*width,
        '\n'.join(['%s\t%s' %(key, title) for key, title, checked in elements]),
        '-'*width,
    )
    print('\n'.join(lines))
    return Output(0, input('Select key: '))


def detailed_error(caption, details, **kwargs):
    lines = ('[ERROR] %s' %caption, '', 'Details:', details, '')
    print('\n'.join(lines))
    return Output(0, '')

