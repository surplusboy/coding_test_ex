def item_search(array, target, start, end): # 타겟값 검색하기, 197
    array.sort()
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# # 계수 정렬로 풀기
# n = int(input())
# a_list = [0] * 1000001
#
# for i in input().split():
#     a_list[int(i)] = 1
#
# m = int(input())
# b_list = list(map(int, input().split()))
#
# for i in b_list:
#     if a_list[i] == 1:
#         print('yes')
#     else:
#         print('no')

# # 집합 자료형으로 풀기
# n = int(input())
# a_list = set(map(int, input().split()))
#
# print(a_list)
#
# m = int(input())
# b_list = list(map(int, input().split()))
#
# for i in b_list:
#     if i in a_list:
#         print('yes')
#     else:
#         print('no')

def cake_cutting(): # 떡 자르기, 201
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    end = max(array)

    start = 0

    result = 0

    while (start <= end):
        total = 0
        mid = (start + end) // 2 # 9

        for x in array: # [19, 15, 10, 17]
            if x > mid: # 19 > 9 ... 10 > 14 ? 
                total += x - mid # total += 10 ... 6 ... 1 ... 8
                print(x-mid)
        if total < m:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    print(result)