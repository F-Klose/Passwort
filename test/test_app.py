import unittest
import json
import app

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client() 
        #app. hinzugefügt und __init__.py angelegt dann war test i.O. SF
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/api/helloworld')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()