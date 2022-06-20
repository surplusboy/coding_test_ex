def make_it_one():  # 1로 만들기, 217
    x = int(input())
    # dp = [0] * 30001
    dp = [0] * 30
    for i in range(2, x + 1): # 2, 5
        dp[i] = dp[i-1] + 1
        # print(dp)
        # print(dp[i])
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5] + 1)
    print(dp)
    print(dp[x])


make_it_one()

# print(3//2)