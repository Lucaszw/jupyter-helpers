import os
import signal
import subprocess
import sys

import psutil

from jupyter_helpers import notebook

def test_get_session():
    sm = notebook.SessionManager()
    session = sm.get_session()
    session.thread.stop()
    process = psutil.Process(session.process.pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()
    return session
