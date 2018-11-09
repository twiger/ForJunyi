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


    def execute(self, num):
        # print num

        if num < 1:
            return None

        rList = []

        for i in range(1, num+1):
            # print i
            # print i % 3

            if (i % 3) == 0 and (i % 5) != 0:
                continue

            if (i % 3) != 0 and (i % 5) == 0:
                continue

            if (i % 3) == 0 and (i % 5) == 0:
                rList.append(i)
                continue

            rList.append(i)

        return len(rList)




