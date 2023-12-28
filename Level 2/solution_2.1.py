def solution(s):
	r = 0
	salutes = 0
	for chr in s:
		if (chr == ">"):
			r = r + 1
		elif (chr == "<"):
			salutes = salutes + (2 * r)
	return salutes