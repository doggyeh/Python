#!/usr/bin/env python

import sys
import re
import os
import shutil
import commands
import subprocess

def main():
  """
  args = sys.argv[1:]
  if not args:
    print "usage: push.py";
    sys.exit(1)
  """
  cmd = 'git branch'
  (status, branch) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(branch)
    sys.exit(1)

  cmd = 'git branch -r'
  (status, branch_r) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(branch_r)
    sys.exit(1)
  
  #search keyword
  match = re.search('\*\s(\w*)',branch)
  if match:
    branch = match.group(1)
  while 1:
    match = re.search('->\s(\w+)([\w\W]*)$',branch_r)
    if match:
      fdc = match.group(1)
      branch_r = match.group(2)
    else :
      break
  #start git push
  cmd = 'git push '+fdc+' '+branch+':refs/for'+branch_r
  print cmd
  os.system(cmd)
  
if __name__ == "__main__":
  main()
