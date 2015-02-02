import unittest
import requests
import server
import subprocess

class ServerTests(unittest.TestCase):
    """ Demo how to use ShutShut with tests """

    def setUp(self):
        """ Run ShutShut """
        subproccess.call(['python', 'server.py'])

    def test_index(self):
        """ Request index.htm """
        r = requests.get('http://localhost:8080')
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()

