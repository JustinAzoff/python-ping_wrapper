import os
import tempfile
import subprocess
from ping_wrapper.backends.base import BasePinger
from ping_wrapper.backends.util import os_wait

class NmapPinger(BasePinger):
    program = "nmap"

    def parse_output(self, output):
        for line in output:
            if 'Status: Up' in line:
                ip = line.split()[1]
                yield ip

    def ping(self, hosts):
        """For each address in addrs, run a nmap ping scan on them.  each address
        can be a single IP or any type of notation that nmap supports"""
        
        f = tempfile.NamedTemporaryFile(dir='/tmp')
        for ip in addrs:
            f.write("%s\n" % ip)
        f.flush()
        
        cmd = [self.program_path, "--max-rtt-timeout", "4000", "-n", "-sP", "-PE", "-oG", "-", "-iL", f.name]
        if self.use_sudo:
            cmd = ["sudo"] + cmd

        pipe = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True).stdout
        for ip in self.parse_output(pipe):
            yield ip
        f.close()
        pipe.close()
        os_wait()


    def ping_many(self, addrs):
        """Ping a list of ips, return a tuple of (up nodes, down nodes)"""
        all = list(addrs)
        up = set(ping(all))
        down = [x for x in all if x not in up]
        return up, down

    def ping_one(self, host):
        cmd = [self.program_path, "--max-rtt-timeout", "2000", "-n", "-sP", "-PE", "-oG", "-", host]
        if self.use_sudo:
            cmd = ["sudo"] + cmd

        pipe = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True).stdout
        out = pipe.read()
        pipe.close()
        os_wait()

        return 'Status: Up' in out
