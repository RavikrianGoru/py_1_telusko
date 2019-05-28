# https://sourceforge.net/projects/gnuwin32/files/zip/3.0/zip-3.0-setup.exe/download?use_mirror=nchc
# Install in this path C:\GnuWin32\ and set path variables  C:\GnuWin32\bin

# C:\Users\ravi\PycharmProjects\py_durga\byte_of_python\py_tasks>python backup_files.py
# Zip command is: C:\\GnuWin32\\bin\\zip -r C:\destBkp\20190520210854.zip C:\srcBkp
#   adding: srcBkp/ (236 bytes security) (stored 0%)
#   adding: srcBkp/1.txt (172 bytes security) (stored 0%)
#   adding: srcBkp/2.txt (172 bytes security) (stored 0%)
#   adding: srcBkp/3.txt (172 bytes security) (stored 0%)
#   adding: srcBkp/4.txt (172 bytes security) (stored 0%)
#   adding: srcBkp/5.txt (172 bytes security) (stored 0%)
# Successful backup to C:\destBkp\20190520210854.zip

import os
import time
import sys

print(sys.path.append(r'C:\GnuWin32\bin'))
print(sys.path)

# source file or directories specified in list
source = [r'C:\srcBkp'] # windows
# source = [r'/Users/srcBkp'] # linux

# backup files  stored location
target_dir = r'C:\destBkp'

# backup file format with date time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

# zip command to create zip file
#zip_command = f'C:\\GnuWin32\\bin\\zip -r {target} {" ".join(source)}' # zip -r C:\destBkp\20190520205002.zip C:\srcBkp
zip_command = f'zip -r {target} {" ".join(source)}' # zip -r C:\destBkp\20190520205002.zip C:\srcBkp

print('Zip command is:', zip_command)

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
