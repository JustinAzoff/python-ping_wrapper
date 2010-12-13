import os
def os_wait():
    try:
        os.wait()
    except OSError:
        pass

