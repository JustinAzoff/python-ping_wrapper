from ping_wrapper.backends.base import BasePinger

def test_avialable_when_program_does_not_exist():
    p = BasePinger(program_path="not_exist")
    assert p.is_available() == False

def test_avialable_when_program_exists():
    p = BasePinger(program_path="ls")
    assert p.is_available() == True
