def maxSum(arr,n,k):
    if not n > k:
        print("Invalid")
        return -1
    max_sum = -5000
    window_sum = sum([arr[i] for i in range(k)])
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum,max_sum)
    return max_sum


if __name__ == '__main__':
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    n = len(arr)
    k = 4
    print(maxSum(arr,n,k))
