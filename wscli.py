import argparse
from string import Template
import poster

class doitAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(doitAction, self).__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print "doit trying to do '%s'" % values
        a = vars(namespace)
        print a
        print getattr( namespace, 'animal')
#        print('%r %r %r' % (namespace, values, option_string))
#        setattr(namespace, self.dest, values)


class WebServiceCLI:
    def test(self):
        Environments = {
            'server1' : 'http://blah1.com',
            'server2' : 'http://blah2.com',
            }

        Requests = {
            'blah' : Template("Blah: ${animal}nix has $num legs on $server"),
            'bleh' : Template("Bleh: ${animal}nix has $num legs on $server"),
            }
        
        parser = argparse.ArgumentParser()

        # USAGE
        parser.add_argument("--usage", action='store_const', const=True)

        # Custom action
        parser.add_argument("--doit", action=doitAction )

        # Required arguments
        parser.add_argument("--num", type=int, required=True)

        # Optional arguments
        parser.add_argument("--animal")
        parser.add_argument("--server",  choices=Environments.keys() )
        parser.add_argument("--request", choices=Requests.keys() )

        args = parser.parse_args()
        
if __name__ == "__main__":
    WebServiceCLI().test()

