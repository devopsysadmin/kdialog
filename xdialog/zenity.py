def __cmd(**kwargs):
    cmd = ['zenity']
    def append_optionals(key):
        if kwargs.get(key, None) is not None:
            cmd.append(key)
            cmd.append(kwargs[key])
    return cmd


def __run(cmd):
    import subprocess
    from shlex import split
    if isinstance(cmd, str):
        cmd = split(cmd)
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout.decode('utf8')

def sudo(command):
    return __run('kdesu -t -c %s' %command)

def msgbox(text, **kwargs):
    cmd = __cmd(**kwargs) + [ '--info', '--text', text ]
    return __run(cmd)
