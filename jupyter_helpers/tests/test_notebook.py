import sys

from jupyter_helpers import notebook

def test_get_session():
    sm = notebook.SessionManager()
    sessions = sm.get_session()
    sm.stop()
    print "I was here!"
    assert False
