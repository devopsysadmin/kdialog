# pyalog
Python 3 library for easy managing _desktop_ dialog boxes

Currently there is only kdialog implementation, but zenity is also in the scope

# Usage

The simplest usage is letting pyalog to guess which dialog tool should be used:

    from pyalog import pyalog
    pyalog.msgbox('hello world')

You may, however, force the tool to be used by using the `pyalog_set` method:

    from pyalog import pyalog
    from pyalog import pyalog_set
    ...
    pyalog = pyalog_set('zenity')
    pyalog.msgbox('hello world')
