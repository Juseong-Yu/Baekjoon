const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ');

const N = parseInt(input[0]);
const M = parseInt(input[1]);
let arr = [];
for (let k = 1; k <= N; k++){
  arr.push([k])
}
for (let i = 1; i < M; i++){
  let tmparr = []
  for (let j = 0; j < arr.length; j++){
    for(let p = arr[j][arr[i].length-1]; p <= N ; p++){
      let tmp = arr[j].slice()
      tmp.push(p)
      tmparr.push(tmp)
    }
  }
  arr = tmparr.slice()
}
for(let idx = 0; idx < arr.length; idx++){
  console.log(...arr[idx])
}