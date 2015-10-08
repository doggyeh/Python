import sys
import re

pattern = "^\d\d-\d\d\s\d\d\:\d\d\:\d\d\.\d\d\d\s+\d"

def grp(pat, txt): 
	r = re.search(pat, txt)
	#print r.group(0) if r else 'not found'
	return r.group(0) if r else '0'

   
def main():
	if len(sys.argv) >= 2:
		file = sys.argv[1]
	else:
		print "argument error"
	if len(sys.argv) == 3:
		file1 = sys.argv[2]
	#read file
	f = open(file, 'rU')
	list = f.readlines()
	f.close()
	if (file1):
		f = open(file1, 'rU')
		list1 = f.readlines()
		f.close()
		list += list1
	#sort
	list.sort(key = lambda l:grp(pattern,l))
	#output
	fo = open(file+".log", "w")
	for i in list:
		if re.search(pattern, i):
			fo.write(i)
	fo.close() 

if __name__ == '__main__':
	main()
