const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ');

let N = parseInt(input[0]);
let M = parseInt(input[1]);
let K = parseInt(input[2]);

for (let i = 0; i < K; i++){
  if (N / 2 > M){
    N--
  }else{
    M--
  }
}

if (N / 2 > M){
  console.log(M)
}else{
  console.log(Math.floor(N/2))
}