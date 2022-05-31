import dfs_bfs_ex
import sorting_ex.coding_test_sorting as sorting_example
import sorting_ex.sorting_solution as sorting_solution
import searching_ex.coding_test_searching as searching_example
import searching_ex.searching_solution as searching_solution
# import dynamic_ex.coding_test_dynamic as dynamic_example
import time

start_time_log = time.time()

# 정렬 관련 연습
# sorting_example.for_test()

# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# sorting_example.quick_sort(array, 0, len(array)-1)
# print(array)

# sorting_solution.two_arrays()


# 탐색 관련 연습
# print(searching_example.sequetial_search(5, 'babymon', ['uni', 'test1', 'test2', 'babymon']))
# result1 = searching_example.recursive_binary_search([1, 3, 5, 6, 7, 8, 9, 10], 5, 0, 8-1)
#
# print(result1 + 1)

# result2 = searching_example.iteration_binary_search([1, 3, 5, 6, 7, 8, 9, 10], 5, 0, 8-1)

# print(result2 + 1)

# n = int(input())
# a_list = list()
#
# a_list = list(map(int, input().split()))
# m = int(input())
#
# b_list = list(map(int, input().split()))
#
# for i in b_list:
#     result = searching_solution.item_search(a_list, i, 0, n-1)
#
#     if result is None:
#         print('no')
#     else:
#         print('yes')

# searching_solution.cake_cutting()

# 다이나믹 프로그래밍 연습

# print(dynamic_example.recursive_fibo(99, d))
import dynamic_ex.coding_test_dynamic as dynamic_example

logic_flag = dynamic_example.answer_logic()
if logic_flag is True:
    print('good')
else:
    print('bad')

end_time_log = time.time()
print(f'수행 시간 : {end_time_log - start_time_log}')

