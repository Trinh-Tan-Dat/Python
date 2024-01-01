import numpy as np
import time
import multiprocessing
matrix = np.random.randint(1, 10, (1000, 1000));
arr = [0] * matrix.shape[0];
for i in range(matrix.shape[0]):
    arr[i] = len(matrix[i])

def scan_r(args):
    s, t, offset, prefixSum = args
    if s == t:
        prefixSum[s] = offset + arr[s]
        return 
    mid = (s + t) // 2
    scan_r((s, mid, offset, prefixSum))
    for i in range(s, mid + 1):
        offset += arr[i]
    scan_r((mid + 1, t, offset, prefixSum))

def flatten(args):
    i,j,index,result = args
    for k in range(i,j):
        result[k*matrix.shape[0]:index[k]] = matrix[k][0:matrix.shape[0]]

if __name__ == "__main__":
    start = time.time()
    manager = multiprocessing.Manager()
    prefixSum = manager.list([0] * len(arr))
    result = manager.list([0] * matrix.size)
    count_cpu = multiprocessing.cpu_count()
    worker = []
    for i in range(count_cpu):
        if i == count_cpu - 1:
            worker.append((i * len(arr) // count_cpu, len(arr) - 1, sum(arr[0: i * len(arr) // count_cpu]), prefixSum))
        else:
            worker.append((i * len(arr) // count_cpu, (i + 1) * len(arr) // count_cpu - 1, sum(arr[0: i * len(arr) // count_cpu]), prefixSum))

    with multiprocessing.Pool() as pool:
        pool.map(scan_r, worker)
        pool.close()
        pool.join()

    worker2 = []
    for i in range(count_cpu):
        if i == count_cpu  - 1:
            worker2.append((i * len(arr) // count_cpu, len(arr), prefixSum, result))
        else:
            worker2.append((i*len(arr)//count_cpu, (i+1)*len(arr)//count_cpu , prefixSum, result))

    with multiprocessing.Pool() as pool:
        pool.map(flatten, worker2)
        pool.close()
        pool.join()
    print("Result:")
    print(result)
    end = time.time()
    print(end - start)
    print(len(result))