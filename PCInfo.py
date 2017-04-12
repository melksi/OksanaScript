'''run below code to install pcutill:
python.exe -m pip install psutil
'''

import sys
import sqlite3
import os
import platform 
import psutil

def readOSVersion():
	return '{0} {1} {2}'.format(os.name, platform.platform(), platform.machine())


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) < 2:
        print('Please, provide at least one file to parse')
        return False

    for i in range(len(argv) - 1):
        res = processFile(argv[i + 1])
        if res == False:
            print("Failed parsing file {0}".format(argv[i + 1]))
            return False
    print('Operation executed successfully')


if __name__ == "__main__":
    print(psutil.cpu_freq())
