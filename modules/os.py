import os
from datetime import datetime

print(os.getcwd())
os.chdir('/home/roopam/Desktop')
print(os.getcwd())
os.chdir('/home/roopam/Desktop/Python/modules')
print(os.listdir())
os.makedirs('test/test')        #You can also use mkdir but it only reates the top level directory
os.removedirs('test/test')      #or rmdir to remove just one folder in a tree structure
# os.rename('sys1.py', 'sys.py')

mtime = os.stat('sys.py').st_mtime
print(datetime.fromtimestamp(mtime))