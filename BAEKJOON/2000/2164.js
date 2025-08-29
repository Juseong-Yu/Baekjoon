const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

let N = parseInt(input);
let arr = [];
let inArr = false;
if (N === 1){
  console.log(1)
}else{
  for (let i = 1; i <= N; i += 1){
  arr.push(i)
}

while (true){
  let tmparr = [];
  if(arr.length % 2 === 1){
    tmparr.push(arr.pop())
  }
  for (let j = 1; j < arr.length; j += 2){
    tmparr.push(arr[j])
  }
  arr = tmparr;
  if (arr.length === 1){
    break
  }
}
console.log(arr[0])
}
