const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

const N = parseInt(input[0]);
arr = input.slice(1,N+1).sort();
let max = 0;
let maxword = arr[0];
let row = 0;
let rowword = '';

for(let i = 0; i < arr.length; i++){
  if(rowword === arr[i]){
    row += 1;
    if(row > max){
      max = row;
      maxword = rowword;
    }
  }else{
    row = 0;
    rowword = arr[i];
  }
}

console.log(maxword)