const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split(' ');

const K = parseInt(input[0]);
const N = parseInt(input[1]);
const M = parseInt(input[2]);

let result = K * N - M;
if(result < 0){
  console.log(0);
}else{
  console.log(result);
}