const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ');

const A = parseInt(input[0]);
const B = parseInt(input[1]);
let arr = [];
let num = 1;
let result = 0;
while(arr.length <= 1000){
  for (let i = 0; i < num; i++){
    arr.push(num)
  }
  num++
}

for (let j = A-1; j < B; j++){
  result += arr[j]
}
console.log(result)