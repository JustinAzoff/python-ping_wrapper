import subprocess

class BasePinger:
    program = None
    help_argument = "-h"
    help_return_code = 0
    def __init__(self, program_path=None, use_sudo=False):
        self.program_path = program_path or self.program
        self.use_sudo = use_sudo

    def is_available(self):
        """Is this backend available"""
        try :
            p = subprocess.Popen([self.program_path, self.help_argument],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.communicate()
            return p.wait() == self.help_return_code
        except OSError:
            return False
    
    def ping_one(self, host):
        """Ping a single host, return True or False"""
        up = self.ping_many([host])
        return len(up) == 1

    def ping_many_updown(self, hosts):
        """Ping many hosts, return a tuple of up hosts, down hosts"""
        raise NotImplementedError()

    def ping_many_updown_iter(self, hosts):
        """Ping many hosts, return a tuple of up hosts, down hosts"""
        raise NotImplementedError()

    def ping_many(self, hosts):
        return self.ping_many_updown(hosts)[0]

    def ping_many_iter(self, hosts, *args, **kwargs):
        """Ping many hosts, return a tuple of up hosts, down hosts"""
        for state, ip in self.ping_many_updown_iter(hosts, *args, **kwargs):
            if state=='up':
                yield ip
