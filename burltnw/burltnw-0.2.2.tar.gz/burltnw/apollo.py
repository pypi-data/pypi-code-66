import os
import subprocess
import sys

class apollo:
	def __init__(self):
		self.file=str(os.path.join(sys.path[5],"burltnw\\Apollo_SDK_exe\\burl.exe"))

	def get_status(self):
		_status=str(subprocess.Popen([self.file,"status"],stdout=subprocess.PIPE))
		if "subprocess.Popen" in _status :
			_status = None
		return _status

	def get_battery(self):
		_battery=str(subprocess.Popen([self.file,"battery"],stdout=subprocess.PIPE))
		if "subprocess.Popen" in _battery:
			_battery = None
		return _battery

	def walk(self,x,y):
		os.system(self.file+" move "+str(x)+" "+str(y))

	def rotate(self,degree):
		os.system(self.file+" rotate "+str(degree))

	def home(self):
		os.system(self.file+" home")