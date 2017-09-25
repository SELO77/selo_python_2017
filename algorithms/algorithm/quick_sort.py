def quick_sort(arr):
    if len(arr) < 2:
        return arr
    left = []
    right = []
    pivot = arr[0]
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    import random

    def generate_test_set():
        return [random.randint(0, 99999) for _ in range(1000)]

    def test():
        print(quick_sort(generate_test_set()))

    for _ in range(2):
        test()