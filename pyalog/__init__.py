import logging
from types import SimpleNamespace

__DEFAULT = 'console'

class Output:
    def __init__(self, sc, stdout):
        self.sc = sc
        self.stdout = stdout
    def __str__(self):
        return str(self.as_dict())
    def as_array(self):
        return self.sc, self.stdout
    def as_dict(self):
        return { 'sc' : self.sc, 'stdout' : self.stdout }


def __run(cmd):
    import subprocess
    from shlex import split
    if isinstance(cmd, str):
        cmd = split(cmd)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sc, stdout = proc.returncode, proc.stdout.decode('utf8')
    return Output(sc, stdout)


def get_desktop_tool(name='auto'):
    from os import path, environ
    env_map = {
        'gnome' : 'zenity',
        'ubuntu' : 'zenity',
        'plasma' : 'kdialog',
        'apple' : 'osascript',
        'kde' : 'kdialog',
        'console' : 'console',
        'kdialog' : 'kdialog',
        'zenity' : 'zenity'
    }
    if name == 'auto':
        desktop = __DEFAULT
        if 'DESKTOP_SESSION' in environ:
            desktop = environ['DESKTOP_SESSION']
        elif 'Apple_PubSub_Socket_Render' in environ:
            desktop = 'apple'
        return env_map.get(desktop, __DEFAULT)
    else:
        return env_map.get(name, __DEFAULT)


def init(name='auto'):
    import importlib
    desktop = get_desktop_tool(name)
    return importlib.import_module('%s.%s' %('pyalog', desktop))

