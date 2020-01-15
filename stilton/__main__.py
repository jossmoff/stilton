from argparse import ArgumentParser

MODULE_NAME = "stilton: The command line tool that detects code smells for refactoring"
__version__ = "0.0.1"


def main():
    arg_parser = ArgumentParser(description=MODULE_NAME)
    try:
        args = arg_parser.parse_args()
    except Exception as e:
        traceback.print_exc()
        exit(1)
    exit(0)
                        
if __name__ == "__main__":
  main()