#!/usr/bin/python3
import cgi
import subprocess
import time

from datetime import datetime
print("Content-type: text/html")
print()

f = cgi. FieldStorage ( )
cmd = f.getvalue ("x")

print(cmd)

output = subprocess.getoutput("kubctl" + cmd + " -- kubeconfig admin.conf")
print("*"*100)
print()
print (output)
print()
print("*"*100)
time. sleep (0)