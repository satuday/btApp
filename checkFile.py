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
bc_cmd = "C:\\Program Files\\BitComet\\BitComet.exe"
rar_cmd = "C:\\Program Files\\WinRAR\\Rar.exe"

def checkFiles(folderPath):
	for rarfile in glob.iglob(folderPath + "*.rar" ):
		print(rarfile)
		args = [rar_cmd, "e", rarfile, "*.txt", "C:\\"]
		subprocess.call(args)
		os.remove(rarfile)

	for btfile in glob.iglob(folderPath + "*.txt"): #.torrent
		dest_file = dest_dir + os.path.basename(btfile)
		if os.path.exists(dest_file):
			os.remove(dest_file)
		shutil.move(btfile, dest_dir)
		args = [bc_cmd, dest_file, '-o ' + dest_dir, '-s']
		#subprocess.Popen(args) 

def longRunningProcess():
	while True:
		checkFiles("C:\\")
		time.sleep(5)


longRunningProcess()
