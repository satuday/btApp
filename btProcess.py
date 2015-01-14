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

processed_dir = "E:\\Processed\\"
dl_dir = "Z:\\Download\\"
bc_cmd = "C:\\Program Files\\BitComet\\BitComet.exe"
rar_cmd = "C:\\Program Files\\WinRAR\\WinRar.exe"

def uncompress(folderPath):
	for rarfile in glob.iglob(folderPath + "*.zip" ):
		args = [rar_cmd, "e", rarfile, "*.torrent", "E:\\"]
		print(args)
		subprocess.call(args)
		os.remove(rarfile)
		
	for rarfile in glob.iglob(folderPath + "*.rar" ):
		args = [rar_cmd, "e", rarfile, "*.torrent", "E:\\"]
		print(args)
		subprocess.call(args)
		os.remove(rarfile)
		
def checkFiles(folderPath):
	uncompress(folderPath)
	for btfile in glob.iglob(folderPath + "*.torrent"): #.torrent
		dest_file = processed_dir + os.path.basename(btfile)
		print(dest_file)
		if os.path.exists(dest_file):
			os.remove(dest_file)
		shutil.move(btfile, processed_dir)
		args = [bc_cmd, dest_file, '-o ' + dl_dir, '-s']
		subprocess.Popen(args) 

def longRunningProcess():
	while True:
		checkFiles("E:\\")
		time.sleep(5)


longRunningProcess()
