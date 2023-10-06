const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

let N = parseInt(input[0]);
let A = input[1].split(' ').map(ele => {return parseInt(ele)});
const input2 = input[2].split(' ');
let B = parseInt(input2[0]);
let C = parseInt(input2[1]);

let count = 0;
for(let i = 0; i < N; i++){
  count++;
  if(A[i] - B >= 0){
    count += Math.ceil((A[i] - B) / C)
  }
}

console.log(count)