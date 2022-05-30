def sequential_search(n, target, array): # 순차 탐색의 소스 구현
    # n : 배열의 총길이, target : 찾고자 하는 값, array : 데이터 집합
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소와 target 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재 위치 return

'''
가장 기본적인 탐색 알고리즘으로서, 단어 그대로 특정 데이터를 찾기위해 리스트의 앞에서부터 하나씩 차례대로 확인하는 방법이다.
파이썬의 count() 함수도 내부에서는 순차 탐색이 수행된다.
최악의 경우 시간복잡도는 O(N)이 된다.
'''

def recursive_binary_search(array, target, start, end): # 재귀적으로 구현한 이진 탐색 소스 코드
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        print(mid)
        print('넘어옴')
        return recursive_binary_search(array, target, start, mid - 1)
    else:
        print(mid)
        print('안넘어옴')
        return recursive_binary_search(array, target, mid + 1, end)

def iteration_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

'''
이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
정렬되어 있는 데이터를 절반씩 좁혀가며 탐색하는 기법으로서, 시작점, 끝점, 중간점의 변수 3개를 사용한다.
찾으려는 데이터와 중간점의 데이터를 반복적으로 비교하여 원하는 결과를 얻어낼 수 있다.
이진 탐색의 시간복잡도는 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 O(lonN)으로 표현된다.
코딩 테스트에서 자주 출제되는 유형이니 숙지하고 있는것이 좋다.

트리 자료구조와 이진 탐색 트리에 대해 좀 더 알아볼 것
'''