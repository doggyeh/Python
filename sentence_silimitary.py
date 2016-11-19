import sys
import re
import os
import nltk.corpus
import nltk.tokenize.punkt
import string

def contain(txt,pattern,flag): 
	for pat in pattern:
		if re.search(pat, txt):
			return True == flag
	return False == flag
   
def main():
	stopwords = nltk.corpus.stopwords.words('english')
	stopwords.extend(string.punctuation)
	stopwords.append('')
	print stopwords

if __name__ == '__main__':
	main()
