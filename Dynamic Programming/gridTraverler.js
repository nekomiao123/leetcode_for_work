const base_gridTravelar = (m, n) => {
  if (m==1 && n==1) return 1;
  if (m==0 || n==0) return 0;
  return base_gridTravelar(m-1, n) + base_gridTravelar(m, n-1);
};


const improve_gridTravelar = (m, n, memo={}) => {
  const key = m + "," + n;
  if (key in memo) return memo[key];
  if (m==1 && n==1) return 1;
  if (m==0 || n==0) return 0;
  memo[key] =  improve_gridTravelar(m-1, n, memo) + improve_gridTravelar(m, n-1, memo);
  return memo[key]
};


console.log(base_gridTravelar(2,3))
console.log(base_gridTravelar(18,18))
console.log(improve_gridTravelar(3,3))
console.log(improve_gridTravelar(18,18))




