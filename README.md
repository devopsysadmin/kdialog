# xdialog
Python 3 library for easy managing _desktop_ dialog boxes

Currently there is only kdialog implementation, but zenity is also in the scope

# Usage

The simplest usage is letting xdialog to guess which dialog tool should be used:

    from xdialog import xdialog
    xdialog.msgbox('hello world')

You may, however, force the tool to be used by using the `xdialog_set` method:

    from xdialog import xdialog
    from xdialog import xdialog_set
    ...
    xdialog = xdialog_set('zenity')
    xdialog.msgbox('hello world')
