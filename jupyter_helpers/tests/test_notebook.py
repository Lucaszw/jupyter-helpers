import sys

from jupyter_helpers import notebook

def test_get_session():
    sm = notebook.SessionManager(True)
    session = sm.get_session()
    session.thread.stop()
    session.thread.join()
    pass
