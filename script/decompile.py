import os
import sys
import subprocess

directory = sys.argv[1]

i = 0

apktool = "/home/psyhax/StAlK/script/apktool/apktool.jar" #specify the location of apktool

for root, subdirs, files in os.walk(directory):
  for file in files:
   if file.endswith(".apk"):
    i=i+1
    print str(i) + "-" + file 
    os.system(" mkdir -v decompiled && cd decompiled")
    os.system("java -jar " + apktool + " d " + root + "/" + file)