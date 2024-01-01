def devive_conquer_sum(arr):
    if(len(arr) == 0):
        return 0;
    elif len(arr) == 1:
        return arr[0];
    else:
        middle = len(arr) // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        left_sum = devive_conquer_sum(left_arr)
        right_sum = devive_conquer_sum(right_arr)
        return left_sum + right_sum;

arr = [1,2,4,5,6,7,8]
print(devive_conquer_sum(arr))