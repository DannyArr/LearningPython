#! /usr/env/bin python3

import sys
import math
from typing import List


#N = int(input())  # the number of temperatures to analyse
#TEMPS = input()  # the N temperatures expressed as integers ranging from -273 to 5526

def Attempt1(TEMPS):

    N = 0
    if(TEMPS != ""):
        tempList = TEMPS.split(" ")
        N = len(tempList)
    
    if(N > 0):

        def get_ordinal(intx):
            if(intx < 0):
                multiplier = -1
                addition = 0.1
            else:
                multiplier = 1
                addition = 0

            return intx * multiplier + addition

        temps_dictionary = {}
        for temp in tempList:
            temp = int(temp)
            temps_dictionary.__setitem__(temp, get_ordinal(temp))

        sorted_dict = dict(sorted(temps_dictionary.items(), key=lambda x: x[1]))

        output = list(sorted_dict)[0]
    else:
        output = 0

    return output