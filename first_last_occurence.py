def first_occurence(arr,target):
	l,h = 0,len(arr)-1
	while(l<=h):
		m = l+(h-l)//2		
		if arr[m]<target:
			l=m+1
		else:
			h=m-1
	return l

def last_occurence(arr,target):
	l,h = 0,len(arr)-1
	ans = -1
	while(l<=h):
		m=l+(h-l)//2
		if arr[m]>target:
			h=m-1
		else:
			l=m+1
	return h

if __name__ == '__main__':
	arr = [2,4,4,4,4,5,7,9,11]
	target = 12
	print(first_occurence(arr,target))
	print(last_occurence(arr,target))
