const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

let M = input[0]
let ball = 1
for (let i = 0; i < M; i++){
  arr = input[i+1].split(' ');
  a = parseInt(arr[0])
  b = parseInt(arr[1])
  if (a === ball){
    ball =  b
  }else if( b === ball){
    ball =  a
  }
}
console.log(ball)