#!/usr/bin/env python
"""
soars.py

Script for using SOARS to administer student course evaluations.

Usage:
    soars test
    soars check
    soars process    

"""

import docopt
import pandas as pd
import ConfigParser


def config():
    pass

def check():
    """ Check survey generation csv file is valid
    """
    print(config)
    pass

def process():
    """ Process JSON output and generate a single file for reporting surveys
    """ 
    print(config)
    pass

def test():
    """ Generate a csv file for testing survey generation 
    """
    print(config)
    pass

def main():
    args = docopt.docopt(__doc__)
    if args['check']:
        check()
    if args['process']:
        process()
    if args['test']:
        test()

if __name__ == '__main__':
    main()