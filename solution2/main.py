#!/usr/bin/python

__Version__ = "0.1"
__Owner__ = "Cheng-Ying Chang"


# import external package
import os
from pprint import pprint

# import internal package
from Tester import Tester


def main():

    tester = Tester()
    tester.normalTest()
    # tester.wrongTest()
    # tester.performanceTest()


if __name__ == '__main__':
    main()

