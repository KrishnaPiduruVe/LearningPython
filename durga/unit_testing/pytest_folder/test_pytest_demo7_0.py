def test_methodA(setUptearDownClass, setUptearDownMethod):
    print('test_methodA execution')


def test_methodB(setUptearDownMethod, setUptearDownClass):
    print('test_methodB execution')


def test_methodC(setUptearDownMethod, setUptearDownClass):
    print('test_methodC execution')


# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test -sv test_pytest_demo7_0.py
# ===================================================================== test session starts ======================================================================
# platform win32 -- Python 3.7.4, pytest-7.2.2, pluggy-1.0.0 -- c:\users\venka\appdata\local\programs\python\python37-32\python.exe
# cachedir: .pytest_cache
# rootdir: D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder
# collected 2 items

# test_pytest_demo7_0.py::test_methodA conftest.py : setupClass method from setUptearDownClass
# conftest.py :  setup method from setUptearDownMethod
# test_methodA execution
# PASSEDconftest.py :  teardown method from setUptearDownMethod

# test_pytest_demo7_0.py::test_methodB conftest.py :  setup method from setUptearDownMethod
# test_methodB execution
# PASSEDconftest.py :  teardown method from setUptearDownMethod
# conftest.py :  teardownClass method from setUptearDownClass
# ====================================================================== 2 passed in 0.03s =======================================================================
# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder>
