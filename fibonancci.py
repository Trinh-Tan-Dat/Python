import math
import multiprocessing
import time
from decimal import Decimal




def fib(n):
    if n<=1:
        return n
    else:
        return Decimal(((1+math.sqrt(5))**n - (1-math.sqrt(5))**n)/(2**n*math.sqrt(5)))
def fib_parallel(m):
    if m <= 10:
        return fib(m)
    else:
        if m % 2 == 0:
            n = m//2
            k = m//2
        else:
            n = (m-1)//2
            k = (m+1)//2
        result = fib_parallel(n + 1) * fib_parallel(k) + fib_parallel(n) * fib_parallel(k - 1);
    return result;



def testF():
    m = 2000;
    if(m > 1000):
        if m % 2 == 0:
            n = m//2
            k = m//2
        else:
            n = (m-1)//2
            k = (m+1)//2
    worker = [n+1,k,n,k-1]
    with multiprocessing.Pool() as pool:
        result = pool.map(fib_parallel,worker)
        pool.close()
        pool.join()
    return result[0] * result[1] + result[2] * result[3]


if __name__ == "__main__":
    start = time.time()
    testF()
    print("Execution time: ", time.time() - start)

