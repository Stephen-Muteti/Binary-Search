def lower_bound(arr,target):
	l,h = 0, len(arr)-1
	while(l<=h):
		m = l+(h-l)//2
		if arr[m] == target:
			return m
		if arr[m] < target:
			l = m+1
		if arr[m] > target:
			h = m-1
	return l

if __name__ == '__main__':
	arr = [2,4,5,7,9,11]
	target = 12
	print(lower_bound(arr,target))