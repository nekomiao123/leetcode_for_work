# Dynamic programming Notes One

[The link](https://www.youtube.com/watch?v=oBt53YbR9Kk)

## Begin with fib memoization

```javascript
const fib = (n)=>{
  if (n<=2) return 1;
  return fib(n-1) + fib(n-2);
};
```

The time complexity is $O(2^n)$ 

The space comlexity is $O(n)$

![image-20210303203734777](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210303203734777.png)

### improve

Many subtrees are the same. We need reuse this subtrees.

So, we can just store some subtrees which means we can store more values to do this.

```javascript
const fib = (n, memo={})=>{
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
  };
```

![image-20210303210217668](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210303210217668.png)

If we use this tech, it will be like this .

The time comlexity is $O(n)$

The space comlexity is $O(n)$

## Then we go with grid-g questions

![image-20210303210729083](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210303210729083.png)

![image-20210303211612556](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210303211612556.png)

![image-20210303211639479](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210303211639479.png)

So, firstly, we can find the edge of this problem which is that if m or n is zero, there is no way to go. The value will be zero.

```javascript
const gridTravelar = (m, n) => {
  if (m==1 && n==1) return 1;
  if (m==0 || n==0) return 0;
  return gridTravelar(m-1, n) + gridTravelar(m, n-1);
};
```

Time complexity $O(2^{m+n})$

Space complexity $O(n+m)$

### improve

So, the same as the fib function, we can store some numbers to avoid from mant dupilcate computation.

```javascript
const improve_gridTravelar = (m, n, memo={}) => {
  const key = m + "," + n;
  if (key in memo) return memo[key];
  if (m==1 && n==1) return 1;
  if (m==0 || n==0) return 0;
  memo[key] =  improve_gridTravelar(m-1, n, memo) + improve_gridTravelar(m, n-1, memo);
  return memo[key]
};
```

Time complexity $O(n*m)$

Space complexity $O(n+m)$

## Memoization Recipe

1. Make it work.
   - Visualize the problem as a tree
   - Implement the tree using recursion
   - Test it
2. Make it efficient
   - add a memo object
   - add a base a case to return memo values
   - Store return values into the memo

