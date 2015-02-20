import SimpleHTTPServer
import BaseHTTPServer
import tempfile
import thread
import os
from threading import Thread

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
        super(HTTPRequestHandler, self).do_GET()

def configure(server_address=None):
    if server_address is None:
        server_address = ('', 8181)
    handler = HTTPRequestHandler
    httpd = BaseHTTPServer.HTTPServer(server_address, handler)
    return httpd

def shutdown(httpd):
    thread.start_new_thread(stop_server, (httpd,))

def stop_server(httpd):
    httpd.shutdown()

def start_server(httpd):
    httpd.serve_forever()

def run(httpd):
    thread.start_new_thread(start_server, (httpd,))

if __name__ == '__main__':
    httpd = configure()
    run(httpd)
