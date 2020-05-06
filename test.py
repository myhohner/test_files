
def foo():
    print('Start')
    while True:
        res=yield 4
        print('res:',res)

g=foo()

print(next(g),'\n************\n')
print(next(g),'\n************\n')
print(next(g),'\n************\n')

