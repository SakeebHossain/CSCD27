import BaseHTTPServer
import urllib
import urllib2

# https://www.reddit.com/r/learnpython/comments/2iv1c4/best_way_to_listen_on_port_80_for_json_being/

class MyServer(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def do_POST(s):
        """Respond to a POST request."""

        # Extract and print the contents of the POST
        length = int(s.headers['Content-Length'])
        
        print "~~~~~~ ALICE ~~~~~~~~~~~~~~~~~~~~~"
        print s.rfile.read(length).decode('utf-8')
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        
        make_POST()

def make_POST():
    url = "http://http-only.seclab.space"
    data = urllib.urlencode({'username' : 'alice', 'password'  : 'pass4alice'})
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)

    print "~~~~~~ MALLORY ~~~~~~~~~~~~~~~~~~~~"
    print response.read()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"    





if __name__ == '__main__':
    print "serving....\n"
    server = BaseHTTPServer.HTTPServer(('', 8080), MyServer)
    server.serve_forever()






