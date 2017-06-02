import os
import signal
import sys

from jupyter_helpers import notebook

def test_get_session():
    sm = notebook.SessionManager()
    session = sm.get_session()
    session.thread.stop()
    os.kill(session.process.pid, signal.CTRL_C_EVENT)
    pass
