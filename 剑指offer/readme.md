# 1.二维数组中的查找
## 题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
## 考点
二分查找，从角落开始
 ```python
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return False
        if target < array[0][0]:
            return False
        if target > array[-1][-1]:
            return False
        p1 = len(array)-1
        p2 = 0
        while ((p1 >= 0) and (p2 < len(array[0]))):
            if target < array[p1][p2]:
                p1 -= 1
            elif target > array[p1][p2]:
                p2 += 1
            elif target == array[p1][p2]:
                return True
        return False
```

# 2.重建二叉树
## 题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
## 考点
二叉树的前序，中序，后序遍历
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        node = TreeNode(pre[0])
        root_index_in_tin = tin.index(pre[0])
        left_tin = tin[0: root_index_in_tin]
        right_tin = tin[root_index_in_tin + 1:]
        left_pre = pre[1:len(left_tin) + 1]
        right_pre = pre[len(left_tin) + 1:]
        left_node = self.reConstructBinaryTree(left_pre, left_tin)
        right_node = self.reConstructBinaryTree(right_pre, right_tin)
        node.left = left_node
        node.right = right_node
        return node
```

# 3.两个栈实现队列
##题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
## 考点
栈，队列
```python
class Solution:
    l1 = []
    l2 = []
    def push(self, node):
        # write code here
        self.l1.append(node)
    def pop(self):
        if len(self.l1) == 0 and len(self.l2) == 0:
            return None
        if len(self.l2) == 0:
            while len(self.l1) != 0:
                self.l2.append(self.l1.pop())
        return self.l2.pop()
```

# 4.旋转数组最小数字
## 题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
## 考点
二分查找
```python
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        else:
            left = 0
            right = len(rotateArray) - 1
            while left < right:
                mid = (left + right) // 2
                if rotateArray[mid] < rotateArray[right]:
                    right = mid
                elif rotateArray[mid] > rotateArray[right]:
                    left = mid + 1
                else:
                    right -= 1
            return rotateArray[left]
```
# 5.青蛙跳台阶
## 题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
## 考点
递归
代码很简单

# 6.二进制中1的个数
## 题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
## 考点
原码，反码，补码
```python
class Solution:
    def NumberOf1(self, n):
        if n == 0:
            return 0
        if n > 0:
            count = 0
            while n > 0:
                y = n % 2
                if y == 1:
                    count += 1
                n = n // 2
            return count
        elif n < 0:
            binary = [0] * 32
            n = -n
            ids = 0
            while n > 0:
                y = n % 2
                binary[ids] = y
                ids += 1
                n = n // 2
            ids = binary.index(1)
            count = binary[ids + 1:].count(0)
            count += 1
            return count

def good_NumberOf1(self, n):
    # 优秀解法
    # 首先bin()函数可以将整数转换为2进制，例如bin(4)='0b100'， bin(-4) = '-0b100'
    # 对负数，bin(还是用原码表示输出的)。此时要想输出负数补码的1的个数，就要将补码转换为原码
    # 计算机表示有符号整数时，范围是[-2**32, 2**32-1]，用补码表示的
    # 将补码加上2**32就等价于把有符号数转换成了无符号数,考虑溢出，此时范围成了[0, 2*33-1]
    # 其次，负数的补码加上2**32就等价于将其转换成了原码，再直接数1就可以了。
    # 例如-3的补码表示为：1101。将其加上2**3，等于1101+1000=10101
    return bin(n).replace("0b", "").count("1") if n >= 0 else bin(2 ** 32 + n).replace("0b", "").count("1")
```

# 7.反转链表 (重点复习)
## 题目描述
输入一个链表，反转链表后，输出新链表的表头。
## 考点
链表反转规则
```python
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        next = None
        while pHead:  # 精华全在这里
            next = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = next
        return pre
