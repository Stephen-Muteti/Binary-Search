def upper_bound(arr,target):
	l,h = 0,len(arr)-1
	while(l<=h):
		m = l + (h-l)//2
		if arr[m] == target: return arr[m]
		if arr[m] < target: l=m+1
		if arr[m] > target: h=m-1
	return arr[h] if 0<=h<len(arr) else h

if __name__ == '__main__':
	arr = [2,4,5,7,9,11]
	target = 14
	print(upper_bound(arr,target))