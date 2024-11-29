# here we are going to see how can we detect any file present or not, the basic stuff
# this happens with "os" module provided by the python

import os

print(os.path.exists("file_detection.py")) # this exists method returns value in boolean, that file is present or not

print(os.path.isfile("file_detection.py")) # this isfile method returns value in boolean, checks the path given is for directory or file

print(os.path.isdir("file_detection.py")) # this will ofcourse give false value

print(os.path.isdir("files")) # returns boolean value, this checks for directory or not!
