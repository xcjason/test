import random

def findMedian(L):
	return recur(L, len(L) / 2)

def recur(L, k):
	elem = random.choice(L)
	low = [i for i in L if i < elem]
	up = [i for i in L if i > elem]
	print L, k, elem
	if len(low) == k: return elem
	if len(low) > k: return recur(low, k - 1)
	if len(low) < k: return recur(up, k - len(low))


if __name__ == '__main__':
	L = [3, 43, 6, 1, 90, 4, 9, 8, 24, 23, 65, 7, 1235, 0]
	print sorted(L)
	print findMedian(L)