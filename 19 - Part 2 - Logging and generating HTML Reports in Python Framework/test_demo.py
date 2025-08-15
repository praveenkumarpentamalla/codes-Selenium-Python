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
# fixture and make it available to all test cases (fixture name into parameters of method)
# datadriven and parameterization can be done with return statement in tuple format
# when you define fixture scope to class it will run once before class is initiated and at the end



import pytest
from BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_edit_profile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])


def test_crossBrowser(crosBrowser):
    print(crosBrowser)
