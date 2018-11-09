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

        actualOutput = Solution().reverseWordInSentence(input)

        print "\n\n>>> Expected Result\t: ", expectedOutput
        print ">>> Actual Result\t: ", actualOutput

        print "\n===================================="


    def normalTest(self):
        print "\n\nStart to execute normal test case...\n\n"
        actualResult = self.execute("junyiacademy", "ymedacaiynuj")
        actualResult = self.execute("flipped class room is important", "deppilf ssalc moor si tnatropmi")
        print "\n\nThe ened of the normal test case...\n\n"


    def wrongTest(self):
        print "\n\nStart to execute wrong test case...\n\n"
        actualResult = self.execute("", "")
        actualResult = self.execute(" ", " ")
        print "\n\nThe ened of the wrong test case...\n\n"


    def performanceTest(self):
        pass
