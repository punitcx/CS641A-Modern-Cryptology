import math
a,x=(429,  431955503618234519808008749742)
b,y=(1973, 176325509039323911968355873643)
c,z=(7596, 98486971404861992487294722613)

p = 455470209427676832372575348833
u,v = -2298, 631
xinv = pow(x,-1,p)
yinv = pow(y,-1,p)


t1 = pow(y*xinv,u,p) # ((x*yinv)**u)%p
t2 = pow(z*yinv,v,p)  # ((y*zinv)**v)%p
g = pow(t1*t2,1,p)
print(t1,t2)
print('g = {}'.format(g),'\nPassword = {}'.format((x*pow(g**a,-1,p))%p))
