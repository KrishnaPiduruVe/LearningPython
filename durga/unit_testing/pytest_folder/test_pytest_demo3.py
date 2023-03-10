import pytest


@pytest.fixture()
def setUp():  # use any name but recomended
    print("setup method")


@pytest.fixture()
def m1():
    print("m1 method")


def test_methodA(setUp):
    print('test_methodA execution')


def test_methodB(m1):
    print('test_methodB execution')


# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test -sv test_pytest_demo3.py
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = test session starts == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# platform win32 - - Python 3.7.4, pytest-7.2.2, pluggy-1.0.0 - - c: \users\venka\appdata\local\programs\python\python37-32\python.exe
# cachedir: .pytest_cache
# rootdir: D: \work\Mosh\LearningPython\durga\unit_testing\pytest_folder
# collected 2 items

# test_pytest_demo3.py:: test_methodA setup method
# test_methodA execution
# PASSED
# test_pytest_demo3.py:: test_methodB m1 method
# test_methodB execution
# PASSED

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == 2 passed in 0.02s == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# PS D: \work\Mosh\LearningPython\durga\unit_testing\pytest_folder >
