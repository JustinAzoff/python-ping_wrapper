#!/usr/bin/env python
"""NMap Ping Module"""

import os
import tempfile
import subprocess

def os_wait():
    try:
        os.wait()
    except OSError:
        pass


def ping(addrs, use_sudo=False):
    """For each address in addrs, run a nmap ping scan on them.  each address
    can be a single IP or any type of notation that nmap supports"""
    
    f = tempfile.NamedTemporaryFile(dir='/tmp')
    for ip in addrs:
        f.write("%s\n" % ip)
    f.flush()
    
    cmd = "/usr/bin/nmap --max-rtt-timeout 4000 -n -sP -PE -oG - -iL %s 2>/dev/null" % f.name
    if use_sudo:
        cmd = "sudo " + cmd

    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, close_fds=True).stdout

    for line in pipe:
        if 'Status: Up' in line:
            ip = line.split()[1]
            yield ip
    f.close()
    pipe.close()
    os_wait()


def pingmanyupdown(addrs, use_sudo=False):
    """Ping a list of ips, return a tuple of (up nodes, down nodes)"""
    all = list(addrs)
    up = set(ping(all, use_sudo))
    down = [x for x in all if x not in up]
    return up, down

if __name__ == "__main__":
    import sys
    for ip in ping(sys.argv[1:]):
        print ip
