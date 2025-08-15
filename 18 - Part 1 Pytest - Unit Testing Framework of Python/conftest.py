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



@pytest.fixture(scope="class")
def setup():
    print("I will be executing the first")
    yield
    print("I will be executing last")
