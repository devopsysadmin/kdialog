import logging
from pyalog import __run

exe = 'zenity'

def __cmd(**kwargs):
    cmd = [exe]
    def append_optionals(key):
        if kwargs.get(key, None) is not None:
            cmd.append(key)
            cmd.append(kwargs[key])
    return cmd


def sudo(command):
    return __run('gksu --sudo-mode %s' %command)


def msgbox(text, **kwargs):
    cmd = __cmd(**kwargs) + [ '--info', '--text', text ]
    return __run(cmd)


'''
*elements* is list of tuples. Each tuple contains 3 values:
- (str) return value: a string without spaces or special characters
- (str) title: how will be shown in display
- (bool) checked: Determine if this item is checked when radiolist appears
Note: If there are more than one item checked, the last one applies
Ex: [('foo', 'Something nice', False), ('bar', 'Something ugly', True)]
'''
def radiolist(caption, elements, **kwargs):
    cmd = __cmd(**kwargs) + [
                            '--list', '--radiolist',
                            '--text', caption,
                            '--column', "", 
                            '--column', 'Key', 
                            '--column', 'Option'
                            ]
    for key, title, enabled in [ element for element in elements ]:
        cmd.append('TRUE' if enabled else 'FALSE')
        cmd.append('%s' %key)
        cmd.append(u'%s' %title)
    return __run(cmd)


def error(caption, details, **kwargs):
    cmd = __cmd(**kwargs) + [ '--error', '--title', caption ]
    return __run(cmd)


def detailed_error(caption, details, **kwargs):
    return error(caption, details, **kwargs)
