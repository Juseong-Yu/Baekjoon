const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const n = parseInt(input[0]);
const k = input[1].split(' ');
let arr = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]]
for(let i = 0; i < n; i++){
  let tmparr = []
  if(k[i] === '<'){
    for (let m = 0; m < arr.length; m++){
      for (let p = parseInt(arr[m][i])+1; p < 10; p++){
        if(!arr[m].includes(p)){
          let tmp = arr[m].slice()
          tmp.push(p)
          tmparr.push(tmp)
        }
      }
    }
  }else if(k[i] === '>'){
    for (let m = 0; m < arr.length; m++){
      for (let p = parseInt(arr[m][i])-1; p >=0 ; p--){
        if(!arr[m].includes(p)){
          let tmp = arr[m].slice()
          tmp.push(p)
          tmparr.push(tmp)
        }
      }
    }
  }
  arr = tmparr.slice()
}
arr = arr.map((ele) => ele.join(''))
let max = Math.max(...arr)
let min = Math.min(...arr)
if (min < Math.pow(10,n)){
  min = '0' + min
  max = String(max)
}else{
  min = String(min)
  max = String(max)
}
console.log(max)
console.log(min)