'''
you can use conftest.py for common setUp(),tearDown(),setUpClass(),tearDownClass()



conftest.py:
============
code reusability
common setup and teardown activities we have to define in this file 
automatically available for all test scripts
it must be avaialble at the same level as rest test scripts are available
conftest.py file name is fixed name by default

if you want different name say conftest1.py import the methods from conftest1
from conftest1 import *



various possible ways to run pytest test scripts:
=================================================

1. py.test  -v -s 
    To run all test methods present in all test scripts of current working directory

2. py.test  -v -s  test.py
    To run all test methods present of a particular script

3. py.test  -v -s  test.py test1.py
    To run all test methods present of a multiple scripts

4. py.test -vs test.py::test_methodB

we can use py.test or pytest

5. all test methods will be executed from top to bottom.
    pytest will not consider alphabetical order like unitest

customize order of tests in pytest
we have to install seperate module pytest-ordering module 
pip install pytest-ordering

@pytest.mark.run(order=n)


How to generate test results in html form:

pip install pytest-html

py.test -sv test_pytest_demo7_1.py --html=results2.html
'''
