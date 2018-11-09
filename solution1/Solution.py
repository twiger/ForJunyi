#!/usr/bin/python

__Version__ = "0.1"
__Owner__ = "Cheng-Ying Chang"


# import external package
import os
from pprint import pprint

# import internal package


class Solution(object):

    def __init__(self):
        pass


    def reverseWordInSentence(self, sentence):
        
        revList = []
        senList = sentence.split()
        
        for word in senList:
            revWord = self.reverseWord(word)
            revList.append(revWord)

        # print revList

        returnStr = ""
        for word in revList:
            returnStr += word + " "
        # print returnStr

        returnStr.strip()

        return returnStr

    def reverseWord(self, word):
        strList = list(word)
        # print strList

        strList.reverse()
        # print strList
        revWord = ''.join(strList)
        # print revWord
        return revWord
    


