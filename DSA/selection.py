

def selection_sort(arr: list[str]):
    for i in range(len(arr)):
        for j in range(i+1):
            for k in range(j, len(arr)):
                if arr[j] > arr[k]:
                    if arr[i] > arr[k]:
                        arr[i], arr[k] = arr[k], arr[i]

    print(arr)
                


if __name__=='__main__':
    arr = [64, 12, 25, 22, 11]

    selection_sort(arr)