def bubble_sort(arr):
    n = len(arr)
    # 遍历数组的所有元素
    for i in range(n):
        # 最后i个元素已经是排序好的
        for j in range(0, n - i - 1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 示例使用
if __name__ == "__main__":
    # 示例数组
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("排序前的数组:", arr)

    sorted_arr = bubble_sort(arr)
    print("排序后的数组:", sorted_arr)
