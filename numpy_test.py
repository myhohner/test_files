import numpy as np
t1=np.arange(1,5,1).reshape(2,2)
t2=np.arange(5,1,-1).reshape(2,2)
m3=np.random.randn(4).reshape(2,2)

print(t1)

'''
#纵向分割#
print(np.split(t1,2,axis=1)) 
'''
'''
n1=np.array([1,2,3,4])
r1=n1[np.newaxis,:]
r2=n1[:,np.newaxis]
print(r1)
print(r2)
'''
'''
#合并
t=np.concatenate([t1,t2],axis=0)
print(t)
'''
'''
#合并
m=np.vstack((t1,t2))
'''
'''
#一维转二维
A=np.array([1,2,3])
A=A[np.newaxis,:]
print(np.ndim(A))
print(A)
'''
'''
#分割
t_split=np.split(t,2,axis=0)
print(t_split)
'''

