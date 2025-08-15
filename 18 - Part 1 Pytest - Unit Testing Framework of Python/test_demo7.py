# Any pytest files shoud start with 'test_' or end with 'test_'
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names executions, -s logs in out put -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m 
# you can skip with @pytest.mark.skip
# @pytest.mark.xfail it do not show in output
# fixtures are used as setup and tear dwon methods for test cases - conftest file to generalize
# fixture and make it available to all test cases




import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")


    def test_first(self):
        msg = "Hello"
        assert msg == "Hi"

    @pytest.mark.smoke
    def test_second(self):
        a = 3
        b = 4
        assert a+2 != 6

    @pytest.mark.smoke
    @pytest.mark.skip
    def test_secondfirsttest(self):
        msg = "Hello"
        print("Hi")

    @pytest.mark.xfail
    def test_one():
        print("*August*")
