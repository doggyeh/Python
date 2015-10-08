import nltk.corpus
import nltk.tokenize
import nltk.stem
import nltk.tag
import string

target_question = ["In the eighteenth century it was often convenient to regard man as a clockwork automaton.",
					"Please check my account balance."]

questions = [
			# question1
			 "In the eighteenth century it was often convenient to regard man as a clockwork automaton.",
             "in the eighteenth century    it was often convenient to regard man as a clockwork automaton",
             "In the eighteenth century, it was often convenient to regard man as a clockwork automaton.",
             "In the eighteenth century, it was not accepted to regard man as a clockwork automaton.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automata.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automatons.",
             "It was convenient to regard man as a clockwork automaton in the eighteenth century.",
             "In the 1700s, it was common to regard man as a clockwork automaton.",
             "In the 1700s, it was convenient to regard man as a clockwork automaton.",
             "In the eighteenth century.",
             "Man as a clockwork automaton.",
             "In past centuries, man was often regarded as a clockwork automaton.",
             "The eighteenth century was characterized by man as a clockwork automaton.",
             "Very long ago in the eighteenth century, many scholars regarded man as merely a clockwork automaton.",
			# question2 
			 "Could you tell me what my account balance is",
			 "What is my account balance",
			 "How can I check my account balance",
			 "Please check my account balance."
			 ]

answers = [ "Bingo, question1 hit!",
			"Here is your account balance:987654321",
			"Sorry, you can call MR XXX 0912345678 for further information.",
			]

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)

# Create tokenizer and stemmer
tokenizer = nltk.tokenize.TreebankWordTokenizer()
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

def is_match(b,questions_token):
    
	pos_b = nltk.pos_tag(tokenizer.tokenize(b))
	tokens_b = [token.lower().strip(string.punctuation) for token, pos in pos_b if pos.startswith('N') and (token.lower().strip(string.punctuation) not in stopwords)]
	stems_b = [lemmatizer.lemmatize(token) for token in tokens_b if len(token) > 0]

	# Calculate Jaccard similarity
	max = target = 0
	for i in range(len(target_question)):
		tokens = questions_token[i]
		ratio = len(set(tokens).intersection(stems_b)) / float(len(set(tokens).union(stems_b)))
		if ratio > max:
			max, target = ratio, i
			print "----",(stems_b,tokens,ratio),"----"
	#The final match result
	if max >= 0.66:
		print (b,answers[target],max)
	else:
		print (b,answers[len(answers)-1],max)

def init(questions):
	questions_token =[]
	for question in questions:
		pos_a = nltk.pos_tag(tokenizer.tokenize(question))
		tokens_a = [token.lower().strip(string.punctuation) for token, pos in pos_a if pos.startswith('N') and (token.lower().strip(string.punctuation) not in stopwords)]
		stems_a = [lemmatizer.lemmatize(token) for token in tokens_a if len(token) > 0]
		questions_token.append(stems_a)
	return questions_token


def main():
	print "target question =",target_question
	questions_token = init(target_question)
	for question in questions:
		is_match(question,questions_token)


if __name__ == '__main__':
	main()
"""
def get_wordnet_pos(pos_tag):
	if pos_tag[1].startswith('J'):
		return (pos_tag[0], wordnet.ADJ)
	elif pos_tag[1].startswith('V'):
		return (pos_tag[0], wordnet.VERB)
	elif pos_tag[1].startswith('N'):
		return (pos_tag[0], wordnet.NOUN)
	elif pos_tag[1].startswith('R'):
		return (pos_tag[0], wordnet.ADV)
	else:
		return (pos_tag[0], wordnet.NOUN)
"""