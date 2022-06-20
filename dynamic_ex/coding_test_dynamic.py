'''
Dynamic Programming
컴퓨터의 연산 속도와 메모리 공간은 한계점이 있다.
따라서 연산속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘을 작성하여야 한다.
어떤 문제는 메모리 공간을 약간 더 사용하면 연산 속도를 비약적으로 증가시킬 수 있는데,
그 중 대표적인 방법을 Dynamic Programming (동적 계획법) 이라 한다.
Dynamic Programming 의 2가지 방식인 Top-Down과 Bottom-Up을 다뤄 볼 것이며, 자주 사용 되는 메모이제이션 기법까지 알아 볼 것이다.
'''

def fibo(x): # 피보나치 함수 예시
    if x == 1 or x ==2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
'''
위와 같은 풀이는 n의 크기가 커질수록 수행 시간이 기하급수적으로 늘어난다.
f(6) 일 때, fibo(3) 이 총 세번 호출되는데 이 처럼 이미 계산한 결과를 메모이제이션 (= 캐싱) 하면 효율적으로 계산할 수 있다.
따라서 다음과 같은 두 조건이 필요하다
1. 큰 문제를 작은 문제로 나눌 수 있음.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일
'''
d = [0] * 100

def memoization_fibo(x): # 메모이제이션을 활용한 피보나치 수열 구현
    print(f'f({str(x)})', end=' ')
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = memoization_fibo(x - 1) + memoization_fibo(x - 2)
    return d[x]

# print(memoization_fibo(99))

'''
다이나믹 프로그래밍을 적용했을 때의 피보나치 수열 알고리즘의 시간 복잡도는 O(N)이 된다.
f(1)을 구한 다음 그 값이 f(2)를 구하는데 사용되고, 또 그값이 f(3)을 구하는데 사용되는 방식으로 이어지기 때문이다.
한 번 구한 결과는 다시 구해지지 않는다.
출력문과 함께 현재의 피보나치 수의 출력값을 확인하면 알 수 있다.
이처럼 재귀 함수를 이용하여 작성하는 다이나믹 프로그래밍 소스코드를, 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 Top-Down 방식이라고 한다.
반면, 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을 도출한다고 하여 Bottom-Up 방식이라고 한다.
'''

def loop_type_fibo():
    d[1] = 1
    d[2] = 1

    n = 99

    for i in range(3, n + 1):
        d[i] = d[i-1] + d[i-2]

    print(d[n])


'''
탑다운(메모이제이션) 방식은 하향식이라고도 하며, 보텀업(반복문 구현) 방식은 상향식이라고도 한다.
다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다.
보텀업 방식에서 사용되는 결과 저장용 리스트를 'DP테이블' 이라고 부른다.
'''