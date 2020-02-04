# 力扣网刷题记录

# 扰乱字符串

题目详细描述见[这里](https://leetcode-cn.com/problems/scramble-string/)

# 解题思路

## 1.递归解法

与二叉树相关，可以从递归的思路入手。
如果s2是s1的扰乱字符串，那么它们必须满足如下条件：

1. s1和s2排序后必须相等
2. s2的左边部分必须是s1左边部分的扰乱字符串，同时s2的右边部分必须是s1右边部分的扰乱字符串
3. s2的左边部分必须是s1右边部分的扰乱字符串，同时s2的右边部分必须是s1左边部分的扰乱字符串

以上3个条件中，1必须满足，2和3有一个满足。至于如何界定左边和右边，需要遍历。因此思路便很清晰了。具体代码如下：
```python
def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 and len(s2) == 0:
            return True
        if len(s1) == 1 and len(s2) == 1 and s1 == s2:
            return True
        a = sorted(s1)
        b = sorted(s2)
        if a == b:
            for i in range(1, len(s1)):
                res1 = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
                res2 = self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])
                flag = res1 or res2
                if flag:
                    return flag
            return False
        else:
            return False
```

## 2.动态规划

在上面的递归解法中，for循环部分重复求解了很多相同的子问题。因此可以考虑使用动态规划来求解。
设dp[k][i][j]表示s1中从下标i开始长度为k的子串与s2中下标j开始长度为k的子串互为扰乱字符串的情况。
那么递推公式如下：

<a href="https://www.codecogs.com/eqnedit.php?latex=dp[k][i][j]=\left\{\begin{matrix}&space;True&space;&,&space;k=1&space;\quad&space;and&space;\quad&space;s1[i]=s2[j]\\&space;False&space;&,&space;k=1&space;\quad&space;and&space;\quad&space;s1[i]!=s2[j]\\&space;(dp[h][i][j]\&dp[k-h][i&plus;h][j&plus;h])&space;||(dp[h][i][j&plus;k-h]\&dp[k-h][i&plus;h][j])&space;\quad&space;for&space;\quad&space;h&space;\quad&space;in&space;\quad&space;range(1,k)&&space;,&space;k>2\\&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?dp[k][i][j]=\left\{\begin{matrix}&space;True&space;&,&space;k=1&space;\quad&space;and&space;\quad&space;s1[i]=s2[j]\\&space;False&space;&,&space;k=1&space;\quad&space;and&space;\quad&space;s1[i]!=s2[j]\\&space;(dp[h][i][j]\&dp[k-h][i&plus;h][j&plus;h])&space;||(dp[h][i][j&plus;k-h]\&dp[k-h][i&plus;h][j])&space;\quad&space;for&space;\quad&space;h&space;\quad&space;in&space;\quad&space;range(1,k)&&space;,&space;k>=2\\&space;\end{matrix}\right." title="dp[k][i][j]=\left\{\begin{matrix} True &, k=1 \quad and \quad s1[i]=s2[j]\\ False &, k=1 \quad and \quad s1[i]!=s2[j]\\ (dp[h][i][j]\&dp[k-h][i+h][j+h]) ||(dp[h][i][j+k-h]\&dp[k-h][i+h][j]) \quad for \quad h \quad in \quad range(1,k)& , k>2\\ \end{matrix}\right." /></a>

上述公式中，k=1为初始条件，如果长度为1的两个子串相等，那么他们互为扰乱字符串，结果为true，否则为false。

当k>=2时，两个子串要互为扰乱字符串就有两种可能（详见递归解法中的2,3点），至于在何处分界，需要遍历从1到k-1的长度，分别判断。如果在某个分界处结果为true，那么两个子串就互为扰乱字符串。如果所有分界处都为false，那么它们就不互为扰乱字符串。

具体代码如下：
```python
def isScramble1(self, s1: str, s2: str) -> bool:
    if len(s1) == 0 and len(s2) == 0:
        return True
    dp = [[[False for i in range(len(s1))] for j in range(len(s1))] for k in range(len(s1) + 1)]
    for i in range(len(s1)):  # 初始条件，k=1
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[1][i][j] = True
    for k in range(2, len(s1) + 1):  # 长度从2到len(s1)
        for i in range(len(s1) - k + 1):  # 从第一个字符开始到最后剩k个字符的下标处
            for j in range(len(s2) - k + 1):
                res = False  # 先默认不存在满足条件的分界点
                for h in range(1, k):  # 遍历1到k-1的长度，判断是否存在一个分界点使它们满足条件
                    r1 = dp[h][i][j] and dp[k - h][i + h][j + h]
                    r2 = dp[h][i][j + k - h] and dp[k - h][i + h][j]
                    if r1 or r2:  # 如果存在满足条件的分界点，结果为True，终止循环
                        res = True
                        break
                dp[k][i][j] = res
    return dp[len(s1)][0][0]  # 返回从下标为0开始长度为len(s1)的子串是否为扰乱字符串的结果
```

# 交错字符串

题目描述见[这里](https://leetcode-cn.com/problems/interleaving-string/submissions/)

# 解题思路

如果s3由s1和s2交错组成，那么首先必须满足，len(s1)+len(s2)=len(s3)。其次，s3的最后一个字符要么等于s1的最后一个字符，要么等于s2的最后一个字符，或者都相等。同时问题转化成判断s3[:-1], s1[:-1], s2 或者s3[:-1], s1, s2[:-1]是否为交错字符串的规模更小的子问题。因此：可以归纳出该问题的最优子结构：

设dp[k][i][j]表示长度为k的s3字符串是否由长度为i和j的s1和s2交错组成的情况。那么：

<a href="https://www.codecogs.com/eqnedit.php?latex=dp[k][i][j]=\left\{\begin{matrix}&space;false&space;&,&space;i&plus;j&space;\neq&space;k&space;\\&space;true&space;&,&space;i=j=k=0\\&space;dp[k-1][i-1][0]&space;&&space;,i=k,j=0,s1[i]=s3[k]&space;\\&space;dp[k-1][0][j-1]&space;&&space;,j=k,i=0,s2[j]=s3[k]&space;\\&space;dp[k-1][i-1][j]&space;&&space;,i&plus;j=k,s1[i]=s3[k],&space;s2[j]&space;\neq&space;s3[k]\\&space;dp[k-1][i][j-1]&space;&&space;,i&plus;j=k,s1[i]\neq&space;s3[k],s2[i]&space;=&space;s3[k]\\&space;dp[k-1][i-1][j]&space;\quad&space;or&space;\quad&space;dp[k-1][i][j-1]&space;&&space;,&space;i&plus;j=k,s1[i]=s3[k],&space;s2[j]=s3[k]&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?dp[k][i][j]=\left\{\begin{matrix}&space;false&space;&,&space;i&plus;j&space;\neq&space;k&space;\\&space;true&space;&,&space;i=j=k=0\\&space;dp[k-1][i-1][0]&space;&&space;,i=k,j=0,s1[i]=s3[k]&space;\\&space;dp[k-1][0][j-1]&space;&&space;,j=k,i=0,s2[j]=s3[k]&space;\\&space;dp[k-1][i-1][j]&space;&&space;,i&plus;j=k,s1[i]=s3[k],&space;s2[j]&space;\neq&space;s3[k]\\&space;dp[k-1][i][j-1]&space;&&space;,i&plus;j=k,s1[i]\neq&space;s3[k],s2[i]&space;=&space;s3[k]\\&space;dp[k-1][i-1][j]&space;\quad&space;or&space;\quad&space;dp[k-1][i][j-1]&space;&&space;,&space;i&plus;j=k,s1[i]=s3[k],&space;s2[j]=s3[k]&space;\end{matrix}\right." title="dp[k][i][j]=\left\{\begin{matrix} false &, i+j \neq k \\ true &, i=j=k=0\\ dp[k-1][i-1][0] & ,i=k,j=0,s1[i]=s3[k] \\ dp[k-1][0][j-1] & ,j=k,i=0,s2[j]=s3[k] \\ dp[k-1][i-1][j] & ,i+j=k,s1[i]=s3[k], s2[j] \neq s3[k]\\ dp[k-1][i][j-1] & ,i+j=k,s1[i]\neq s3[k],s2[i] = s3[k]\\ dp[k-1][i-1][j] \quad or \quad dp[k-1][i][j-1] & , i+j=k,s1[i]=s3[k], s2[j]=s3[k] \end{matrix}\right." /></a>

代码如下：
```python
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
        return True
    dp = [[[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] for k in range(len(s3) + 1)]
    dp[0][0][0] = True
    for i in range(1, len(s1) + 1):
        if s1[i - 1] == s3[i - 1]:
            dp[i][i][0] = dp[i - 1][i - 1][0]
    for j in range(1, len(s2) + 1):
        if s2[j - 1] == s3[j - 1]:
            dp[j][0][j] = dp[j - 1][0][j - 1]

    for k in range(2, len(s3) + 1):
        for i in range(1, min(len(s1) + 1, k)):
            j = k - i
            if j <= len(s2):
                if s1[i - 1] == s3[k - 1] and s2[j - 1] == s3[k - 1]:
                    dp[k][i][j] = dp[k - 1][i - 1][j] or dp[k - 1][i][j - 1]
                elif s1[i - 1] == s3[k - 1] and s2[j - 1] != s3[k - 1]:
                    dp[k][i][j] = dp[k - 1][i - 1][j]
                elif s1[i - 1] != s3[k - 1] and s2[j - 1] == s3[k - 1]:
                    dp[k][i][j] = dp[k - 1][i][j - 1]
                else:
                    dp[k][i][j] = False

    return dp[len(s3)][len(s1)][len(s2)]

```
