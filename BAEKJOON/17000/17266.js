const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0]);
const M = parseInt(input[1]);
const x = input[2].split(' ').map(ele => {return parseInt(ele)});
let arr = [];
for(let i = 1; i < x.length; i++){
  arr.push(Math.ceil((x[i]-x[i-1]) / 2));
}
let max = Math.max(...arr,x[0],N-x[x.length-1]);
console.log(max)