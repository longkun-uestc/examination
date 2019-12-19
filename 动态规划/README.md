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