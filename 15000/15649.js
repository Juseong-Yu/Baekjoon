const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ');

// const N = parseInt(input[0]);
// const M = parseInt(input[1]);

// function NM(n,m,used,arr){
//   if(m == 1){
//     for(let i = 1; i <= n; i++){
//       if(!used.includes(i)){
//         arr.push([...used,i])
//       }
//     }
//     return arr
//   }else{
//     let result = []
//     for(let j = 1; j <= n; j++){
//       if(!used.includes(j)){
//         result = [...NM(n,m-1,[...used,j],arr)];
//       }
//     }
//     return result
//   }
  
// }

// let done = NM(N,M,[],[]);

// for (let k = 0; k < done.length; k++){
//   console.log(...done[k])
// }

const N = parseInt(input[0]);
const M = parseInt(input[1]);

function NM(n, m, used, result) {
  if (m === 0) {
    console.log(...used);
    return;
  }

  for (let j = 1; j <= n; j++) {
    if (!used.includes(j)) {
      NM(n, m - 1, [...used, j], result);
    }
  }
}

NM(N, M, [], []);