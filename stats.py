from collections import defaultdict

def count_words(filepath):
	with open(filepath) as f:
		filetext = f.read()
		wordlist = filetext.split()
		return f"Found {len(wordlist)} total words"
	
def count_chars(filepath):
	with open(filepath) as f:
		filetext = f.read()
		filetext = filetext.lower()
		charsdict = {}
		dictlist = []
		endlist = []
		for i in filetext:
			if i.isalpha() == True:
				if i not in charsdict:
					charsdict[i] = 1
				else:
					charsdict[i] += 1
		for key, value in charsdict.items():
			currentdict=defaultdict(dict)
			currentdict['char']=key
			currentdict['num']=value
			dictlist.append(currentdict)
			dictlist.sort(reverse=True, key=sort_on)
			output = [[d.get("char"), d.get("num")] for d in dictlist]
		for c, n in output:
			print(f"{c}: {n}")
		#return output
#		return charsdict

def sort_on(items):
    return items["num"]

#def dictionary_lister(dict):

