# 动态规划专题
# 最长递增子序列
对于一个数字序列，请设计一个复杂度为O(nlogn)的算法，返回该序列的最长上升子序列的长度，这里的子序列定义为这样一个序列U1，U2...，其中Ui < Ui+1，且A[Ui] < A[Ui+1]。

给定一个数字序列A及序列的长度n，请返回最长上升子序列的长度。

测试样例：
~~~~
[2,1,4,3,1,5,6],7
~~~~
~~~
返回：4
~~~
## 最优子结构：
令<a href="https://www.codecogs.com/eqnedit.php?latex=F[i]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F[i]" title="F[i]" /></a>
表示以<a href="https://www.codecogs.com/eqnedit.php?latex=A[i]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?A[i]" title="A[i]" /></a>
结尾的最长递增子序列的长度。那么：

<a href="https://www.codecogs.com/eqnedit.php?latex=F[i]=\left\{\begin{matrix}&space;max(F[j]&space;&plus;&space;1)&space;&&space;j<i,&space;A[j]<A[i]&space;\\&space;1&space;&&space;A[i]<min(A[0],...,A[i-1])&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?F[i]=\left\{\begin{matrix}&space;max(F[j]&space;&plus;&space;1)&space;&&space;j<i,&space;A[j]<A[i]&space;\\&space;1&space;&&space;A[i]<min(A[0],...,A[i-1])&space;\end{matrix}\right." title="F[i]=\left\{\begin{matrix} max(F[j] + 1) & j<i, A[j]<A[i] \\ 1 & A[i]<min(A[0],...,A[i-1]) \end{matrix}\right." /></a>

这种算法的复杂度是<a href="https://www.codecogs.com/eqnedit.php?latex=O(n^{2})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(n^{2})" title="O(n^{2})" /></a>。
代码如下
```python
class AscentSequence:
    def findLongest(self, A, n):
        if len(A) == 0:
            return 0
        dp = [1] * n
        for i in range(1, len(A)):
            max_dp = 0
            for j in range(0, i):
                if A[j] < A[i] and dp[j] > max_dp:
                    max_dp = dp[j]
            dp[i] = max_dp + 1
        print(dp)
        return max(dp)
```

改进方法：上述方法中，要在0~i-1的数组中寻找在A[j]<A[i]的情况下最大的F[j]。这里需要O(n)的复杂度。
改进的思路是用一个辅助数组end来存储已经遍历到的递增子序列。

当A[i]大于end[-1]时，将A[i]直接添加到end末尾，并且dp[i]=len(end)

当A[i]小于等于end[-1]时，用A[i]替换end中第一个不小于A[i]的元素(假设为end[j])，并且dp[i]=j+1。

由于end是一个有序的数组，所以找end中第一个不小于A[i]的元素可以用二分查找，因此复杂度降为O(logn)
整体复杂度降为<a href="https://www.codecogs.com/eqnedit.php?latex=O(nlogn)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?O(nlogn)" title="O(nlogn)" /></a>

```python
def findLongest1(self, A, n):
    if len(A) == 0:
        return 0
    ends = [A[0]]
    dp = [1] * n
    for i in range(1, n):
        l, r = (0, len(ends) - 1)
        while l <= r:
            mid = (l + r) // 2
            if A[i] < ends[mid]:
                r = mid - 1
            elif A[i] == ends[mid]:
                l = mid
                break
            else:
                l = mid + 1
        if l < len(ends):
            ends[l] = A[i]
        else:
            ends.append(A[i])
        dp[i] = l + 1
    return max(dp)
```

#最长公共子序列
对于两个字符串，请设计一个高效算法，求他们的最长公共子序列的长度，
这里的最长公共子序列定义为有两个序列U1,U2,U3...Un和V1,V2,V3...Vn,
其中Ui<Ui+1，Vi<Vi+1。且A[Ui] == B[Vi]。

给定两个字符串A和B，同时给定两个串的长度n和m，请返回最长公共子序列的长度。保证两串长度均小于等于300。
测试样例：
~~~
"1A2C3D4B56",10,"B1D23CA45B6A",12
~~~
~~~
返回：6
~~~
## 最优子结构
令C[i，j]表示长度为i和j的字符串的最长公共子序列。那么：

