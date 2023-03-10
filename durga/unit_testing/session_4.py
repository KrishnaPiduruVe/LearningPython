
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test  will run all 4 test cases from demo1 and demo2 files
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo1.py   just run 2 test cases from only demo1 file
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo2.py -s if you want to see print statement outputs
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test test_pytest_demo2.py -s -v if you want to see print statements with details/verbose
# D:\work\Mosh\LearningPython\durga\unit_testing\pytest_folder> py.test -sv test_pytest_demo3.py
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



'''
