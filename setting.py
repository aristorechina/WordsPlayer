#---coding:utf-8---
# setting dir
import os
import sys

path = os.path.dirname(os.path.realpath(sys.argv[0]))
new_path = "/".join(path.split("\\"))
dir = f"{new_path}/user_dic/"