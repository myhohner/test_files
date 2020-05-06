import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-4, 4,50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
l,=plt.plot(x, y,linewidth=10)
m,=plt.plot(y, x,linewidth=10)
plt.legend(handles=[l,m],labels=['one','two'],loc='upper right')


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0)) 
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0)) 

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.7))


x0 = 1
y0 = 2*x0 + 1

'''
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# set dot styles
plt.scatter([x0, ], [y0, ], s=50, color='b')
'''


plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

plt.show()