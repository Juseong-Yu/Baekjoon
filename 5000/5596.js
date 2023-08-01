const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

let minguk = input[0].split(' ').map((ele) => parseInt(ele)).reduce((acc,cur) => acc + cur);
let manse = input[1].split(' ').map((ele) => parseInt(ele)).reduce((acc,cur) => acc + cur);

if (minguk > manse){
  console.log(minguk);
}else{
  console.log(manse)
}