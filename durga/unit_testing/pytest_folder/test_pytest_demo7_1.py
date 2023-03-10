import pytest


def test_methodE(setUptearDownMethod, setUptearDownClass):
    print('test_methodE execution')


@pytest.mark.run(order=2)
def test_methodC(setUptearDownClass, setUptearDownMethod):
    print('test_methodC execution')


def test_methodG(setUptearDownMethod, setUptearDownClass):
    print('test_methodG execution')


@pytest.mark.run(order=1)
def test_methodD(setUptearDownMethod, setUptearDownClass):
    print('test_methodD execution')


def test_methodF(setUptearDownMethod, setUptearDownClass):
    print('test_methodF execution')


# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test -sv test_pytest_demo7_1.py --html=results2.html
# ===================================================================== test session starts ======================================================================
# platform win32 -- Python 3.7.4, pytest-7.2.2, pluggy-1.0.0 -- c:\users\venka\appdata\local\programs\python\python37-32\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.7.4', 'Platform': 'Windows-10-10.0.19041-SP0', 'Packages': {'pytest': '7.2.2', 'pluggy': '1.0.0'}, 'Plugins': {'html': '3.2.0', 'metadata': '2.0.4', 'ordering': '0.6'}, 'JAVA_HOME': 'C:\\JDK'}
# rootdir: D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder
# plugins: html-3.2.0, metadata-2.0.4, ordering-0.6
# collected 5 items

# test_pytest_demo7_1.py::test_methodD conftest.py : setupClass method from setUptearDownClass
# conftest.py :  setup method from setUptearDownMethod
# test_methodD execution
# PASSEDconftest.py :  teardown method from setUptearDownMethod

# test_pytest_demo7_1.py::test_methodC conftest.py :  setup method from setUptearDownMethod
# test_methodC execution
# PASSEDconftest.py :  teardown method from setUptearDownMethod

# test_pytest_demo7_1.py::test_methodE conftest.py :  setup method from setUptearDownMethod
# test_methodE execution
# PASSEDconftest.py :  teardown method from setUptearDownMethod

# test_pytest_demo7_1.py::test_methodG conftest.py :  setup method from setUptearDownMethod
# test_methodG execution
# PASSEDconftest.py :  teardown method from setUptearDownMethod

# test_pytest_demo7_1.py::test_methodF conftest.py :  setup method from setUptearDownMethod
# test_methodF execution
# PASSEDconftest.py :  teardown method from setUptearDownMethod
# conftest.py :  teardownClass method from setUptearDownClass


# --------------------------- generated html file: file:///D:/work/Mosh/LearningPython/durga/unit_testing/pytest_folder/results2.html ----------------------------
# ====================================================================== 5 passed in 0.14s =======================================================================
# PS D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder>
