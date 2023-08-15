const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ');

const E = parseInt(input[0]);
const S = parseInt(input[1]);
const M = parseInt(input[2]);

for (let i = 1; i <= 7980; i++){
  if ((i%15 === E && i%28 === S && i%19 === M) || i === 7980){
    console.log(i)
    break
  }
}
