const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

const N = parseInt(input[0]);
let arr = [];
for(let i = 1; i <= N; i++){
  let TP = input[i].split(' ').map((ele) => parseInt(ele));
  arr.push(TP);
}

let results = [0]
function bind(N, D, added, arr){
    for(let i = 0; i < arr.length; i++){
      let add = added
      let d = D
      let tmp = arr[i]
      arrtmp = arr.slice(i);
      arrtmp = arrtmp.slice(tmp[0])
      d = d+i+tmp[0]
      if(N < d){
      }else{
        add += tmp[1]
        results.push(add)
        bind(N, d, add, arrtmp)
      }
  }
}
bind(N,0,0,arr);
console.log(Math.max(...results));