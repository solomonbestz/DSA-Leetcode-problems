from typing import List
from time import perf_counter


def linear_search(datas: List[int]):
    start_time = perf_counter()
    for n in range(len(datas)):
        if target == datas[n]:
            print(f"Found {target} at index {n}")
            break
    stop_time = perf_counter()
    print(f"The Time to find the target {target} took {stop_time-start_time} seconds")

if __name__=='__main__':
    data_range = 1_000_000
    datas = []
    
    for data in range(1, data_range+1):
        
        datas.append(data)

    
    target = 98765
    print(datas)
    linear_search(datas)
