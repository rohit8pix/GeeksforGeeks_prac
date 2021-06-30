from collections import defaultdict
def Anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram
    '''
    
    #code here
    anag=defaultdict(list)
	  for ele in words:
		  k=tuple(sorted(ele))
		  anag[k].append(ele)
	  return(list(anag.values()))
