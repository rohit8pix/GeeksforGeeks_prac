class Solution:

	def matchPairs(self,nuts, bolts, n):
		# code here
		pref = ['!', '#', '$' ,'%' ,'&','*', '@','^','~']
        prior={}
        for i in range(len(pref)):
	        prior[i+1]=pref[i]

        def getpriority(element):
        	for k,v in prior.items():
        		if v==element:
        			return k
        			break
        
        for i in range(len(nuts)):
        	nuts[i]=getpriority(nuts[i])
        	bolts[i]=getpriority(bolts[i])
        nuts.sort()
        bolts.sort()
        
        for i in range(len(nuts)):
        	nuts[i]=prior[nuts[i]]
        	bolts[i]=prior[bolts[i]]
        
