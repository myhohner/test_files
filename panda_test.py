import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

test=pd.DataFrame(np.arange(10).reshape(5,2),columns=list('AB'))
'''
#混合选择
print(test.ix[:2,['A']])
'''
'''
#条件修改
test.B[test.A==0]=0
print(test)
'''

left=pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']},index=['k0','k1','k2'])
right=pd.DataFrame({'C':['C0','C2','C3'],'D':['D0','D2','D3']},index=['k0','k2','k3'])
middle=pd.DataFrame({'A':['A0','A1','A2'],'B':['B0','B1','B2']},index=['k0','k1','k2'])

'''
#横向合并
res=pd.concat([left,right],join_axes=[left.index],axis=1)
print(res)
'''

'''
res=pd.merge(left,right,left_index=True,right_index=True,how='outer')
print(res)
'''

'''
#纵向合并
res1=pd.concat([left,right],axis=0)
print(res1)
res2=pd.concat([left,right],axis=0,ignore_index=True)
print(res2)
'''

'''
#纵向合并,middle下合并其他两个
res=middle.append([left,right],ignore_index=True)
print(res)
'''

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

'''
#避免overlapping的合并
people=pd.merge(boys,girls,on='k',suffixes=['_boys','_girls'],how='inner')
print(people)
'''


'''
#添加一列数据
test['C']=pd.Series(np.arange(2,7))
print(test)
'''


'''
#dataframe排序
#test1=test.sort_index(axis=0,ascending=False)
test2=test.sort_values(by='B',ascending=False)
print(test2)
'''

'''
data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data=data.cumsum()
ax=data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()
'''

