import sys
import re
import os

#pattern = "^\d\d-\d\d\s\d\d\:\d\d\:\d\d\.\d\d\d\s+\d"
filter = ["ThermalEngine","CM36283"]
keyword = ["ANR\sin","\sF\s","DEBUG","boot completed","\sdied","AndroidRuntime","fatal","WATCHDOG","Power-on\sreason","Power-off"]

def contain(txt,pattern,flag): 
	for pat in pattern:
		if re.search(pat, txt):
			return True == flag
	return False == flag
   
def main():
	dir = os.getcwd()
	flist = sorted(os.listdir(dir))
	"""
	if len(sys.argv) >= 2:
		file = sys.argv[1]
	else:
		print "usage : parse_log.py logcat.txt"
	print file
	"""
	#read file
	fo1 = open("Suspects.log", "w")
	for file in flist:
		fo1.write("============================================="+file+" begin=============================================\n")
		f = open(file, 'rU')
		fo = open(file+".log", "w")
		for line in f:
			if contain(line,filter,False):
				fo.write(line)
			if contain(line,keyword,True):
				fo1.write(line)
		f.close()
		fo.close() 
		fo1.write("========================================"+file+" done.========================================\n")
	fo1.close()

if __name__ == '__main__':
	main()
