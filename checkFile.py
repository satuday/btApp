import os
from datetime import datetime
from datetime import timedelta
import os.path
import glob
import subprocess
import time
import shutil

dest_dir = "C:\\1\\"

def getCreateDateTime(filename):
	ct = os.path.getctime(filename)
	return datetime.fromtimestamp(ct)


def checkFiles(folderPath):
	#now = datetime.now()
	#delta = timedelta(seconds=5)
	for file in glob.iglob(folderPath + "/*.txt"):
		#ctime = getCreateDateTime(file)
		#diff = now - ctime
		#print file, diff
		#if(diff <= delta):#change to <= for production
			#os.startfile(file)
			dest_file = dest_dir + os.path.basename(file)
			print file, dest_file
			if os.path.exists(dest_file):
				os.remove(dest_file)
			shutil.move(file, dest_dir)


def longRunningProcess():
	while True:
		checkFiles("C:\\")
		time.sleep(5)


longRunningProcess()


