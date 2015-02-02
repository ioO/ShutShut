import SimpleHTTPServer
import BaseHTTPServer
import os

ROOT_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'www')
        )

class HTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def translate_path(self, path):
        """ Use another dir as web root """
        # remove first / of path
        root_path = os.path.abspath(os.path.join(ROOT_DIR, path[1:]))
        return root_path

def run():
    server_address = ('', 8080)
    handler = HTTPRequestHandler
    httpd = BaseHTTPServer.HTTPServer(server_address, handler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
