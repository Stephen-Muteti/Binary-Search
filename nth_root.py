def find_nth_root(nth,target):
	ans = -1
	l,h = 1,target
	while(l<=h):
		m = l+(h-l)//2
		root = 1
		for i in range(0,nth): root = root*m
		if root == target: 
			ans = m
			break
		elif root > target: h = m-1
		else: l = m+1
	return ans

if __name__ == '__main__':
	nth = 4
	target = 16
	print(find_nth_root(nth,target))