
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test  will run all 4 test cases from demo1 and demo2 files
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo1.py   just run 2 test cases from demo1 file
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo2.py -s if you want to see print statement outputs
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo2.py -s -v if you want to see print statements with details/verbose

import pytest


def test_methodA():
    print('demo1 test_methodA execution')


def test_methodB():
    print('demo1 tes_methodB execution')


def my_own_test_method2():
    print('demo1 my_own_test_method execution')


def my_own_test_method2():
    print('demo1 my_own_test_method2 execution')
