# cofing: utf-8

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    if re.search('AM', s):
        time = s.replace('AM', '')
        time_list = time.split(':')
        if time_list[0] == '12':
            hour = '00'
        else:
            hour = str(time_list[0])
    elif re.search('PM', s):
        time = s.replace('PM', '')
        time_list = time.split(':')
        if time_list[0] == '12':
            hour = int(time_list[0])
        else:
            hour = 12 + int(time_list[0])

    result = str(hour) + ':' + str(time_list[1]) + ':' + str(time_list[2])
    return result


if __name__ == '__main__':
    #s = '07:05:45PM'
    #s = '12:00:00AM'
    #s = '06:40:03AM'
    #s = '12:45:54PM'
    s = '04:59:59AM'

    result = timeConversion(s)
    print(result + '\n')
