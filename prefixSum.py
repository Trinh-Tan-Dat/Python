arr = [1,2,3,4,5]
prefixSum = [0] * len(arr);
prefixSum[0] = arr[0] 
for i in range (1, len(arr)):
    prefixSum[i] = prefixSum[i - 1] + arr[i];

print(prefixSum)