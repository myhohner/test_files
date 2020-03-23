import multiprocessing as mp


def test(x):
    return x*x

def multicore():
    pool=mp.Pool()
    res_all=[pool.apply_async(test,(i,)) for i in range(10)]
    print([res.get() for res in res_all])
    #res=pool.map(test,range(10))
    #print(res)

if __name__=='__main__':
    multicore()

