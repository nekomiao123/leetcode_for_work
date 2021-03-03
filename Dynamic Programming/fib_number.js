const fib = (n, memo={})=>{
    if (n in memo) return memo[n];
    if (n <= 2) return 1;
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
    return memo[n];
};


const base_fib = (n)=>{
  if (n<=2) return 1;
  return fib(n-1) + fib(n-2);
};


console.log(fib(1));
// console.log(fib(100));
console.log(base_fib(100));

