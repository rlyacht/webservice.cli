# coding=UTF-8
# The above is so I can have "Mañana" in a comment


"""
Makes POST requests to an endpoint specified by a URI, with the request
names and structures specified in the templates.

__init__
    URI:        The endpoint, which must accept post requests
    templates:  Dictionary -  Keys are the names of requests that can be made.
         Values are templates using the format required by string.Template

request
    Name - the request to be made (index into templates)
    args - dictionary used to instantiate the template to create the
           content for the POST request
"""

import urllib2
from string import Template

class Poster:
    HEADERS = { 'Content-Type' : 'text/plain',
                'Charset' : 'UTF-8'
              }

    def __init__( self, uri, templates, headers=HEADERS):
        self.uri = uri
        self.headers = headers

        # create dict where values are Templates objects
        self.templates = dict()
        for k in templates:
            self.templates[k] = Template( templates[k] )

    def request( self, name, args ):
        if name not in self.templates :
            return None
        q =  self.templates[name].substitute( args )
        try:
            x = urllib2.Request( self.uri, q )
            for h in self.headers:
                x.add_header( h, self.headers[h] )
            return urllib2.urlopen(x).read()
        except IOError as e:
            # Mañana: do more specific exception handling
            # Having trouble referring to urllib2-specific exceptions
            return "Poster.request error: ", e

def test( ):
    URL = 'http://www.posttestserver.com/post.php?dir=goatnix'
    TEMPLATES = {
        'a' : "<msg><req>a</req><blah>$animal</blah><blah>$num</blah>",
        'b' : "<msg><req>b</req><blah>$animal</blah><blah>$num</blah>",
        }
    
    p = Poster( URL,  TEMPLATES)
    
    for i in range(3):
        print p.request( 'a', { 'animal' : 'goat', 'num' : i   } )
        print p.request( 'b', { 'animal' : 'hen',  'num' : i*i } )

if __name__ == "__main__":
    test()







