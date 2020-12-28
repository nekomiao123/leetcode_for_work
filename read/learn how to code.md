# 学习怎么写代码

## 简介

只是把我读到的信息，经过我的理解进行二次输出

## 一、学习算法和刷题的思路指南

### 1.数据结构

数据结构只有两种存储方式：数组（顺序存储）和链表（链式存储）

数据结构还有很多，散列表、栈、队列、堆、树、图等等，但总的来看各种数据结构的底层存储，确实除了数组就是链表了。

**数组**由于是紧凑连续存储,可以随机访问，通过索引快速找到对应元素，而且相对节约存储空间。但正因为连续存储，内存空间必须一次性分配够，所以说数组如果要扩容，需要重新分配一块更大的空间，再把数据全部复制过去，时间复杂度 O(N)；而且你如果想在数组中间进行插入和删除，每次必须搬移后面的所有数据以保持连续，时间复杂度 O(N)。

**链表**因为元素不连续，而是靠指针指向下一个元素的位置，所以不存在数组的扩容问题；如果知道某一元素的前驱和后驱，操作指针即可删除该元素或者插入新元素，时间复杂度 O(1)。但是正因为存储空间不连续，你无法根据一个索引算出对应元素的地址，所以不能随机访问；而且由于每个元素必须存储指向前后元素位置的指针，会消耗相对更多的储存空间。

### 2.基本操作

基本操作 遍历+访问  具体一点就是增删查改。

在各种不同的场景里面，尽可能高效的增删查改，这就是数据结构的使命。

遍历+访问的方式

- 线性   for/while作为代表
- 非线性 递归

数组遍历框架，典型的线性迭代结构：

```
void traverse(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        // 迭代访问 arr[i]
    }
}
```

链表遍历框架，兼具迭代和递归结构：

```
/* 基本的单链表节点 */
class ListNode {
    int val;
    ListNode next;
}

void traverse(ListNode head) {
    for (ListNode p = head; p != null; p = p.next) {
        // 迭代访问 p.val
    }
}

void traverse(ListNode head) {
    // 递归访问 head.val
    traverse(head.next)
}
```

二叉树的递归遍历结构和链表相似

```
/* 基本的二叉树节点 */
class TreeNode {
    int val;
    TreeNode left, right;
}

void traverse(TreeNode root) {
    traverse(root.left)
    traverse(root.right)
}
```

二叉树框架可以扩展为 N 叉树的遍历框架：

```
/* 基本的 N 叉树节点 */
class TreeNode {
    int val;
    TreeNode[] children;
}

void traverse(TreeNode root) {
    for (TreeNode child : root.children)
        traverse(child);
}
```

N 叉树的遍历又可以扩展为图的遍历，因为图就是好几 N 叉棵树的结合体。你说图是可能出现环的？这个很好办，用个布尔数组 visited 做标记就行了，这里就不写代码了。

所以在链表的基础上，可以写出二叉树、N叉树、图等的代码（一步步递进），这就是大框架

### 3.刷题指南

**数据结构是工具，算法是通过合适的工具解决特定问题的方法**。

**先刷二叉树，先刷二叉树，先刷二叉树**！

**二叉树是最容易培养框架思维的，而且大部分算法技巧，本质上都是树的遍历问题**。

从二叉树去理解框架的概念。

### 4. 总结

在刷二叉树的过程中逐步逐步去理解框架

# 二、书籍推荐

《algorithms Fourth Edition》

![image-20201228191304129](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20201228191304129.png)



# 参考链接

https://github.com/labuladong/fucking-algorithm

https://github.com/TheAlgorithms/Python