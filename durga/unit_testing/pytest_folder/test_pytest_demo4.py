import pytest


@pytest.fixture()  # setUp() method annotation
def setUp():  # use any name but recomended
    print("setup method from setUp")
    yield
    print("teardown method from setUp")


@pytest.yield_fixture()
def setUptearDown():
    print("setup method from setUptearDown", end="\n")
    yield
    print("teardown method from setUptearDown", end="\n")


def test_methodA(setUp):
    print('test_methodA execution', end="\n")


def test_methodB(setUptearDown):
    print('test_methodB execution', end="\n")

# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test -sv test_pytest_demo4.py
# ===================================================================== test session starts ======================================================================
# platform win32 -- Python 3.7.4, pytest-7.2.2, pluggy-1.0.0 -- c:\users\venka\appdata\local\programs\python\python37-32\python.exe
# cachedir: .pytest_cache
# rootdir: D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder
# collected 2 items

# test_pytest_demo4.py::test_methodA setup method from setUp
# test_methodA execution
# PASSEDteardown method from setUp

# test_pytest_demo4.py::test_methodB setup method from setUptearDown
# test_methodB execution
# PASSEDteardown method from setUptearDown


# ======================================================================= warnings summary =======================================================================
# test_pytest_demo4.py:11
#   D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder\test_pytest_demo4.py:11: PytestDeprecationWarning: @pytest.yield_fixture is deprecated.
#   Use @pytest.fixture instead; they are the same.
#     @pytest.yield_fixture()

# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ================================================================= 2 passed, 1 warning in 0.03s =================================================================
# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder>
