#!python3
import logging
from pyalog import __run

exe = 'osascript'

def __cmd(**kwargs):
    cmd = [exe, '-e']
    def append_optionals(key):
        if kwargs.get(key, None) is not None:
            cmd.append(key)
            cmd.append(kwargs[key])
    return cmd

def msgbox(text, **kwargs):
	cmd = __cmd(**kwargs) + [ 'display dialog "%s"' %text ]
	result = __run(cmd)
	return result
