def can_partition(arr,mid):
	part,s = 1,0
	for item in arr:
		if s+item <= mid:
			s = s+item
		else:
			part = part + 1
			s = item
	return part
def partion(arr,k):
	low, high = min(arr), sum(arr)
	while(low<=high):
		mid = low+(high-low)//2
		parts = can_partition(arr,mid)
		if parts <= k:
			high = mid-1
		else:
			low = mid+1
	return low

if __name__ == '__main__':
	arr = [10,20,30,40]
	k = 2
	print(partion(arr,k))