import os
import sys
arg =  sys.argv[1]
command = "samba-tool ntacl set "
wp = os.getcwd()
for dirname, dirnames, filenames in os.walk(wp):
    os.system(command + "\"" + arg + "\" " + "\"" + dirname  + "\"")
    files = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,f))]
    for f in files:
       os.system(command + "\"" + arg  + "\" " +  "\"" + dirname + "/" + f + "\"")

