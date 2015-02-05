import unittest
import requests
import server
from threading import Thread

class ServerTests(unittest.TestCase):
    """ Demo how to use ShutShut with tests """

    @classmethod
    def setUpClass(cls):
        """ Run ShutShut """
        httpd = Thread(target=server.run)
        httpd.setDaemon(True)
        httpd.start()

    def test_index(self):
        """ Request index.htm """
        r = requests.get('http://localhost:8080')
        self.assertEqual(r.status_code, 200)

    def test_404(self):
        """ Request non-existent resource """
        r = requests.get('http://localhost:8080/non-existent.htm')
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()

