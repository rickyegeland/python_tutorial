#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='square a number')
parser.add_argument('x', type=float, nargs=1,
                    help='a number to square')
parser.add_argument('--power', dest='power', action='store',
                    type=float, default=2.0,
                    help='raise to the given power instead')

args = parser.parse_args()
x = args.x[0]
n = args.power
result = x ** n
print("Result", result)
