import logging

def __run(cmd):
    import subprocess
    from shlex import split
    if isinstance(cmd, str):
        cmd = split(cmd)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sc, stdout = proc.returncode, proc.stdout.decode('utf8')
    print(stdout)
    return sc, stdout


def get_desktop_tool():
    from os import path, getenv
    desktop = path.basename(getenv('DESKTOP_SESSION'))
    env_map = {
        'gnome' : 'zenity',
        'ubuntu' : 'zenity',
        'plasma' : 'kdialog'
    }
    exe = env_map.get(desktop, None)
    if exe is None:
        print('No desktop session available in list. Setting to zenity')
        exe = 'zenity'
    return exe


def pyalog_set(name):
    import importlib
    return importlib.import_module('%s.%s' %('pyalog', name))


if 'pyalog' not in locals().keys():
    pyalog = pyalog_set(get_desktop_tool())
