'''
Dynamic Programming
컴퓨터의 연산 속도와 메모리 공간은 한계점이 있다.
따라서 연산속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘을 작성하여야 한다.
어떤 문제는 메모리 공간을 약간 더 사용하면 연산 속도를 비약적으로 증가시킬 수 있는데,
그 중 대표적인 방법을 Dynamic Programming (동적 계획법) 이라 한다.
Dynamic Programming 의 2가지 방식인 탑다운과 바텀업을 다뤄 볼 것이며, 자주 사용 되는 메모이제이션 기법까지 알아 볼 것이다.
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

def recursive_fibo(x):
    print(f'f({str(x)})', end=' ')
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = recursive_fibo(x - 1) + recursive_fibo(x - 2)
    return d[x]

print(recursive_fibo(99))