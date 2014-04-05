"""
Algorithm to find switch over point of an array that first increases then decreases
"""

array = [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3]

def get_index_of_max(array_in):
	print array_in
	length = len(array_in)
	mid_p = length//2
	if length == 2:
		return mid_p+1
	elif array_in[mid_p] <= array_in[mid_p+1]:

		return mid_p + get_index_of_max(array_in[mid_p:length])
	else:
		
		return get_index_of_max(array_in[0:mid_p])

print get_index_of_max(array)