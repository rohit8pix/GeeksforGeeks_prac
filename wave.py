#a = [1,2,3,4,5]
a = [1,9,10,12]


def convertToWave(a):
	for i in range(0,len(a)-1,2):
		a[i],a[i+1]=a[i+1],a[i]
	print(a)

convertToWave(a)
