import os
import tempfile
import subprocess
from ping_wrapper.backends.base import BasePinger
from ping_wrapper.backends.util import os_wait


class PingPinger(BasePinger):
    program = "ping"
    help_return_code = 2

    def ping_one(self, host):
        """Ping a list of ips, return an iterator of state, node"""
        cmd = [self.program_path, "-c", "1", "-w", "2", host]

        sub = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        sub.communicate()
        ret = sub.wait() == 0
        return ret

pinger_class = PingPinger
