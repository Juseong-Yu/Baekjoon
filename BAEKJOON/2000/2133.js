const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

const N = parseInt(input)
let result = 0;
let arr = [1,0,3,0,11];
if (N === 1 || N === 3){
  result = 0
}else if (N === 2){
  result = 3
}else if (N === 4){
  result = 11
}else{
  for(let i = 5; i <= N; i++){
    let tiles = arr[i-2]*3
    for (let j = 4; i-j >= 0; j+=2){
      tiles += arr[i-j]*2
    }
    arr.push(tiles)
  }
  result = arr[arr.length-1]
}
console.log(result)

// N : 1 ANS : 0

// N : 2 ANS : 3

// N : 3 ANS : 0

// N : 4 ANS : 11

// N : 5 ANS : 0

// N : 6 ANS : 41

// N : 7 ANS : 0

// N : 8 ANS : 153

// N : 9 ANS : 0

// N : 10 ANS : 571

// N : 30 ANS : 299303201