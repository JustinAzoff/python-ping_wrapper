import subprocess

class BasePinger:
    program = None
    def __init__(self, program_path=None, use_sudo=False):
        self.program_path = program_path or self.program
        self.use_sudo = use_sudo

    def is_available(self):
        """Is this backend available"""
        try :
            p = subprocess.Popen([self.program_path],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.communicate()
            return p.wait() == 0
        except OSError:
            return False
    
    def ping_one(self, host):
        """Ping a single host, return True or False"""
        raise NotImplementedError()

    def ping_many(self, hosts):
        """Ping many hosts, return a tuple of up hosts, down hosts"""
        raise NotImplementedError()
