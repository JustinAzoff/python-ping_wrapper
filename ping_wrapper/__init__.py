from ping_wrapper.backends import nmap
from ping_wrapper.backends import fping

backends = {
    "nmap": nmap.pinger_class,
    "fping": fping.pinger_class,
}

default_priority = "nmap", "fping"

def get_backend(priority=None):
    if not priority:
        priority = default_priority

    for name in priority:
        b = backends.get(name)
        if b:
            inst = b()
            if inst.is_available():
                return inst

def ping_one(host):
    return get_backend().ping_one(host)

def ping_many_updown(hosts):
    return get_backend().ping_many_updown(hosts)

def ping_many_updown_iter(hosts):
    return get_backend().ping_many_updown_iter(hosts)

def ping_many(hosts):
    return get_backend().ping_many(hosts)

def ping_many_iter(hosts):
    return get_backend().ping_many_iter(hosts)

