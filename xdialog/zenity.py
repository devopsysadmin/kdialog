import logging
from xdialog import __run

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
