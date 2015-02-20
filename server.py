import SimpleHTTPServer
import BaseHTTPServer
import tempfile
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'www'))


class HTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler, object):
    """ HTTPRequestHandler for shutshut

        class inherit from object to avoid error with super() in do_GET()

        @SEE:
        http://stackoverflow.com/questions/1713038/super-fails-with-error-typeerror-argument-1-must-be-type-not-classobj#answer-18392639
    """

    def translate_path(self, path):
        """ Use another dir as web root """
        # remove first / of path
        root_path = os.path.abspath(os.path.join(ROOT_DIR, path[1:]))
        return root_path

    def log_message(self, format, *args):
        """ override writing message to stderr
            use a temporary file to log message
        """
        with tempfile.NamedTemporaryFile() as f:
            message = "%s - - [%s] %s\n" % (self.client_address[0],
                                            self.log_date_time_string(),
                                            format % args)
            f.write(message)
            f.flush()

    def do_GET(self):
        """ Watch for get param to kill the server """
        if self.path == '/please-kill-me-softly':
            print self.path
        super(HTTPRequestHandler, self).do_GET()

def configure(server_address=None):
    if server_address is None:
        server_address = ('', 8080)
    handler = HTTPRequestHandler
    httpd = BaseHTTPServer.HTTPServer(server_address, handler)
    return httpd

def run(httpd):
    httpd.serve_forever()

if __name__ == '__main__':
    run()
