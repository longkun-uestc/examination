class Expression:
    def countWays(self, exp, len, ret):
        if len == 0:
            return 0
        var = []
        op = []
        for i in range(len):
            if i % 2 == 0:
                var.append(exp[i])
            else:
                op.append(exp[i])
        var_len = len // 2 + 1
        B = [[0 for i in range(var_len)] for j in range(var_len)]
        A = [[0 for i in range(var_len)] for j in range(var_len)]
        C = [B, A]
        for i in range(var_len):
            if var[i] == "0":
                C[0][i][i] = 1
            elif var[i] == "1":
                C[1][i][i] = 1
        for r in range(2, var_len+1):
            for i in range(var_len - r + 1):
                j = i + r - 1
                min_count_0 = 0
                min_count_1 = 0
                for k in range(i, j):
                    if op[k] == "&":
                        count_0 = C[0][i][k] * C[1][k+1][j] + C[1][i][k] * C[0][k+1][j] + C[0][i][k] * C[0][k+1][j]  # 0&1, 1&0, 0&0 = 0
                        count_1 = C[1][i][k] * C[1][k+1][j]  # 1&1 = 1
                    elif op[k] == "|":
                        count_0 = C[0][i][k] * C[0][k+1][j]  # 0|0 = 0
                        count_1 = C[1][i][k] * C[0][k+1][j] + C[0][i][k] * C[1][k+1][j] + C[1][i][k] * C[1][k+1][j]  # 1|0, 0|1, 1|1 = 1
                    else:
                        count_0 = C[0][i][k] * C[0][k+1][j] + C[1][i][k] * C[1][k+1][j]  # 0^0, 1^1 = 0
                        count_1 = C[0][i][k] * C[1][k+1][j] + C[1][i][k] * C[0][k+1][j]  # 0^1, 1^0 = 1
                    min_count_0 += count_0
                    min_count_1 += count_1
                C[0][i][j] = min_count_0
                C[1][i][j] = min_count_1
        # print("0---------")
        # for n in range(var_len):
        #     print(C[0][n])
        # print("1---------")
        # for n in range(var_len):
        #     print(C[1][n])
        # print(C[ret][0][var_len-1])
        return C[ret][0][var_len-1] % 10007


if __name__ == '__main__':
    x = "1^0|0|1"
    s = Expression()
    s.countWays(x, len(x), 0)
