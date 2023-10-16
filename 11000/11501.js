const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

const T = parseInt(input[0]);

for (let testcase = 0; testcase < T; testcase++){
  let N = parseInt(input[2*testcase+1]);
  let arr = input[2*testcase+2].split(' ').map((ele) => parseInt(ele));
  let earn = 0;
  let nowMax = arr[N - 1]
  for(let i = N - 2; i >= 0; i--){
    if(nowMax < arr[i]){
      nowMax = arr[i];
    }else{
      earn += nowMax - arr[i]
    }
  }
  console.log(earn);
}