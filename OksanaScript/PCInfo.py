'''run below code to install pcutill:
python.exe -m pip install psutil
-f:<pathToFile>
'''

import sys
import subprocess
import os
import re
import platform 
import psutil

def readOSVersion():
	return '{0} {1} {2} {3}'.format(os.name, platform.platform(), platform.machine(), psutil.cpu_freq())

def readNvidiaVersion():
    cmd = r'"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi" --format=csv,noheader --query-gpu=driver_version,name, ver'
    output = subprocess.check_call(cmd, shell=True)
    all = [float(x) for x in re.findall('Display\.Driver/(\d+\.?\d*)', str(output))]
    return (', '.join(all))


def writeHelp():
    print("Please, make sure that pcutill is installed on your PC. ")
    print("To install pcutill please run: python.exe -m pip install psutil")
    print("To write collected information to file (default behavior is writing to console), please use -f:<file> key")
    print("Example: -f:info.log")
    print("Use -help key for help")


def main(argv=None):
    if argv is None:
        argv = sys.argv

        
    f = None    
    needClosing = False
    try:
        for x in range(1, len(argv)):
            if argv[x].startswith('-f:') & (f is None):
                file = argv[x][3:]
                f = open(file, 'w+') 
                needClosing = True
            elif argv[x] == '-help':
                writeHelp()
                return

        if f == None:
            f = sys.stdout    
    
        f.write(readOSVersion())
        f.write(readNvidiaVersion())
    except Exception as e:
        print("Something goes wrong. See details: ")
        print(e)
        print('\n')
        writeHelp()
    finally:
        if needClosing:
            f.close()

if __name__ == "__main__":
    main()
    input("Press Enter")
