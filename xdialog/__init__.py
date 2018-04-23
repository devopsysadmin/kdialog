def set(name):
    import os
    import importlib
    if name is None:
        env_map = {
            'gnome' : 'zenity',
            'kde' : 'kdialog',
            'plasma' : 'kdialog'
        }
        name = env_map[os.path.basename(os.getenv('DESKTOP_SESSION'))]
    try:
        return importlib.import_module('%s.%s' %('xdialog', name))
    except:
        return None

if 'xdialog' not in locals().keys():
    xdialog = set(None)
