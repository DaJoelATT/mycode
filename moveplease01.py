#!/usr/bin/env python3
# File Moving Util
import shutil
# os Util
import os

#go to right dir

os.chdir('/home/student/mycode/')

# we like to move it move it

shutil.move("raynor.obj","ceph_storage/")

# Find out the new name

xname = input("What is the new name for kerrigan.obj? ")

# Rename it

shutil.move("ceph_storage/kerrigan.obj","ceph_storage/"+xname)


