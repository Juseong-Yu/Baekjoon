const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0]);
const A = input[1].split(' ').map((ele) => parseInt(ele));
let dp = [1]
for (let i = 1; i < A.length; i++){
  let dpmax = 1
  for (let j = 0; j < i; j++){
    if (A[j] < A[i] && dpmax < dp[j]+1){
        dpmax = dp[j]+1
    }
  }
  dp.push(dpmax);
}
result = Math.max(...dp);
console.log(result);