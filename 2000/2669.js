const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

let arr = Array.from({ length: 101 }, () => Array(101).fill(0));

for(let rect = 0; rect < 4; rect++){
  let now = input[rect].split(' ');
  let nowx1 = parseInt(now[0]);
  let nowx2 = parseInt(now[2]);
  let nowy1 = parseInt(now[1]);
  let nowy2 = parseInt(now[3]);
  for(let x = nowx1; x < nowx2; x++){
    for(let y = nowy1; y < nowy2; y++){
      arr[y][x] = 1;
    }
  }
}
for (let i = 0; i < arr.length; i++){
  arr[i] = arr[i].reduce(function add(sum, cur){
  return sum + cur;
},0)
}
console.log(arr.reduce(function add(sum, cur){
  return sum + cur;
},0))