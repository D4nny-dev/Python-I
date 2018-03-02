import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """ Test for the class Employee"""

    def setUp(self):
        self.employee = Employee('Juan','Gomez',2000)
    
    def test_default_salary(self):
        default_salary = self.employee.give_raise()
        self.assertEqual(default_salary,7000)
    
    def test_custom_salary(self):
        custom_salary = self.employee.give_raise(400)
        self.assertEqual(custom_salary,2400)
    
unittest.main()