<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]=\left\{\begin{matrix}&space;C[i-1][j-1]&plus;1&space;&&space;A[i]=B[j]\\&space;max(C[i-1][j],C[i][j-1],C[i-1][j-1])&space;&&space;A[i]!=B[j]\\&space;0&space;&&space;i=0&space;or&space;j=0&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]=\left\{\begin{matrix}&space;C[i-1][j-1]&plus;1&space;&&space;A[i]=B[j]\\&space;max(C[i-1][j],C[i][j-1],C[i-1][j-1])&space;&&space;A[i]!=B[j]\\&space;0&space;&&space;i=0&space;or&space;j=0&space;\end{matrix}\right." title="C[i,j]=\left\{\begin{matrix} C[i-1][j-1]+1 & A[i]=B[j]\\ max(C[i-1][j],C[i][j-1],C[i-1][j-1]) & A[i]!=B[j]\\ 0 & i=0 or j=0 \end{matrix}\right." /></a>

代码如下：
```python
class LCS:
    def findLCS(self, A, n, B, m):
        C = [[0 for i in range(m+1)] for j in range(n+1)]
        i, j = (n - 1, m - 1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # print(i, j)
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                else:
                    C[i][j] = max(C[i - 1][j], C[i][j - 1], C[i - 1][j - 1])
        return C[n][m]
```
#最长公共子串
对于两个字符串，请设计一个时间复杂度为O(m*n)的算法(这里的m和n为两串的长度)，求出两串的最长公共子串的长度。这里的最长公共子串的定义为两个序列U1,U2,..Un和V1,V2,...Vn，其中Ui + 1 == Ui+1,Vi + 1 == Vi+1，同时Ui == Vi。

给定两个字符串A和B，同时给定两串的长度n和m。

测试样例：
~~~
"1AB2345CD",9,"12345EF",7
~~~
~~~
返回：4
~~~
## 最优子结构
这个题与上题的不同之处在于，本题要求的字符串是连续的，条件更严格。因此：
设C[i,j]为分别以A[i],B[j]结尾的字符串的最长公共子串的长度，那么：
<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]=\left\{\begin{matrix}&space;C[i-1][j-1]&plus;1&space;&&space;A[i]=B[j]\\&space;0&space;&&space;A[i]!=B[j]\\&space;0&space;&&space;i=0&space;or&space;j=0&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]=\left\{\begin{matrix}&space;C[i-1][j-1]&plus;1&space;&&space;A[i]=B[j]\\&space;0&space;&&space;A[i]!=B[j]\\&space;0&space;&&space;i=0&space;or&space;j=0&space;\end{matrix}\right." title="C[i,j]=\left\{\begin{matrix} C[i-1][j-1]+1 & A[i]=B[j]\\ 0 & A[i]!=B[j]\\ 0 & i=0 or j=0 \end{matrix}\right." /></a>

代码如下：
```python
class LongestSubstring:
    def findLongest(self, A, n, B, m):
        C = [[0 for i in range(m + 1)] for j in range(n + 1)]
        max_len = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                else:
                    C[i][j] = 0  
                if C[i][j] > max_len:
                    max_len = C[i][j]
        # print(max_len)
        return max_len
```
# 最小编辑代价
对于两个字符串A和B，我们需要进行插入、删除和修改操作将A串变为B串，定义c0，c1，c2分别为三种操作的代价，请设计一个高效算法，求出将A串变为B串所需要的最少代价。

给定两个字符串A和B，及它们的长度和三种操作代价，请返回将A串变为B串所需要的最小代价。保证两串长度均小于等于300，且三种代价值均小于等于100。

测试样例：
~~~
"abc",3,"adc",3,5,3,100
~~~
~~~
返回：8
~~~
## 最优子结构
设C[i,j]为将长度为i的字符串A编辑为长度为j的字符串B的代价。
那么：

<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]=\left\{\begin{matrix}&space;C[i-1][j-1]&space;&&space;A[i]=B[j]\\&space;min(C[i][j-1]&plus;c_{insert},&space;C[i-1][j]&plus;c_{delet},&space;C[i-1][j-1]&plus;c_{change})&space;&A[i]!=B[j]&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]=\left\{\begin{matrix}&space;C[i-1][j-1]&space;&&space;A[i]=B[j]\\&space;min(C[i][j-1]&plus;c_{insert},&space;C[i-1][j]&plus;c_{delet},&space;C[i-1][j-1]&plus;c_{change})&space;&A[i]!=B[j]&space;\end{matrix}\right." title="C[i,j]=\left\{\begin{matrix} C[i-1][j-1] & A[i]=B[j]\\ min(C[i][j-1]+c_{insert}, C[i-1][j]+c_{delet}, C[i-1][j-1]+c_{change}) &A[i]!=B[j] \end{matrix}\right." /></a>

代码如下：
```python
class MinCost:
    def findMinCost(self, A, n, B, m, c0, c1, c2):
        C = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(0, n + 1):
            C[i][0] = i * c1
        for j in range(0, m + 1):
            C[0][j] = j * c0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1]
                else:
                    C[i][j] = min(C[i][j - 1] + c0, C[i - 1][j] + c1, C[i - 1][j - 1] + c2)
        # for c in C:
        #     print(c)
        # print(C[n][m])
        return C[n][m]
```

# 字符串交错组成
对于三个字符串A，B，C。我们称C由A和B交错组成当且仅当C包含且仅包含A，B中所有字符，且对应的顺序不改变。请编写一个高效算法，判断C串是否由A和B交错组成。

给定三个字符串A,B和C，及他们的长度。请返回一个bool值，代表C是否由A和B交错组成。保证三个串的长度均小于等于100。

测试样例：
~~~
"ABC",3,"12C",3,"A12BCC",6
~~~
~~~
返回：true
~~~
##最优子结构
设M[i,j]表示由A[1-i]和B[1-j]是否能组成C[i+j]的判别结果。
那么：
<a href="https://www.codecogs.com/eqnedit.php?latex=M[i,j]=\left\{\begin{matrix}&space;M[i-1][j]&space;or&space;M[i][j-1]&space;&&space;C[i&plus;j]=A[i]=B[j]\\&space;False&space;&&space;C[i&plus;j]!=A[i]=B[j]\\&space;M[i-1][j]&space;&&space;C[i&plus;j]=A[i]!=B[j]\\&space;M[i][j-1]&space;&&space;C[i&plus;j]=B[j]&space;!=A[i]\\&space;False&space;&&space;C[i&plus;j]&space;!=A[i]!=B[j]&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?M[i,j]=\left\{\begin{matrix}&space;M[i-1][j]&space;or&space;M[i][j-1]&space;&&space;C[i&plus;j]=A[i]=B[j]\\&space;False&space;&&space;C[i&plus;j]!=A[i]=B[j]\\&space;M[i-1][j]&space;&&space;C[i&plus;j]=A[i]!=B[j]\\&space;M[i][j-1]&space;&&space;C[i&plus;j]=B[j]&space;!=A[i]\\&space;False&space;&&space;C[i&plus;j]&space;!=A[i]!=B[j]&space;\end{matrix}\right." title="M[i,j]=\left\{\begin{matrix} M[i-1][j] or M[i][j-1] & C[i+j]=A[i]=B[j]\\ False & C[i+j]!=A[i]=B[j]\\ M[i-1][j] & C[i+j]=A[i]!=B[j]\\ M[i][j-1] & C[i+j]=B[j] !=A[i]\\ False & C[i+j] !=A[i]!=B[j] \end{matrix}\right." /></a>

代码如下：
```python
class Mixture:
    def chkMixture(self, A, n, B, m, C, v):
        if n == 0 and m == 0 and v == 0:
            return True
        if n == 0 and B != C:
            return False
        if m == 0 and A != C:
            return False
        if n == 0 and m == 0 and v != 0:
            return False
        if v != n + m:
            return False
        M = [[False for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            if A[i-1] == C[i-1]:
                M[i][0] = True
        for j in range(1, m + 1):
            if B[j-1] == C[j-1]:
                M[0][j] = True
        M[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    if C[i + j - 1] == A[i - 1]:
                        M[i][j] = M[i][j - 1] or M[i - 1][j]
                    else:
                        M[i][j] = False
                else:
                    if C[i + j - 1] == A[i - 1]:
                        M[i][j] = M[i - 1][j]
                    elif C[i + j - 1] == B[j - 1]:
                        M[i][j] = M[i][j - 1]
                    else:
                        M[i][j] = False
        for a in M:
            print(a)
        print(M[n][m])
        return M[n][m]
```

# 矩阵连乘
给定n个矩阵｛A1, A2, …, An｝，Ai的维数为pi-1×pi，Ai与Ai+1是可乘的，i=1,2 ,…,n-1。如何确定计算矩阵连乘积的计算次序，使得依此次序计算矩阵连乘积需要的数乘次数最少

## 最优子结构
设M[i,j]表示从Ai到Aj做乘法需要的最小步数。那么原问题相当于求解M[1, n]

<a href="https://www.codecogs.com/eqnedit.php?latex=M[i,j]&space;=&space;\left\{\begin{matrix}&space;0&space;&i=j&space;\\&space;min_{i\leqslant&space;k<j}(M[i,k]&plus;M[k&plus;1,j]&plus;P[i,0]*P[k,1]*P[j,&space;1])&space;&&space;i!=j&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?M[i,j]&space;=&space;\left\{\begin{matrix}&space;0&space;&i=j&space;\\&space;min_{i\leqslant&space;k<j}(M[i,k]&plus;M[k&plus;1,j]&plus;P[i,0]*P[k,1]*P[j,&space;1])&space;&&space;i!=j&space;\end{matrix}\right." title="M[i,j] = \left\{\begin{matrix} 0 &i=j \\ min_{i\leqslant k<j}(M[i,k]+M[k+1,j]+P[i,0]*P[k,1]*P[j, 1]) & i!=j \end{matrix}\right." /></a>

代码如下：
```python
class Solution:
    def matrix_multiply(self, matrix_list):
        if len(matrix_list) == 0:
            return 0
        n = len(matrix_list)
        M = [[0 for i in range(n)] for j in range(n)]
        for r in range(2, n+1):
            for i in range(n - r + 1):
                left = matrix_list[i]
                j = i+r-1
                right = matrix_list[j]
                M[i][j] = min([M[i][k] + M[k + 1][j] + left[0] * matrix_list[k][1] * right[1] for k in range(i, j)])
        for m in M:
            print(m)
        return M[0][n-1]
```
# 表达式组成方案
对于一个只由0(假)、1(真)、&(逻辑与)、|(逻辑或)和^(异或)五种字符组成的逻辑表达式，再给定一个结果值。现在可以对这个没有括号的表达式任意加合法的括号，返回得到能有多少种加括号的方式，可以达到这个结果。

给定一个字符串表达式exp及它的长度len，同时给定结果值ret,请返回方案数。保证表达式长度小于等于300。为了防止溢出，请返回答案Mod 10007的值。

测试样例：
~~~
"1^0|0|1",7,0
~~~
~~~
返回：2
~~~
## 最优子结构
这道题和上面的矩阵连乘类似。使用区间动态规划的方法。
由于这里存在两种情况(ret=0, 或ret=1)，因此需要使用两个数组来记录中间过程，并且这两个数组互相会受对方的影响。

令B[i,j]表示从第i个bool变量到第j个bool变量的子串用加括号的方式使结果为1的方法数

令C[i,j]表示从第i个bool变量到第j个bool变量的子串用加括号的方式使结果为0的方法数

那么最终输出的结果为：
```python
result = B[0][n] if ret == 1 else C[0][n]
```
以B[i,j]为例进行分析：要计算子串exp[i,j]加括号使之为1的方法数，可以将其分为两个部分[i,k]和[k+1, j]
然后看这两部分用什么符号连接的，然后再根据符号计算每个部分为0或者为1的方法数。

令数组A为字符串exp中提取出来的bool变量，数组op为字符串中提取出的操作符。那么len(A)+len(op)=len(exp)并且len(A)=len(op)+1

那么B[i,j]和C[i,j]的递推表达式为：

<a href="https://www.codecogs.com/eqnedit.php?latex=B[i,j]=\left\{\begin{matrix}&space;0&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=0&space;\\&space;1&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=1&space;\\&space;\sum&space;count1_{k}&space;&&space;for&space;\quad&space;k&space;\quad&space;in&space;\quad&space;range(i,j)&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?B[i,j]=\left\{\begin{matrix}&space;0&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=0&space;\\&space;1&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=1&space;\\&space;\sum&space;count1_{k}&space;&&space;for&space;\quad&space;k&space;\quad&space;in&space;\quad&space;range(i,j)&space;\end{matrix}\right." title="B[i,j]=\left\{\begin{matrix} 0 & ,if \quad i=j \quad and \quad A[i]=0 \\ 1 & ,if \quad i=j \quad and \quad A[i]=1 \\ \sum count1_{k} & for \quad k \quad in \quad range(i,j) \end{matrix}\right." /></a>

其中：

<a href="https://www.codecogs.com/eqnedit.php?latex=count1_{k}=\left\{\begin{matrix}&space;B[i,k]*B[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\&$\\&space;B[i,k]*C[k&plus;1,j]&plus;C[i,k]*B[k&plus;1,j]&plus;B[i,k]*B[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\|$\\&space;B[i,k]*C[k&plus;1,j]&plus;C[i,k]*B[k&plus;1,j]&&space;if\quad&space;op[k]==&space;\oplus&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?count1_{k}=\left\{\begin{matrix}&space;B[i,k]*B[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\&$\\&space;B[i,k]*C[k&plus;1,j]&plus;C[i,k]*B[k&plus;1,j]&plus;B[i,k]*B[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\|$\\&space;B[i,k]*C[k&plus;1,j]&plus;C[i,k]*B[k&plus;1,j]&&space;if\quad&space;op[k]==&space;\oplus&space;\end{matrix}\right." title="count1_{k}=\left\{\begin{matrix} B[i,k]*B[k+1,j] & if \quad op[k]==$\&$\\ B[i,k]*C[k+1,j]+C[i,k]*B[k+1,j]+B[i,k]*B[k+1,j] & if \quad op[k]==$\|$\\ B[i,k]*C[k+1,j]+C[i,k]*B[k+1,j]& if\quad op[k]== \oplus \end{matrix}\right." /></a>

C[i,j]的公式同理

<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]=\left\{\begin{matrix}&space;1&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=0&space;\\&space;0&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=1&space;\\&space;\sum&space;count0_{k}&space;&&space;for&space;\quad&space;k&space;\quad&space;in&space;\quad&space;range(i,j)&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]=\left\{\begin{matrix}&space;1&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=0&space;\\&space;0&space;&&space;,if&space;\quad&space;i=j&space;\quad&space;and&space;\quad&space;A[i]=1&space;\\&space;\sum&space;count0_{k}&space;&&space;for&space;\quad&space;k&space;\quad&space;in&space;\quad&space;range(i,j)&space;\end{matrix}\right." title="C[i,j]=\left\{\begin{matrix} 1 & ,if \quad i=j \quad and \quad A[i]=0 \\ 0 & ,if \quad i=j \quad and \quad A[i]=1 \\ \sum count0_{k} & for \quad k \quad in \quad range(i,j) \end{matrix}\right." /></a>

其中

<a href="https://www.codecogs.com/eqnedit.php?latex=count0_{k}=\left\{\begin{matrix}&space;C[i,k]*B[k&plus;1,j]&plus;B[i,k]*C[k&plus;1,j]&plus;C[i,k]*C[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\&$\\&space;C[i,k]*C[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\|$\\&space;B[i,k]*B[k&plus;1,j]&plus;C[i,k]*C[k&plus;1,j]&&space;if\quad&space;op[k]==&space;\oplus&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?count0_{k}=\left\{\begin{matrix}&space;C[i,k]*B[k&plus;1,j]&plus;B[i,k]*C[k&plus;1,j]&plus;C[i,k]*C[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\&$\\&space;C[i,k]*C[k&plus;1,j]&space;&&space;if&space;\quad&space;op[k]==$\|$\\&space;B[i,k]*B[k&plus;1,j]&plus;C[i,k]*C[k&plus;1,j]&&space;if\quad&space;op[k]==&space;\oplus&space;\end{matrix}\right." title="count0_{k}=\left\{\begin{matrix} C[i,k]*B[k+1,j]+B[i,k]*C[k+1,j]+C[i,k]*C[k+1,j] & if \quad op[k]==$\&$\\ C[i,k]*C[k+1,j] & if \quad op[k]==$\|$\\ B[i,k]*B[k+1,j]+C[i,k]*C[k+1,j]& if\quad op[k]== \oplus \end{matrix}\right." /></a>

写代码时，可以将B和C整合成一个三维数组。代码如下：
```python
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
```

#纸牌博弈

有一个整型数组A，代表数值不同的纸牌排成一条线。玩家a和玩家b依次拿走每张纸牌，规定玩家a先拿，玩家B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家a和玩家b都绝顶聪明，他们总会采用最优策略。请返回最后获胜者的分数。

给定纸牌序列A及序列的大小n，请返回最后分数较高者得分数(相同则返回任意一个分数)。保证A中的元素均小于等于1000。且A的大小小于等于300。

测试样例：
~~~
[1,2,100,4],4
~~~
~~~
返回：101
~~~
## 最优子结构
这个题中，A和B每次有两种选择(拿左边还是拿右边)。同样是区间动态规划的思想

设C[i,j]表示当前要拿牌的人从牌序列S[i~j]中拿了一张牌后，获得的最大值。

当前拿牌的人(假设为A)可以选择拿左边，也可以拿右边。如果他选择拿左边，那么另外一个人B就会从S[i+1~j]的序列中拿牌，
他也可以选择拿左边还是拿右边。再轮到A拿牌时，他就只能在长度为j-i-1的序列中拿牌了。他有4种可能：B选左边，他可以选左或右;B
选右边，他也可以选左或右。

所以C[i,j]的最大值有如下四种可能：

<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]=max(C[i&plus;2,j]&plus;c_{l},C[i&plus;1,j-1]&plus;c_{l},&space;C[i,&space;j-2]&plus;c_{r},&space;C[i&plus;1,&space;j-1]&plus;c_{r})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]=max(C[i&plus;2,j]&plus;c_{l},C[i&plus;1,j-1]&plus;c_{l},&space;C[i,&space;j-2]&plus;c_{r},&space;C[i&plus;1,&space;j-1]&plus;c_{r})" title="C[i,j]=max(C[i+2,j]+c_{l},C[i+1,j-1]+c_{l}, C[i, j-2]+c_{r}, C[i+1, j-1]+c_{r})" /></a>

但是问题的关键在于B只会选择让他最优的那种情况。因此C[i,j]可能的选择就从4种降到了2种。

那么如何知道B选择的是左边还是右边呢？可以另增一个记号数组来记录B选择的方向。

令F[i,j]表示当前从i~j子串中选择的人选择的方向。

递推表达式如下：

<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]&space;=&space;\left\{\begin{matrix}&space;S[i,i]&space;&&space;if&space;\quad&space;i=j&space;\\&space;max(S[i,i],&space;S[i,i&plus;1])&space;&&space;if&space;j=i&plus;1\\&space;max(left,&space;right)&space;&&space;if&space;j>&space;i&plus;1\\&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]&space;=&space;\left\{\begin{matrix}&space;S[i,i]&space;&&space;if&space;\quad&space;i=j&space;\\&space;max(S[i,i],&space;S[i,i&plus;1])&space;&&space;if&space;j=i&plus;1\\&space;max(left,&space;right)&space;&&space;if&space;j>&space;i&plus;1\\&space;\end{matrix}\right." title="C[i,j] = \left\{\begin{matrix} S[i,i] & if \quad i=j \\ max(S[i,i], S[i,i+1]) & if j=i+1\\ max(left, right) & if j> i+1\\ \end{matrix}\right." /></a>

其中：

<a href="https://www.codecogs.com/eqnedit.php?latex=left&space;=&space;S_{i}&plus;C[i&plus;2,j]\quad&space;if&space;\quad&space;F[i&plus;1,j]=L&space;\quad&space;else&space;\quad&space;S_{i}&plus;C[i&plus;1,j-1]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?left&space;=&space;S_{i}&plus;C[i&plus;2,j]\quad&space;if&space;\quad&space;F[i&plus;1,j]=L&space;\quad&space;else&space;\quad&space;S_{i}&plus;C[i&plus;1,j-1]" title="left = S_{i}+C[i+2,j]\quad if \quad F[i+1,j]=L \quad else \quad S_{i}+C[i+1,j-1]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=right&space;=&space;S_{j}&plus;C[i&plus;1,j-1]\quad&space;if&space;\quad&space;F[i,j-1]=L&space;\quad&space;else&space;\quad&space;S_{j}&plus;C[i,j-2]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?right&space;=&space;S_{j}&plus;C[i&plus;1,j-1]\quad&space;if&space;\quad&space;F[i,j-1]=L&space;\quad&space;else&space;\quad&space;S_{j}&plus;C[i,j-2]" title="right = S_{j}+C[i+1,j-1]\quad if \quad F[i,j-1]=L \quad else \quad S_{j}+C[i,j-2]" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=F[i,j]=\left\{\begin{matrix}&space;L&space;&&space;,if&space;\quad&space;i=j\\&space;L\quad&space;if&space;\quad&space;S[i]\geqslant&space;S[j]&space;\quad&space;else&space;\quad&space;R&space;&&space;,if&space;\quad&space;j=i&plus;1&space;\\&space;L&space;\quad&space;if&space;\quad&space;left&space;\geqslant&space;right&space;\quad&space;else&space;\quad&space;R&space;&&space;,otherwise&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?F[i,j]=\left\{\begin{matrix}&space;L&space;&&space;,if&space;\quad&space;i=j\\&space;L\quad&space;if&space;\quad&space;S[i]\geqslant&space;S[j]&space;\quad&space;else&space;\quad&space;R&space;&&space;,if&space;\quad&space;j=i&plus;1&space;\\&space;L&space;\quad&space;if&space;\quad&space;left&space;\geqslant&space;right&space;\quad&space;else&space;\quad&space;R&space;&&space;,otherwise&space;\end{matrix}\right." title="F[i,j]=\left\{\begin{matrix} L & ,if \quad i=j\\ L\quad if \quad S[i]\geqslant S[j] \quad else \quad R & ,if \quad j=i+1 \\ L \quad if \quad left \geqslant right \quad else \quad R & ,otherwise \end{matrix}\right." /></a>

代码如下：
```python
class Cards:
    def cardGame(self, A, n):
        if n <= 0:
            return 0
        M = [[0 for i in range(n)] for j in range(n)]
        F = [["0" for i in range(n)] for j in range(n)]
        for i in range(n):
            M[i][i] = A[i]
            F[i][i] = "L"
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                M[i][i + 1] = A[i]
                F[i][i + 1] = "L"
            else:
                M[i][i + 1] = A[i + 1]
                F[i][i + 1] = "R"
        for r in range(3, n + 1):
            for i in range(n - r + 1):
                j = i + r - 1
                if F[i + 1][j] == "L":
                    left = A[i] + M[i + 2][j]
                else:
                    left = A[i] + M[i + 1][j - 1]
                if F[i][j - 1] == "L":
                    right = A[j] + M[i + 1][j - 1]
                else:
                    right = A[j] + M[i][j - 2]

                if left >= right:
                    M[i][j] = left
                    F[i][j] = "L"
                else:
                    M[i][j] = right
                    F[i][j] = "R"
        # print("-----------------------")
        # for m in M:
        #     print(m)
        # for f in F:
        #     print(f)
        a = M[0][n - 1]
        b = sum(A) - a
        result = a if a > b else b
        print(result)
        return result
```

# 字符串通配
对于字符串A，其中绝对不含有字符’.’和’*’。再给定字符串B，其中可以含有’.’或’*’，’*’字符不能是B的首字符，并且任意两个’*’字符不相邻。exp中的’.’代表任何一个字符，B中的’*’表示’*’的前一个字符可以有0个或者多个。请写一个函数，判断A是否能被B匹配。

给定两个字符串A和B,同时给定两个串的长度lena和lenb，请返回一个bool值代表能否匹配。保证两串的长度均小于等于300。

测试样例：
~~~
"abcd",4,".*",2
~~~
~~~
返回：true
~~~

## 最优子结构

设C[i,j]表示是否能用字符串Bj匹配Ai的bool值。那么存在如下三种情况。

1.A[i]=B[j] or B[j]="."

2.A[i]!=B[j] and B[j]!="*"

3.B[j]="*"

对于情况1，C[i,j]=C[i-1,j-1]。对于情况2，C[i,j]=False。对于情况3，要考虑*到底代替了几个B[j-1]。它可以代替0个，1个或多个B[j-1]
。当代替0个时，C[i,j]=C[i,j-2]。当代替1个时，C[i,j]=C[i,j-1]。当代替多个时， 要考虑Ai是否等于B[j-1]，如果相等，C[i,j]=C[i-1,j],
如果不等，C[i,j]=False。

因此，递推表达式为：

当i>0并且j>0时：

<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]=\left\{\begin{matrix}&space;C[i-1,j-1]&space;&,&space;A_{i}=B_{j}&space;\quad&space;or&space;\quad&space;B_{j}="."&space;,i>0,&space;j>0\\&space;False&space;&,&space;A_{i}!=B_{j}&space;\quad&space;and&space;\quad&space;B_{j}!="*"&space;\\&space;\begin{Bmatrix}&space;C[i,j-2]&space;&,&space;"*"&space;\quad&space;repalce&space;\quad&space;0&space;\quad&space;B_{j-1}&space;\\&space;or&space;\quad&space;C[i,j-1]&space;&,&space;"*"&space;\quad&space;repalce&space;\quad&space;1&space;\quad&space;B_{j-1}\\&space;or&space;\quad&space;(C[i-1,&space;j]&space;\quad&space;if&space;A_{i-1}=B_{j-1}&space;\quad&space;or&space;\quad&space;B_{j-1}="."&space;\quad&space;else&space;\quad&space;False)&space;&,&space;"*"&space;\quad&space;repalce&space;\quad&space;multiple&space;\quad&space;B_{j-1}&space;\end{Bmatrix}&,&space;B_{j}="*"&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]=\left\{\begin{matrix}&space;C[i-1,j-1]&space;&,&space;A_{i}=B_{j}&space;\quad&space;or&space;\quad&space;B_{j}="."&space;,i>0,&space;j>0\\&space;False&space;&,&space;A_{i}!=B_{j}&space;\quad&space;and&space;\quad&space;B_{j}!="*"&space;\\&space;\begin{Bmatrix}&space;C[i,j-2]&space;&,&space;"*"&space;\quad&space;repalce&space;\quad&space;0&space;\quad&space;B_{j-1}&space;\\&space;or&space;\quad&space;C[i,j-1]&space;&,&space;"*"&space;\quad&space;repalce&space;\quad&space;1&space;\quad&space;B_{j-1}\\&space;or&space;\quad&space;(C[i-1,&space;j]&space;\quad&space;if&space;A_{i-1}=B_{j-1}&space;\quad&space;or&space;\quad&space;B_{j-1}="."&space;\quad&space;else&space;\quad&space;False)&space;&,&space;"*"&space;\quad&space;repalce&space;\quad&space;multiple&space;\quad&space;B_{j-1}&space;\end{Bmatrix}&,&space;B_{j}="*"&space;\end{matrix}\right." title="C[i,j]=\left\{\begin{matrix} C[i-1,j-1] &, A_{i}=B_{j} \quad or \quad B_{j}="." ,i>0, j>0\\ False &, A_{i}!=B_{j} \quad and \quad B_{j}!="*" \\ \begin{Bmatrix} C[i,j-2] &, "*" \quad repalce \quad 0 \quad B_{j-1} \\ or \quad C[i,j-1] &, "*" \quad repalce \quad 1 \quad B_{j-1}\\ or \quad (C[i-1, j] \quad if A_{i-1}=B_{j-1} \quad or \quad B_{j-1}="." \quad else \quad False) &, "*" \quad repalce \quad multiple \quad B_{j-1} \end{Bmatrix}&, B_{j}="*" \end{matrix}\right." /></a>

边界条件为：

<a href="https://www.codecogs.com/eqnedit.php?latex=C[i,j]=\left\{\begin{matrix}&space;True&space;&&space;,i=j=0\\&space;False&space;&&space;,j=0&space;\quad&space;and&space;\quad&space;i!=0\\&space;False&space;&&space;,i=0&space;\quad&space;and&space;\quad&space;j=1&space;\\&space;C[i][j-2]&space;\quad&space;if&space;B_{j}="*"&space;\quad&space;else&space;\quad&space;False&space;&&space;,&space;i=0\quad&space;and&space;\quad&space;j>0&space;\\&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?C[i,j]=\left\{\begin{matrix}&space;True&space;&&space;,i=j=0\\&space;False&space;&&space;,j=0&space;\quad&space;and&space;\quad&space;i!=0\\&space;False&space;&&space;,i=0&space;\quad&space;and&space;\quad&space;j=1&space;\\&space;C[i][j-2]&space;\quad&space;if&space;B_{j}="*"&space;\quad&space;else&space;\quad&space;False&space;&&space;,&space;i=0\quad&space;and&space;\quad&space;j>0&space;\\&space;\end{matrix}\right." title="C[i,j]=\left\{\begin{matrix} True & ,i=j=0\\ False & ,j=0 \quad and \quad i!=0\\ False & ,i=0 \quad and \quad j=1 \\ C[i][j-2] \quad if B_{j}="*" \quad else \quad False & , i=0\quad and \quad j>0 \\ \end{matrix}\right." /></a>

代码如下：
```python
class WildMatch:
    def chkWildMatch(self, A, lena, B, lenb):
        if lenb == 0 and lena > 0:
            return False
        if lena == 0 and lenb == 0:
            return True
        C = [[False for j in range(lenb+1)] for i in range(lena+1)]
        C[0][0] = True
        C[0][1] = False
        for i in range(1, lena+1):
            C[i][0] = False
        for j in range(2, lenb+1):
            if B[j-1] == "*":
                C[0][j] = C[0][j-2]
            else:
                C[0][j] = False
        for c in C:
            print(c)
        for i in range(1, lena+1):
            for j in range(1, lenb+1):
                if A[i-1]==B[j-1] or B[j-1] == ".":
                    C[i][j] = C[i-1][j-1]
                elif A[i-1] != B[j-1] and B[j-1] != "*":
                    C[i][j] = False
                elif B[j-1] == "*":
                    a = C[i][j-2]  # 产生0个
                    b = C[i][j-1]  # 产生1个
                    c = C[i-1][j] if A[i-1] == B[j-2] or B[j-2] == "." else False  # 产生多个。如果A的当前字符和B的前一个字符不相等，直接为False, 否则B不变，A前移一个字符
                    C[i][j] = a or b or c  # 最终结果为3种情况选1
                else:
                    print("error")  # 永远不会进这个分支
                    exit()
        print("---------------------------------")
        for c in C:
            print(c)
        print(C[lena][lenb])
        return C[lena][lenb]
```










