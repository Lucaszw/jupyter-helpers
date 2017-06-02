from jupyter_helpers import notebook

def test_get_session():
    sm = notebook.SessionManager()
    session = sm.get_session()
    session.stop()
    print sm.sessions.values()
    print "I was here!"
    assert False
