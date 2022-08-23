outputs=[]
for inp in range(2**6):
	inpbin='{0:06b}'.format(inp)
	b1,b2,b3,b4,b5,b6 = [int(bit) for bit in inpbin]
	o1 = b1^(b2 & b3 & b4)
	o2 = (b3 & b4 & b5) ^ b6
	o3 =  b1^(b4 & b5 & b2)
	o4 = (b5 & b2 & b3)^b6
	outputs.append('{}{}{}{}'.format(o1,o2,o3,o4))
	print('Input bits: {} Output bits: {}'.format(inpbin,(o1,o2,o3,o4)))
outputs=set(outputs)
print(outputs,len(outputs))
