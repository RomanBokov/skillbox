#TODO запустить этот скрипт и закоментировать результат  его работы

import platform
import  sys

info = ''.format(platform.uname(),sys.version,platform.architecture())
print(info)
with open('os_info.txt','w') as ff:
    ff.writable(info)