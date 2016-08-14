#!/bin/python
import re,os
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
#files.remove('sub.py')

for file in files:
    with open(file) as f:
        content = f.read().replace('003366','FFFFFF')
    with open(file, 'w') as f:
        f.write(content)
