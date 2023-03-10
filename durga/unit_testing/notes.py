'''
There is no seperate team going forward for testing

Developer must be the tester in future

Testing :
    1. Unit Testing : 
        The process of testing each unit 
    2. Integration Testing : 
        end to end testing after integrating each unit
    
    Final testing is superior or final level testing

The process of testing whether a particular unit is working properly or not is called unit testing. --- Developer
The process of total application end to end is called integration testing --- QA 
'''


'''
Test Scenario
Test Case
Test Suite

I developed gmail application


this testing will be divided in to multiple scenerios
1. testing login functionality -- > Test Scenerio
    1.1 with valid user and valid password  ---> Test case 1 
    1.2 with invalid user and valid password ---> Test case 2
    1.3 empty user and password  ---> Test case 3
2. testing inbox functionality

[Test Case 1  +  Test Case 2  + Test Case 3] ====> Test Suite (testing as a group or batch)


How to perform unit testing in Python:

inbuilt module name : unittest 
class name : TestCase
instance methods : 3 methods
                        1. setUp()
                        2. test()
                        3. tearDown()
class methods : 2 methods
                    1.setUpClass(cls)
                    2.tearDownClass(cls)

class TestCaseDemo(TestCase):


Lets say 10 test methods are there

setUp() --> 10 times
tearDown() ---> 10 times 
setUpClass(cls) ---> 1 time  
tearDownClass(cls) ---> 1 time 


write a python test script to test google search functionality by using selinum unit testing  ?

What is Selenium ?
    Funtional testing automation tool

We have to install selenium package 

pip install selenium ==> Install pip

pip install --upgrade pip 
    ==> upgrade pip 
    ===> If ERROR: Could not install packages due to an EnvironmentError: [WinError 5] Access is denied: 'C:\\Users\\venka\\AppData\\Local\\Temp\\pip-uninstall-gdvzc6ou\\pip.exe'
        Consider using the `--user` option or check the permissions ==>
pip install --upgrade pip --user

selenium : package 
webdriver : module

webdriver module contains several classes and functions to test functionality of the web application

Launch browser :
    browser driver must be required to launch our browser
    seleniumhq.org

Browser interaction and navigation of web pages:

driver.get(url) ==> to open specified url
driver.maximize_window()
driver.title
driver.current_url
driver.refresh() or  driver.get(driver.current_url)
driver.back() ===> goes one step backward in the browser history
driver.forward ===> goes one step forward in the browser history
driver.close()  ===> close current window
driver.quit() ===> close associated windows  


driver.find_element("id",'id')
driver.find_element("name",'name')
driver.find_element("text",'txt')
driver.find_element("css selector",'css')

expected one of `css selector`, 
`link text`, `partial link text`, `tag name`, `xpath`



Test Suite:
============
By using unittest module we can execute a group of testcases ,which is nothing but testsuite


Problems with unittest module:
=================================

module : unittest
class : TestCase
instance methods :
    setUp()
    test()
    tearDown()
class methods :
    setUpClass(cls)
    tearDownClass(cls)

1. Test methods will be executed in alphabetical order only (test_a == > test_b ===> test_c) and 
    it is not possible to customize the order
2. Test results will be displayed to the console only and it is not possible to generate reports.
3. As the part of batch execution (TestSuite), all the methods from the specified test case classes will be executed 
    and it is not possible to specify particular methods.
4. In unit testing only limited setUp and tearDown methods are available
    setUpClass ==> before executing all test methods of a testcase class
    tearDownClass  ===> after executing all test methods of a TestCase class
    setUp() == > before every test method execution
    tearDown() ==> after every test method execution

    If we want to perform any activity before executing testsuite and after executing testsuite,
     unit test frame work doesnt proide any methods


PyTest : FrameWork 
=====================

most commonly used FrameWork for unit testing
advanced version of unittest
built on top of unittest framework

PyTest is not availble by default with python

pip install pytest

PyTest naming rules :
==========================
1. File name must start with or end with 'test'
    test_google_search.py
    google_search_test.py

2. Class Name should start with 'Test'
    TestGoogleSearch
    TestCaseDemo

3. Test method name must start with 'test_'
    test_method1()
    test_method2()

'''
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test  will run all 4 test cases from demo1 and demo2 files
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo1.py   just run 2 test cases from only demo1 file
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo2.py -s if you want to see print statement outputs
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo2.py -s -v if you want to see print statements with details/verbose


''' 
pytest dont have any special methods like setUp(),tearDown(),setUpClass(),tearDownClass()

By using some decorator/annotation we can implement above methods

To implement setUp()
@pytest.fixture()  ===> setUp() 

@pytest.yield_fixture() ===> setUp() + tearDown()

@pytest.yield_fixture() ===> setUp() || tearDown() || setUp() + tearDown()
def m1():
    setUp activity
    yield
    tearDown activity

@pytest.yield_fixture()  ===> only tearDown()
def m1():
    yield
    tearDown activity


@pytest.yield_fixture()  ===> only setUp()
def m1():
   setUp activity


How to Implement setUpClass() and tearDownClass() in pytest:

@pytest.yield_fixture(scope='module'): # default scope is function
def m1():
    code

How to Implement setUp(),tearDown() and setUpClass() and tearDownClass() simultaneously

@pytest.yield_fixture(): # default scope is function
def setUptearDownMethod():
    setup()
    yield
    tearDown()
    
@pytest.yield_fixture(scope='module'): # default scope is function
def setUptearDownClass():
    setupClass()
    yield
    tearDownClass()

'''
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo3.py -sv
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo4.py -sv
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo5.py -sv
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo6.py -sv
