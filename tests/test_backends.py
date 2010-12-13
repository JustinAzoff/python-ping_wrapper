from ping_wrapper.backends import fping
from ping_wrapper.backends import nmap

def test_backends():
    backends = nmap.NmapPinger(), fping.FpingPinger()
    for b in backends:
        if b.is_available():
            yield case_ping, b
            yield case_ping_down, b
            yield case_ping_many_updown, b
        else:
            print "Backend %s not available, skipping tests" % b.program_path

def case_ping(backend):
    assert backend.ping_one("127.0.0.1")

def case_ping_down(backend):
    assert backend.ping_one("192.168.200.222") == False


def case_ping_many_updown(backend):
    up, down = backend.ping_many_updown(["127.0.0.1", "192.168.200.222"])

    print "up", up
    print "down", down

    assert list(up) == ["127.0.0.1"]
    assert down == ["192.168.200.222"]
