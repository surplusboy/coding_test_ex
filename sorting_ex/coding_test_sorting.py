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
    앞서 살펴봤던 예제 정렬 알고리즘보다 많이 쓰이는 알고리즘으로서, 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬 알고리즘이다.
    피벗(pivot)은 큰 숫자와 작은 숫자를 교환할 때, 기준이 되는 숫자로서, 퀵 정렬 수행 전 피벗을 먼저 명시하여야 한다.
    위의 예제는 가장 대표적인 피벗 분할 방식인 호어 분할방식을 기준으로 하여 작성되었다.
    
    호어 분할 : 리스트에서 첫 번째 데이터를 피벗으로 지정한다. 
    
    퀵 정렬의 시간 복잡도는 평균적으로 O(NlogN) 이며 (일반적으로 컴퓨터 과학에서 log의 의미는 밑이 2인 log2N을 의미한다.)
    이미 데이터가 정렬되어 있는 최악의 경우일때 O(N^2)가 된다.
    하지만 정렬 라이브러리를 제공하는 언어들은 최악의 경우에도 O(NlogN)을 보장 할수 있도록 피벗값을 설정할 때 추가적인 로직을 더해준다.
    이는 파이썬 내부의 정렬 라이브러리도 동일하다.
    '''

def count_sort(): # 계수 정렬 예제, 171
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    sort_array = list()

    count = [0] * (max(array) +1)

    print(count)

    for i in array:
        count[i] += 1

    '''
    책에선 아래와 같은 예시지만, 
    for i in range(len(array)): # len(array) = 15, range(15) = 0 ~ 14, i = 0
        count[array[i]] += 1  # array[0] = 7, count[7] += 1
    같은 구조이므로 위와 같이 간결하게 작성해도 흐름 상 문제가 없다고 생각
    '''

    print(count)

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
            sort_array.append(i)

    print(f'\n{sort_array}')

    '''
    계수 정렬 알고리즘은 특정한 조건이 부합할 때만 사용할 수 있는 알고리즘이다.
    조건은 '데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을때' 사용이 가능하다.
    '모든 범위를 담을 수 있는 크기의 리스트를 선언' 해야 한다는 조건 때문에 가장 작은 데이터와 큰 데이터의 차이가 너무 클때 사용할 수 없다.
    앞선 예제의 알고리즘의 차이는 계수 정렬 알고리즘은 비교 기반의 정렬 알고리즘이 아니다.
    
    계수 정렬의 시간 복잡도는 O(N+K) 이다. (K는 데이터 중 최대값의 크기)
    기수 정렬 (Radix Sort) 과 더불어 가장 빠른 알고리즘 중 하나이다.
    '''

def various_sort_ex(): # 파이썬 기본 정렬 알고리즘들

    array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    result1 = sorted(array1)

    print(f'sorted(array): {result1}')
    array2.sort()
    print(f'array.sort(): {array2}')

    '''
    파이썬의 기본 정렬 라이브러리인 sorted() 함수는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌다. (병합 정렬 + 삽입 정렬의 하이브리드 방식)
    일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다는 특징이 있다.
    리스트, 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형이다.
    
    리스트 객체의 내장 함수인 sort()는 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬된다.
    '''

def key_utilize_sort_ex():
    array = [('바나나', 2),('사과', 5), ('당근', 3)]

    def setting(data):
        return data[1]

    result = sorted(array, key=setting)
    print(result)

    '''
    코딩테스트에서 정렬 알고리즘이 사용되는 경우는 크게 3가지 문제 유형으로 나타난다.
    1. 정렬 라이브러리로 풀 수 있는 문제 : 단순히 정렬 기법을 알고 있는지 물어보는 문제, 기본 정렬 라이브러리 사용 방법 숙지 필요
    2. 정렬 알고리즘의 원리에 대해서 물어보는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 드으이 원리를 알고 있어야 풀 수 있다.
    3. 더 빠른 정렬이 필요한 문제 : 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며, 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나, 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 함. 
    '''