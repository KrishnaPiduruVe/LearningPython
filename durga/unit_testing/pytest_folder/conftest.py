import pytest


@pytest.fixture(scope='module')
def setUptearDownClass():
    print("conftest.py : setupClass method from setUptearDownClass")
    yield
    print("conftest.py :  teardownClass method from setUptearDownClass")


@pytest.fixture()
def setUptearDownMethod():
    print("conftest.py :  setup method from setUptearDownMethod")
    yield
    print("conftest.py :  teardown method from setUptearDownMethod")
