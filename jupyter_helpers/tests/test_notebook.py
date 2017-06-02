import os
import signal
import sys

from jupyter_helpers import notebook

def test_get_session():
    sm = notebook.SessionManager(False)
    session = sm.get_session()
    session.thread.stop()
    session.thread.join()
    os.kill(session.process.pid, signal.CTRL_C_EVENT)
    pass
