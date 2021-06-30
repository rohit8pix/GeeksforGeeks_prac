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
		  k=tuple(sorted(ele))  # sorted the characters of the word and made it tuple --- this is our KEY
		  anag[k].append(ele)   # if elements of words list match KEY then we store the word as VALUES
	  return(list(anag.values()))
