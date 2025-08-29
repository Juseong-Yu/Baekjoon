const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ')

let A = Math.min(...input)
let B = Math.max(...input)

let Acol = Math.ceil(A/4);
let Bcol = Math.ceil(B/4);
let Arow = A % 4;
if(Arow === 0){
  Arow = 4
}
let Brow = B % 4;
if(Brow === 0){
  Brow = 4
}
let result = Bcol-Acol + Math.abs(Arow-Brow)
console.log(result)