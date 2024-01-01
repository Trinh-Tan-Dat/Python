list = [3, 1, 2, 5, 9, 8, 10, 22, 12]
target_value = 8


def linear_search(arr, n):
    for i in range(len(arr)):
        if(n == arr[i]):
            return i;
    return -1;

print(linear_search(list, target_value));