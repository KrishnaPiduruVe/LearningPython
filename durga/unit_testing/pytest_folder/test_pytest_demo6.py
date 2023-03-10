import pytest


@pytest.fixture()  # setUp() method annotation
def setUp():  # use any name but recomended
    print("setup method from setUp")
    yield
    print("teardown method from setUp")


@pytest.yield_fixture(scope='module')  # By default scope is function
def setUptearDownClass():
    print("setupClass method from setUptearDownClass")
    yield
    print("teardownClass method from setUptearDownClass")


@pytest.yield_fixture()  # By default scope is function
def setUptearDownMethod():
    print("setup method from setUptearDownMethod")
    yield
    print("teardown method from setUptearDownMethod")


def test_methodA(setUp):
    print('test_methodA execution', end="\n")


def test_methodB(setUptearDownClass, setUptearDownMethod):
    print('test_methodB execution', end="\n")


def test_methodC(setUptearDownMethod, setUptearDownClass):
    print('test_methodC execution', end="\n")


# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test -sv test_pytest_demo6.py
# ===================================================================== test session starts ======================================================================
# platform win32 -- Python 3.7.4, pytest-7.2.2, pluggy-1.0.0 -- c:\users\venka\appdata\local\programs\python\python37-32\python.exe
# cachedir: .pytest_cache
# rootdir: D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder
# collected 3 items

# test_pytest_demo6.py::test_methodA setup method from setUp
# test_methodA execution
# PASSEDteardown method from setUp

# test_pytest_demo6.py::test_methodB setupClass method from setUptearDownClass
# setup method from setUptearDownMethod
# test_methodB execution
# PASSEDteardown method from setUptearDownMethod

# test_pytest_demo6.py::test_methodC setup method from setUptearDownMethod
# test_methodC execution
# PASSEDteardown method from setUptearDownMethod
# teardownClass method from setUptearDownClass


# ======================================================================= warnings summary =======================================================================
# test_pytest_demo6.py:11
#   D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder\test_pytest_demo6.py:11: PytestDeprecationWarning: @pytest.yield_fixture is deprecated.
#   Use @pytest.fixture instead; they are the same.
#     @pytest.yield_fixture(scope='module')  # By default scope is function

# test_pytest_demo6.py:18
#   D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder\test_pytest_demo6.py:18: PytestDeprecationWarning: @pytest.yield_fixture is deprecated.
#   Use @pytest.fixture instead; they are the same.
#     @pytest.yield_fixture()  # By default scope is function

# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ================================================================ 3 passed, 2 warnings in 0.05s =================================================================
# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder>
