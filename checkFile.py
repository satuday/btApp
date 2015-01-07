import os
from datetime import datetime
from datetime import timedelta
import os.path
import glob
import subprocess
import time
import shutil
import sys

dest_dir = "C:\\1\\"
dl_dir = "Z:\\Download\\"
bc_cmd = "C:\\Program Files\\BitComet\\BitComet.exe {0} -o {1} -s"

def checkFiles(folderPath):
	for btfile in glob.iglob(folderPath + "*.txt"): #.torrent
		dest_file = unicode(dest_dir + os.path.basename(btfile), sys.getfilesystemencoding())
		uni_file = unicode(btfile, sys.getfilesystemencoding())
		print uni_file, dest_file, 
		print (bc_cmd.format(dest_file, dl_dir))
		if os.path.exists(dest_file):
			os.remove(dest_file)
		shutil.copy2(uni_file, dest_dir)
		#print (bc_cmd.format(dest_file, dl_dir)) #os.startfile(dest_file) 



def longRunningProcess():
	while True:
		checkFiles("C:\\")
		time.sleep(5)


longRunningProcess()


