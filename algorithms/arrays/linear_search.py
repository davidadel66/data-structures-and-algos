from typing import Optional, Literal, Union, List
import numpy as np
import time

def linearSearch(array: List, value: Union[int, float]):
    "Iterate through the array until the value is found"
    for i in array:
        if i == value:
            return i
    return -1


def linearSearchV2(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1




if __name__ == "__main__":
    arr = np.random.randint(0, 10000000, size=100, dtype=int)
    val = np.random.randint(10000000)

    runs = 10

    v1 = []
    v2 = []

    for i in range(runs):
        start = time.time()

        linearSearch(arr, val)

        end = time.time()
        start = time.time()

        elapsed = start - end
        v1.append(elapsed)

        elapsed = start - end
        v2.append(elapsed)

    v1Average = sum(v1) / len(v1)
    v2Average = sum(v2) / len(v2)

    print(f'v1 average {v1Average}')
    print(f'v2 average {v2Average}')

        

        


