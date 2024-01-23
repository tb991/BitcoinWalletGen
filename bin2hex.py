bi = ""
def go():
	c1 = 0
	num = ""
	hexnum = ""
	while c1 < len(bi):
		#print(bi[c1], end="")
		num += bi[c1]
		c1 += 1
		if c1 % 4 == 0:
			print("", end="")
			if num == '0000':
				hexnum += '0'
			elif num == '0001':
				hexnum += '1'
			elif num == '0010':
				hexnum += '2'
			elif num == '0011':
				hexnum += '3'
			elif num == '0100':
				hexnum += '4'
			elif num == '0101':
				hexnum += '5'
			elif num == '0110':
				hexnum += '6'
			elif num == '0111':
				hexnum += '7'
			elif num == '1000':
				hexnum += '8'
			elif num == '1001':
				hexnum += '9'
			elif num == '1010':
				hexnum += 'A'
			elif num == '1011':
				hexnum += 'B'
			elif num == '1100':
				hexnum += 'C'
			elif num == '1101':
				hexnum += 'D'
			elif num == '1110':
				hexnum += 'E'
			elif num == '1111':
				hexnum += 'F'
			#print(hexnum, end="")
			num = ""
	return hexnum