```

# 8.树的子结构  (重点复习)
## 题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
## 考点
1.区分子树和子结构的区别。[这里](https://www.nowcoder.com/questionTerminal/6e196c44c7004d15b1610b9afca8bd88?answerType=1&f=discussion)有详细讲解。

2.注意递归的退出条件
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def cmp(t1, t2):
    pre_order(t1)
    print("------", end=" ")
    pre_order(t2)
    print("\n")
    if t2 is None:
        return True
    if t1 is None:
        return False
    if t1.val != t2.val:
        # return cmp(t1.left, t2) or cmp(t1.right, t2)  # 第一类写法
        return False   # 第二类写法
    return cmp(t1.left, t2.left) and cmp(t1.right, t2.right)

# https://www.nowcoder.com/questionTerminal/6e196c44c7004d15b1610b9afca8bd88?answerType=1&f=discussion
# 子结构与子树不同，子结构没有子树那么严格
# 注意是子结构的成立条件
# 第一类写法是有问题的，以为可能出现t1,t2根节点相同，但是仅在t1的子树中存在t2的子树节点，这时候这也会被判断为true
# 例如 t1 = pre_order[8,8,9,2,4,7,7] in_order[9,8,4,2,7,8,7] t2 = pre[8,9,7] in[9,8,7]
# 这时候其实t2不是t1的子结构，但是用第一类写法就会判断为True

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        return cmp(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        # 注意，首先调用cmp方法，判断跟节点，然后递归调用HasSubTree方法，判断左右节点

def pre_order(node):
    if node is not None:
        print(node.val, end=" ")
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.val, end=" ")
        in_order(node.right)
```

# 9.栈的压入，弹出序列 （重点复习）
## 题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
## 考点
这是一个经典问题，仔细体会
```python
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False
        support_stack = []
        while len(pushV) > 0:
            a = pushV.pop(0)
            if a != popV[0]:
                support_stack.append(a)
            else:
                popV.pop(0)
                if len(popV) == 0:
                    break
                while popV[0] == support_stack[-1]:
                    popV.pop(0)
                    support_stack.pop()
                    if len(support_stack) == 0:
                        break
        if len(support_stack) == 0:
            return True
        else:
            return False
```

# 10.二叉搜索树的后序遍历序列
## 题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
## 考点
二叉搜索树的概念
```python
# -*- coding:utf-8 -*-
def cmp(sequence):
    if len(sequence) == 0 or len(sequence) == 1:
        return True
    now = sequence.pop()
    ids = 0
    for i in range(len(sequence)):
        if sequence[i] < now:
            ids += 1
        else:
            break
    if ids == len(sequence):
        return cmp(sequence)
    if now > min(sequence[ids:]):
        return False
    else:
        return cmp(sequence[:ids]) and cmp(sequence[ids:])


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence) == 0:
            return False
        if cmp(sequence):
            return True
        else:
            return False
```

# 11.字符串排列
## 题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
## 考点
回溯法,递归
```python
def find(ss):
    if len(ss) == 0:
        return None
    if len(ss) == 1:
        return ss
    else:
        result = []
        for i in range(0, len(ss)):
            if i == 0 or ss[i] != ss[0]:
                tmp = ss[i]
                ss[i] = ss[0]
                ss[0] = tmp
                new_result = find(ss[1:])
                for new in new_result:
                    new = ss[0] + new
                    result.append(new)
                tmp = ss[i]
                ss[i] = ss[0]
                ss[0] = tmp
        return result
class Solution:
    def Permutation(self, ss):
        if len(ss) == 0:
            return []
        else:
            ss = list(ss)
            result = find(ss)
            result.sort()
            return result
```

# 12.连续子数组的最大和
## 题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

