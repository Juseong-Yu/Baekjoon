const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const T = parseInt(input[0]);
for (let i = 1; i < T+1; i++){
  let A = input[i].split(' ').map((ele)=> {return parseInt(ele)});
  let max = 0;
  for (let n = 0; n < 3; n++){
    max = Math.max(...A);
    index = A.indexOf(max);
    A.splice(index,1);
  }
  console.log(max)
}