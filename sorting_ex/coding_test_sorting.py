import random

def selection_sort(): # 선택 정렬 예제, 159
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)): # 0
        min_index = i # min_index = 0
        for j in range(i + 1, len(array)): # 1
            if array[min_index] > array[j]: # (array[0] = 7) > (array[1] = 5)
                min_index = j # min_index = 5
        array[i], array[min_index] = array[min_index], array[i] # array[0], array[5] = a

    print(array)

    '''
    선택 정렬의 시간 복잡도는 N * (N + 1) / 2 번의 연산을 수행하게 된다. -> O(N^2)
    데이터의 갯수가 늘어날 수록 처리속도가 급격하게 느려 지지만
    코딩테스트에 특정한 리스트에서 가장 작은 데이터를 검색하는 문제가 있을 수 있으니 익숙해져야 하는 정렬 방법이다.
    '''

def swap_code_ex(): # 파이썬에서의 원소간의 스왑은 간단하다
    array = [3, 5]
    array[0], array[1] = array[1], array[0]

    print(array)

    # 타 언어의 문법으로 구현한 Swap 예제
    ''' 
    int a = 3;
    int b = 5;
    
    int temp = a;
    a = b;
    b = temp
    '''

    # 명시적으로 임시 저장용 변수를 만들어 두 원소의 값을 변경하는것을 확인할 수 있다.


def insertion_sort(): # 삽입 정렬 예제, 164

    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(array)):
        for j in range(i, 0, -1): # i 에서 1 까지 -1 (start, end, step) 의 매개 변수, step에 -1 이 들어갈 시 start 부터 end + 1 까지 -1 감소
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    return array

    '''
    삽입 정렬은 리스트의 0번째 인덱스는 그 자체로 정렬되어 있다고 판단한다.  
    두번째 인덱스의 데이터가 좌, 우 중 어느 위치로 들어갈지 판단한다. 
    '''


def quick_sort(array, start, end): # 퀵 정렬 예제, 16
    # array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    # quick_sort(array, 0, 9)
    if start >= end:

        return

    pivot = start # 0
    left = start + 1 # 1
    right = end # 8

    while left <= right:
        # print(array[left])
        # 피벗 보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]: # 1, 8 and array[1], array[0] -> 7, 5

            left += 1
            print('left', left)
            print(input('left debug'))

        # 피벗 보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            # print(array[right])
            right -= 1
            print('right', right)
            print(input('right debug'))

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)

    '''
    위의 예제 정렬 알고리즘보다 많이 쓰이는 알고리즘으로서, 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬 알고리즘이다.
    피벗(pivot)은 큰 숫자와 작은 숫자를 교환할 때, 기준이 되는 숫자로서, 퀵 정렬 수행 전 피벗을 먼저 명시하여야 한다.
    위의 예제는 가장 대표적인 피벗 분할 방식인 호어 분할방식을 기준으로 하여 작성되었다.
    
    호어 분할 : 리스트에서 첫 번째 데이터를 피벗으로 지정한다. 
    '''





