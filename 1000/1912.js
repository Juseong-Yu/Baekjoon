const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n')

const n = parseInt(input[0]);
const arr1 = input[1].split(' ').map((ele)=> parseInt(ele));
let arr2 = [arr1[0]]
for(let i = 1; i < n; i++){
  if (arr1[i] >= arr2[i-1] + arr1[i] ){
    arr2.push(arr1[i])
  }else{
    arr2.push(arr2[i-1]+ arr1[i])
  }
}
const result = Math.max(...arr2)
console.log(result)