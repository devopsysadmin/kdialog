import subprocess
from shlex import split

def __init(**kwargs):
    cmd = ['kdialog']
    def append_optionals(key):
        if kwargs.get(key, None) is not None:
            cmd.append(key)
            cmd.append(kwargs[key])
    append_optionals('geometry')
    return cmd


def __run(cmd):
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout.decode('utf8')


def msgbox(text, **kwargs):
    cmd = __init(**kwargs) + ['--msgbox', text]
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
    cmd = __init(**kwargs) + ['--radiolist', caption ]
    for key, title, enabled in [ element for element in elements ]:
        cmd.append('%s' %key)
        cmd.append(u'%s' %title)
        cmd.append('on' if enabled else 'off')
    return __run(cmd)


def detailed_error(caption, details, **kwargs):
    cmd = __init(**kwargs) + [ '--detailederror', caption, details ]
    return __run(cmd)

def kdesu(command):
    return __run(split('kdesu -t -c %s' %command))
