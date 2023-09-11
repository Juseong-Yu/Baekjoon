const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split(' ');

let A = input[0].split('');
let B = input[1].split('');
let min = [50];
for(let i = 0; i < B.length-A.length+1; i++){
  let result = 0;
  for(let j = 0; j < A.length; j++){
    if(A[j] != B[j+i]){
      result += 1;
    }
  }
  min.push(result);
}
console.log(Math.min(...min));