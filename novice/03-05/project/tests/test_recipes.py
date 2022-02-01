import unittest

from project import app

class ProjectTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_cliest()

        self.assertEquals(app.debug, False)
    
    def test_main_page(self):
        response = self.app.get('/',follow_redirect=True)
        self.assertIn(b'Welcome to the Kennedy Family Recipe App!', response.data)
        self.assertIn(b'This site describes our favorite family recipes!', response.data)
        self.assertIn(b'Breakfast Recipes', response.data)
        self.assertIn(b'Lunch Recipes', response.data)
        self.assertIn(b'Dinner Recipes', response.data)
        self.assertIn(b'Dessert Recipes', response.data)


if __name__ == '__main__':
    unittest.main()