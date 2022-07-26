import os
import ctypes
import subprocess, signal
import logging

log = logging.getLogger()


class SleepBlogger:
    def __init__(self):
        self.os = os.name
        self.process = None

    def __enter__(self):
        if self.os == "nt":
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
        elif self.os == "posix":
            self.process = subprocess.Popen(["caffeinate"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        else:
            raise NotImplemented("Not implemented OS.")

        log.debug("Sleepmode inhibited.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.os == "nt":
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
        elif self.os == "posix":
            self.process.send_signal(signal.SIGINT)

        log.debug("Sleepmode released.")
