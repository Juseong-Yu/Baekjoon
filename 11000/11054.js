const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0]);
const A = input[1].split(' ').map((ele) => parseInt(ele));

function longarr (arr){
  let dp = [1]
  for (let i = 1; i < arr.length; i++){
    let dpmax = 1
    for (let j = 0; j < i; j++){
      if (arr[j] < arr[i] && dpmax < dp[j]+1){
          dpmax = dp[j]+1
      }
    }
    dp.push(dpmax);
  }
  result = Math.max(...dp);
  return result
};

let max = 0
for (let top = 0; top < A.length; top++){
  let leftarr = A.slice(0,top+1);
  let rightarr = A.slice(top);

  let tmpresult = longarr(leftarr) + longarr(rightarr.reverse())-1;
  if (max < tmpresult){
    max = tmpresult
  }
}

console.log(max)
