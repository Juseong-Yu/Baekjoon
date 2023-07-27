const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0]);
const M = parseInt(input[1]);
const broken = input[2].split(' ').map((ele)=>parseInt(ele));

const result1 = Math.abs(N - 100);
let result2= 0;
let result3 = 0;
let push = 0
while(true){
  let flag = false;
  var minus = N - push;
  if (minus < 0){
    result2 = Infinity
    break
  }
  let minusarr = minus.toString().split('').map((ele) => parseInt(ele));
  for (let i = 0; i < minusarr.length; i++){
    if(broken.includes(minusarr[i])){
      flag = true
    }
  }
  if(flag === false || result1 < push + plusarr.length){
    result2 = push + minusarr.length;
    break
  }else{
    push +=1
  }
}
push = 0
while(true){
  let flag = false;
  var plus = N + push;
  let plusarr = plus.toString().split('').map((ele) => parseInt(ele));
  for (let i = 0; i < plusarr.length; i++){
    if(broken.includes(plusarr[i])){
      flag = true
    }
  }
  if(flag === false || result1 < push + plusarr.length){
    result3 = push + plusarr.length;
    break
  }
  push +=1
}
console.log(Math.min(result1,result2,result3))