const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ');

let N = parseInt(input[0]);
const B = parseInt(input[1]);
let result = [];

while (N / B > 0){
  let num = N % B;
  N = Math.floor(N / B);
  if(num >= 10){
    num = String.fromCharCode(num+55)
  }
  result.unshift(num);
}

console.log(result.join(''));