const canSum = (targetSum, numbers) =>{
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    for(let num of numbers){
        const remainder = targetSum - num;
        if(canSum(remainder, numbers)) return true;
    }
    return false;
};

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



console.log(canSum(7,[2,3,4,7]));
console.log(canSum(7,[2,4]));
console.log(canSum(10,[2,3,4,5]));
console.log(improve_canSum(300,[7,14]));


