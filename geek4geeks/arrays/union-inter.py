'''
This is to return the union and intersection of two sorted arrays.
'''

'''
Algoruthm for union
What we did for union is that, union is defined as elements found in either set A or set B or both in set A and set B
so we start off by having two counters for both sets(A&B); lets say i and j. check A[i]  < B[j] we save A[i] in union
array and increase the value of i. if its the opposite i.e A[i] > B[j], we add b[j] in to union and increment j by 1
if dey are both the same, add either A[i] or b[j] to union and increase both (i & j)
'''

def union():
	pass