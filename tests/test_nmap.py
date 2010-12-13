from ping_wrapper.backends import nmap

def test_ping():
    p = nmap.NmapPinger()
    assert p.ping_one("127.0.0.1")

def test_ping_down():
    p = nmap.NmapPinger()
    assert p.ping_one("127.0.0.300") == False
