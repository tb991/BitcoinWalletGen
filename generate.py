import random
b = ""
while True:
	a = random.randint(0,1)
	b = b + str(a)
	if len(b) == 256:
		break
out = b
