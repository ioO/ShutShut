import unittest
import requests
import server
from threading import Thread


class ServerTests(unittest.TestCase):
    """ Demo how to use ShutShut with tests """

    @classmethod
    def setUpClass(cls):
        """ Run ShutShut """
        cls.httpd = server.configure()
        s = Thread(target=server.run(cls.httpd))
        s.setDaemon(True)
        s.start()

    @classmethod
    def tearDownClass(cls):
        server.shutdown(cls.httpd)

    def test_index(self):
        """ Request index.htm """
        r = requests.get('http://localhost:8181')
        self.assertEqual(r.status_code, 200)

    def test_404(self):
        """ Request non-existent resource """
        r = requests.get('http://localhost:8181/non-existent.htm')
        self.assertEqual(r.status_code, 404)

if __name__ == '__main__':
    unittest.main()
