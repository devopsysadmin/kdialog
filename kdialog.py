import subprocess

def __get_extras(**kwargs):
    extras = list()
    def put_in_extras(key):
        if kwargs.get(key, None) is not None:
            extras.append(key)
            extras.append(kwargs[key])

    put_in_extras('geometry')


def __run(cmd):
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    rc = proc.returncode
    stdout = proc.stdout.decode('utf8')
    return rc, stdout


def msgbox(text, **kwargs):
    cmd =['kdialog', '--msgbox', text]
    if kwargs:
         cmd += __get_extras(**kwargs)
    return __run(cmd)
