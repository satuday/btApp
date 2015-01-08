# coding=utf-8
from __future__ import unicode_literals
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
bc_cmd = "C:\\Windows\\notepad.exe"

def checkFiles(folderPath):
	#shutil.move(unicode("C:\\[bbs[1][1].ysk.cc]足球小將世青賽全集13集全.txt", 'utf-8'), unicode("C:\\1\\[bbs[1][1].ysk.cc]足球小將世青賽全集13集全.txt", 'utf-8'))
	for btfile in glob.iglob(folderPath + "*.txt"): #.torrent
		dest_file = dest_dir + os.path.basename(btfile)
		if os.path.exists(dest_file):
			os.remove(dest_file)
		shutil.move(btfile, dest_dir)
		args = [bc_cmd, dest_file]
		subprocess.Popen(args) 
		#os.startfile(dest_file) 

def longRunningProcess():
	while True:
		checkFiles("C:\\")
		time.sleep(5)


longRunningProcess()
