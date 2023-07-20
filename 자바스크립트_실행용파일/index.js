const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

const N = parseInt(input)
for (let i = 0; i < N; i++){
  let result =  ((N-i)*2-1)
  console.log(result);
}