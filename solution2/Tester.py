#!/usr/bin/python

__Version__ = "0.1"
__Owner__ = "Cheng-Ying Chang"


# import external package
import os
from pprint import pprint

# import internal package
from Solution import Solution


class Tester:

    def __init__(self):
        pass


    def execute(self, input, expectedOutput):
        print "====================================\n"
        print "Input of Test Case\t: ", input
        print "\n\n[ Console Panel ]\n"

        actualOutput = Solution().execute(input)

        print "\n\n>>> Expected Result\t: ", expectedOutput
        print ">>> Actual Result\t: ", actualOutput

        print "\n===================================="


    def normalTest(self):
        print "\n\nStart to execute normal test case...\n\n"
        actualResult = self.execute(15, 9)
        actualResult = self.execute(2, 2)
        print "\n\nThe ened of the normal test case...\n\n"


    def wrongTest(self):
        print "\n\nStart to execute wrong test case...\n\n"
        actualResult = self.execute("", "")
        actualResult = self.execute(" ", " ")
        print "\n\nThe ened of the wrong test case...\n\n"


    def performanceTest(self):
        pass
