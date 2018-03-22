import subprocess

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
    rc = proc.returncode
    stdout = proc.stdout.decode('utf8')
    return rc, stdout


def msgbox(text, **kwargs):
    cmd = __init(**kwargs) + ['--msgbox', text]
    return __run(cmd)

'''
elements is an array which contains a list of tuples of 3 strings:
- return value: a string without spaces or special characters
- title: how will be shown in display
- state: 'on' or 'off'
Note: If there are more than one item in 'on', the last one will be taken as 'on'
Ex: [('foo', 'Something nice', 'off'), ('bar', 'Something ugly', 'off')]
'''
def radiolist(caption, elements, **kwargs):
    cmd = __init(**kwargs) + ['--radiolist', caption ]
    for key, title, state in [ element for element in elements ]:
        cmd.append('%s' %key)
        cmd.append(u'%s' %title)
        cmd.append('%s' %state)
    return __run(cmd)
