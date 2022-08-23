cipher=list("iRqy9U1qdgt")
print("Cipher={}".format(cipher))
for i in range(1,10):
	cip=list(cipher)
	cip[4]=str((int(cip[4])+i)%10)
	cip[6]=str((int(cip[6])+i)%10)
	print("Number Increment Shift {}".format(i),''.join(cip))

