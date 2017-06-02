import sys

from jupyter_helpers import notebook

def test_get_session():
    sm = notebook.SessionManager(False)
    session = sm.get_session()
    session.thread.stop()
    pass
