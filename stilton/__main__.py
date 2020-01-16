from argparse import ArgumentParser
import re
MODULE_NAME = "stilton: The command line tool that detects code smells for refactoring"
__version__ = "0.0.1"

class StiltonFileSmeller():
    
    """ File smelling class that can detect code smells"""

    def __init__(self, filename):
        self._filename = filename
        with open(self._filename) as f:
            self.lines = f.readlines()

    def too_many_parameters(self):
    
        """ Checks methods for too many parameters
        :type self: StiltonFileSmeller
        :param self: StiltonFileSmeller object
    
        :raises: None
    
        :rtype: None
        """

        for line in self.lines:
            method_signature = re.search(r"def \w+\(.*\)", line)
            if method_signature is not None:
                signature = method_signature.group()
                # Splits at the open bracket and then removes the second bracket
                # to just leave the parameters 
                parameters = signature.split('(')[1].split(')')[0]
                # Number of parameters is number of ',' plus 1
                if parameters.count(',') + 1 > 5:
                    print("[WARNING] TooManyParameters: " + signature + " in " + self._filename)

def main():
    arg_parser = ArgumentParser(description=MODULE_NAME)
    arg_parser.add_argument('file', metavar='FILE', type=str, help='The file to be checked')
    args = arg_parser.parse_args()
    if args.file:
        smeller = StiltonFileSmeller(args.file)
        smeller.too_many_parameters()
                        
if __name__ == "__main__":
  main()