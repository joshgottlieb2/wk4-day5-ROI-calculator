from cgi import test
from ROI_Calculator import Property, User, user_list
import unittest


class TestProperty(unittest.TestCase):

    def test_property_init(self):
        property = Property(address='123 Sample St', initial_investment=100, extra_expenses=50, income=300)
        return_on_investment = round(
            (int(property.income)/(int(property.initial_investment) + int(property.extra_expenses))) * 100, 2)
        self.assertAlmostEqual(return_on_investment, 300/(50+100)*100)


class TestUser(unittest.TestCase):
    
    def test_user_init(self):
        user1 = User(first_name='Sample', last_name='Samply')
        self.assertIn(user1.user_name, user_list)





if __name__ == '__main__':
    unittest.main()