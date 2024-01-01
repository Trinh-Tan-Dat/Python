import multiprocessing
import time
import numpy as np
arr = np.random.randint(1,2,10000);
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

if __name__ == "__main__":
    start = time.time();
    manager = multiprocessing.Manager()
    prefixSum = manager.list([0] * len(arr))
    count_cpu = multiprocessing.cpu_count()
    # worker = [(0, len(arr) // 2, 0, prefixSum),(len(arr) //2, len(arr) - 1, sum(arr[0: len(arr) // 2 ]), prefixSum) ]
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
    print(list(prefixSum))
    end = time.time()
    print("Time: ", end - start)