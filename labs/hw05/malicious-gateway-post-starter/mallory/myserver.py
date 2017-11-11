import BaseHTTPServer
import json
import urlparse

# https://www.reddit.com/r/learnpython/comments/2iv1c4/best_way_to_listen_on_port_80_for_json_being/

class MyServer(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_POST(s):
        """Respond to a POST request."""

        # Extract and print the contents of the POST
        print s.headers




if __name__ == '__main__':
    print "serving....\n"
    server = BaseHTTPServer.HTTPServer(('', 8080), MyServer)
    server.serve_forever()
    
