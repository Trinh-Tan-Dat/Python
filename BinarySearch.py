list = [0, 10, 20, 30, 40, 50, 60, 70]
target_value = 50


def binary_search(arr, n):
    left = 0;
    right = len(arr) - 1;
    while left <= right:
        mid = left + (right - left) // 2;
        if arr[mid] == n:
            return mid;
        elif arr[mid] < n :
            left = mid + 1;
        else:
            right = mid - 1;
    return -1;

print(binary_search(list, target_value))