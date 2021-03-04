# Dynamic programming Notes Two

[The link](https://www.youtube.com/watch?v=oBt53YbR9Kk)

## The canSum question

![image-20210304110933588](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210304110933588.png)

Base solution

```javascript
const canSum = (targetSum, numbers) =>{
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    for(let num of numbers){
        const remainder = targetSum - num;
        if(canSum(remainder, numbers)) return true;
    }
    return false;
};
```

Time complexity $O(n^m)$

Space complexity $O(m)$

![image-20210304111037478](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210304111037478.png)

### improve

The same idea as before

```javascript
const improve_canSum = (targetSum, numbers, memo={}) =>{
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    for(let num of numbers){
        const remainder = targetSum - num;
        if(improve_canSum(remainder, numbers, memo)) {
            memo[targetSum] = true;
            return true;
        }
    }
    memo[targetSum] = false;
    return false;
};
```

Time complexity $O(m*n)$

Space complexity $O(m)$

## The howSum question

![image-20210304112114773](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210304112114773.png)

```javascript
const howSum = (targetSum, numbers) =>{
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    for (let num of numbers){
        const remainder = targetSum - num;
        const remainderResult = howSum(remainder, numbers);
        if (remainderResult !== null){
            return [ ...remainderResult, num];
        }
    }

    return null;
};
```

m = target sum

n = numbers

Time complexity $O(n^m*m)$

Space comlexity $O(m)$

### improve

```javascript

const improve_howSum = (targetSum, numbers, memo={}) =>{
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    for (let num of numbers){
        const remainder = targetSum - num;
        const remainderResult = improve_howSum(remainder, numbers, memo);
        if (remainderResult !== null){
            memo[targetSum] = [ ... remainderResult, num];
            return memo[targetSum];
        }
    }

    memo[targetSum] = null;
    return null;
};
```

Time complexity $O(n*m^2)$

Space complexity $O(m^2)$ 

## The bestSum problem

![image-20210304201006420](https://cdn.jsdelivr.net/gh/nekomiao123/pic/img/image-20210304201006420.png)

