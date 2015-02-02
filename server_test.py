import unittest
import requests
import server

class ServerTests(unittest.TestCase):
    """ Demo how to use ShutShut with tests """

    class setUp(self):
        """ Run ShutShut """
        server.run()

    class test_index(self):
        """ Request index.htm """
        r = requests.get('http://localhost:8080')
        self.assertEqual(r.status_code, 200)
