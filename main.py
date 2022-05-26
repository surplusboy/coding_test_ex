import dfs_bfs_ex
import sorting_ex.coding_test_sorting as sorting_example

# sorting_example.for_test()

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

sorting_example.quick_sort(array, 0, len(array)-1)
print(array)