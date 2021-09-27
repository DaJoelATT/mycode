#!/usr/bin/env python3
# Common tools
import shutil
# file stuff
import os
#Now change to the correct directory
# library.method("paramater")
os.chdir("/home/student/mycode/")
# copy some stuff
# library.method("parameter","paramater")
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
# Now copy a whole directory (all whopping 1 file in it)
shutil.copytree("5g_research/", "5g_research_backup/")

