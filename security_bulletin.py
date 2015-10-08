#!/usr/bin/env python

import re
import sys
import os
import commands
#Manually set target project here because it's so confused when trying to handle multiple projects at the same time.
#target = '/mnt/disk3/robin_yeh/clv/rel/'
target = '/mnt/disk3/robin_yeh/mfd/mr2/'
#target = '/mnt/disk3/robin_yeh/mfd/zx/'
#target = '/mnt/disk3/robin_yeh/8939/rel/'

def usage():
  print "usage:"
  print "     1		applying patches"
  print "     push	push commits to Gerrit"
  print "     0		clean up"

#Get target dir list and Copy patches
def getDirlist():
  dirlist = []
  for (cur, dirs, files) in os.walk('.'):
    if files:
      dirlist.append(cur)
      for fname in files:
        cmd = 'cp '+cur+'/'+fname+' '+target+cur
        #print cmd
        os.system(cmd)
  print dirlist
  return dirlist

def main():
  args = sys.argv[1:]
  if not args or args[0] not in ['0','1','push']:
    usage()
    return

  failed = []
  dirlist = getDirlist()
  
  for dir in dirlist:
    os.chdir(target+dir)
    print '=============================================================================='
    print 'starting',os.getcwd()
    if args:
      #1.Start applying patches
      if args[0] =='1':
        os.system('git checkout -b patch')
        (status, result) = commands.getstatusoutput('git am *.patch')
        #if status:
        #  sys.stderr.write(result)
        #  sys.exit(1)
        print result
        match = re.search('abort',result)
        if match:
          failed.append(dir)
        print 'done at',os.getcwd()

      #2.Push to Gerrit
      elif args[0] =='push':
        os.system('push')

      #3.Clean up
      elif args[0] =='0':
          os.system('git am --abort')
          os.system('rm -rf *.patch')
          os.system('git checkout master')
          os.system('git branch -D patch')

    #check patches applied result
    if args[0] =='1':
      print '=============================================================================='
      if failed:
        print 'Patches apply failed at',failed
      else:
        print 'All patches apply success!'

if __name__ == "__main__":
  main()

  """
  for (cur, dirs, files) in os.walk('.'):
    depth = len(cur.split('/'))
    print "--" * depth, cur
    for fname in files:
        print "--" * (depth + 1), fname
  """