import re
a='2345'

'''
print(True) if a==2 else print(False)
'''
'''
#字符串分割成列表
res=a.split('3')
print(res)
'''
'''
#用map函数完成两列表中数字相加
a1=[1,2,3]
a2=[2,3,4]
res=list(map(lambda x,y:x+y,a1,a2))
print(res)
'''
'''
res=a.split('3')
print(res)
'''

selenium_grid_url=''
capabilities=DesiredCapabilities.CHROME
driver=webdriver.Remote(desired_capabilities=capabilities,command_executor=selenium_grid_url)