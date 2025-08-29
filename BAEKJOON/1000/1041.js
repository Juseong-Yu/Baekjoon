const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0])
let arr = input[1].split(' ').map((ele) => parseInt(ele));
arr = [...arr.slice(0,3),arr[5],arr[4],arr[3]]
let result = 0;
let point = 4;
let narrow = (N-2)*8+4
let space = 5 * (N-2)*(N-2) + (N-2)*4;
let min_1 = Math.min(...arr)
let min_2 = Math.max(...arr);
min_2 = min_2 + min_2
let min_3 = Math.max(...arr);
min_3 = min_3 + min_3 + min_3 
if(N === 1){
  result = arr.reduce((acc,cur)=>acc+cur) - Math.max(...arr)
}else{
  for(let i = 1; i < 6; i++){
  for (let k = 0; k < i; k++){
    if(i !== k+3){
      if(min_2 > arr[i]+arr[k]){
        min_2 = arr[i]+arr[k]
      }
    }
  }
}
for (let q = 2; q < 6; q++){
  for (let w = 1; w < q; w++){
    for (let e = 0; e < w; e++){
      if(q !== w+3 && q !== e+3 && w !== e+3){
        if(min_3 > arr[q]+arr[w]+arr[e]){
          min_3 = arr[q]+arr[w]+arr[e]
        }
      }
    }
  }
}
if (N === 1){
  result = arr.reduce((acc,cur) => acc+ cur);
}else{
  result = min_1*space + min_2 * narrow + min_3 * point
}
}
console.log(result)