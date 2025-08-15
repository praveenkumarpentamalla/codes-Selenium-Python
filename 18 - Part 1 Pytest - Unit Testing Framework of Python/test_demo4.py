# Any pytest files shoud start with 'test_' or end with 'test_'
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names executions, -s logs in out put -v stands for more info metadata
# you can run specific file with py.test <filename>

def test_first():
    msg = "Hello"
    assert msg == "Hi"


def test_second():
    a = 3
    b = 4
    assert a+2 != 6


def test_secondfirsttest():
    msg = "Hello"
    print("Hi")
