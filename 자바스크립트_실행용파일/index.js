const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0]);
let result = 0
for(let i = 1; i <= N; i++){
  let adder = parseInt(input[i]);
  adder -=1
  result += adder 
}
console.log(result +1)