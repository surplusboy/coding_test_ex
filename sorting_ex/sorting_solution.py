def up_to_down(): # 수열을 내림차순으로 정렬하는 코드, 178
    '''
    입력 조건 : 첫째 줄에 수열의 갯수 N 이 주어진다, 둘째 줄부터 N + 1 번째 줄까지 N개의 수가 입력된다.
    출력 조건 : 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다.
    '''

    n = int(input())

    array = list()
    for i in range(n):
        array.append(int(input()))


    array = sorted(array, reverse=True)

    for i in array:
        print(i, end= ' ')


    # 계수 정렬로 푼 예시

    # n = int(input())
    # array = list()
    #
    # for i in range(n):
    #     array.append(int(input()))
    #
    # chk_list = [0] * (max(array) + 1)
    #
    # for i in array:
    #     chk_list[i] += 1

    # filter_list = list(filter(lambda x: chk_list[x] == 1, range(len(chk_list))))
    # print(filter_list[::-1])


def student_socre(): # 성적 낮은 순서로 학생 출력

    n = int(input())

    array = list()

    for i in range(n):
        input_data = input().split()

        array.append((input_data[0], input_data[1]))

    array = sorted(array, key=lambda student: student[1])

    for i in array:
        print(i[0], end=' ')


def two_arrays():
    '''
    # 내가 그냥 풀었을 때
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a = [1, 2, 5, 4, 3]
    # b = [5, 5, 6, 6, 5]

    for i in range(k):

        min_int = a.index(min(a))
        max_int = b.index(max(b))

        a.pop(min_int)
        a.append(b[max_int])

        b.append(a[min_int])
        b.pop(max_int)

    print(sum(a))
    '''

    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    print(sum(a))