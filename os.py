import os
cd=os.getcwd()
print(cd)
# /////////////

import os #importing os module
size = os.path.getsize("f.txt")
print("Size of the file is", size," bytes.")

f = open("f.txt", "r")
print(f.read())

