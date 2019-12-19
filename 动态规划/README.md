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

