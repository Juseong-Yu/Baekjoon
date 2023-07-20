const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

const n = parseInt(input);
let arr = [1,1,1,1,1,1,1,1,1,1];
let tmp = []
let result = 10
for (let i = 1; i < n; i++){
  for (let j = 0; j < 10; j++){
    tmp.push(arr.slice(0,j+1).reduce((acc,cur) => acc+cur)% 10007)
  }
  result = tmp.reduce((acc,cur) => acc+cur)
  arr = tmp.slice()
  tmp = []
}
console.log(result % 10007)