定义：F\[i]: 以array\[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
那么：F\[i] = max(F\[i-1]+array\[i], array\[i])

# 13.丑数
## 题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
## 思路
用三个指针分别表示通过乘2，乘3，乘5到达的目前最大的丑数的位置。
产生下一个丑数时，取三个指针对应的丑数分别乘2，乘3，乘5后的最小值，作为下一个丑数。
同时把对应指针右移一位
```python
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        result = [1]
        (p2, p3, p5) = (0, 0, 0)
        for i in range(1, index):
            result.append(min(result[p2] * 2, result[p3] * 3, result[p5] * 5))
            if result[i] == result[p2] * 2:
                p2 += 1
            if result[i] == result[p3] * 3:
                p3 += 1
            if result[i] == result[p5] * 5:
                p5 += 1
        return result[-1]
```
# 孩子们的游戏
## 题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

感觉做好的做法是循环链表，但是python不好实现循环链表，因此考虑用数组代替。
然而用数组代替，在搜索下一个还在圈子里的人时，要花费大量时间，可能会让判定超时。
因此再进一步考虑用两个数组来记录，当前退出的人的上下文。减少搜索用的时间。

```python
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 使用两个记号数组记录上下文。这样方便查找下一个
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        all = [1] * n
        next = [i for i in range(1, n)]
        next.append(0)
        last = [i for i in range(n-1)]
        last.insert(0, n-1)
        num = n
        now = 0
        while num > 1:
            r = 0
            while r < m:
                if all[now] != 0:
                    if r != m-1:
                        now = next[now]
                    r += 1
                else:
                    now = next[now]
                # if all[now] != 0:
                #     if r != m - 1:
                #         now = (now + 1) % n
                #     r += 1
                # else:
                #     now = (now + 1) % n
            all[now] = 0
            flag = next[now]
            last[next[now]] = last[now]
            next[last[now]] = next[now]
            next[now] = -1
            last[now] = -1
            now = flag
            num -= 1
        print(all.index(1))
        return all.index(1)
    # 不用记号数组记录上下文的写法。这样搜索下一个还在圈内的人时容易超时。
    def LastRemaining_Solution1(self, n, m):
        if n < 1 or m < 1:
            return -1
        all = [1] * n
        num = n
        now = 0
        while num > 1:
            r = 0
            while r < m:
                if all[now] != 0:
                    if r != m - 1:
                        now = (now + 1) % n
                    r += 1
                else:
                    now = (now + 1) % n
            all[now] = 0
            # print(num, all)
            num -= 1
            now = (now + 1) % n
            while all[now] != 1:
                now = (now + 1) % n
        print(all.index(1))
        return all.index(1)

# 双向循环链表的写法,最简洁
    def LastRemaining_Solution2(self, n, m):
        if n < 1 or m < 1:
            return -1
        # if n == 1:
        #     return 0
        head = Node(0)
        now = head
        for i in range(1, n):
            new_node = Node(i)
            now.right = new_node
            new_node.left = now
            now = new_node
        now.right = head
        head.left = now
        now = head
        residue = n
        while residue > 1:
            for r in range(0, m-1):
                now = now.right
            now.left.right = now.right
            now.right.left = now.left
            a = now
            now = now.right
            del a
            residue -= 1
        return now.val
```

#不用加减乘除做加法(还没搞懂)
## 题目描述
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

进制转化
```python
class Solution:
    def Add(self, num1, num2):
        if num2 == 0:
            return num1
        sum = 0
        carry = 0
        while num2 != 0:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum & 0xFFFFFFFF # 考虑负数
            num2 = carry
            # print(bin(num1), bin(num2))
        num1 = num1 if num1 >> 31 == 0 else num1 - 4294967296
        # print(num1)
        return num1
```

#正则表达式匹配
## 题目描述
请实现一个函数用来匹配包括'.'和'\*'的正则表达式。模式中的字符'.'表示任意一个字符，而'\*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab\*ac\*a"匹配，但是与"aa.a"和"ab\*a"均不匹配

贪婪匹配 (用动态规划来做？)
分两种情况讨论。
pattern的下一个字符为\*或者不为*。考虑几个特殊情况: ".\*","\**"(原题中没考虑这种情况),"b与b\*b"(\*到底产生了多少个b？)

```python
def check(pattern):
    if len(pattern) == 0:
        return True
    if pattern[0] == "*":
        print("error")
        return False
    ids = len(pattern) - 1
    if pattern[ids] != "*":
        return False
    else:
        if pattern[ids - 1] == "*":
            return True
        return check(pattern[:-2])


class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # print(s, pattern)
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(s) != 0 and len(pattern) == 0:
            return False
        if len(s) == 0 and len(pattern) != 0:
            return check(pattern)
        if len(pattern) > 1 and pattern[1] == "*":
            if pattern[0] == "." or pattern[0] == s[0]:
                f1 = self.match(s, pattern[2:])  # 代替0个
                f2 = self.match(s[1:], pattern[2:])  # 代替1个
                f3 = self.match(s[1:], pattern)  # 代替多个
                return f1 or f2 or f3
            else:
                return self.match(s, pattern[2:])
        elif pattern[0] == s[0] or pattern[0] == ".":
            return self.match(s[1:], pattern[1:])
        else:
            return False
```
