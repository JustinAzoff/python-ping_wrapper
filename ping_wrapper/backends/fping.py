import os
import tempfile
import subprocess
from ping_wrapper.backends.base import BasePinger
from ping_wrapper.backends.util import os_wait


class FpingPinger(BasePinger):
    program = "fping"
    help_return_code = 3

    def ping_many_updown_iter(self, hosts, fast=False):
        """Ping a list of ips, return an iterator of state, node"""
        cmd = [self.program_path]
        if fast:
            cmd.extend(["-r", "1", "-t", "100"])

        sub = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        for ip in hosts:
            sub.stdin.write("%s\n" % ip)
        sub.stdin.close()

        up=[]
        down=[]
        for line in sub.stdout:
            line=line.strip()
            ip = line.split(" ",1)[0]
            if "is alive" in line:
                yield 'up', ip
            elif "is unreachable" in line:
                yield 'down', ip
            
        sub.stdout.close()
        os_wait()

    def ping_many_updown(self, hosts, fast=False):
        """Ping a list of ips, return a tuple of (up nodes, down nodes)"""
        up=[]
        down=[]
        lists = dict(up=up,down=down)
        for state, ip in self.ping_many_updown_iter(hosts, fast):
            lists[state].append(ip)
        return up, down

pinger_class = FpingPinger
