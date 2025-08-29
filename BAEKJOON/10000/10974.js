const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

const N = parseInt(input);
let arr = [];

for(let i = 1; i <= N; i++){
  arr.push([i])
}
for (let j = 1; j < N; j++){
  let tmparr = []
  for (let n = 0; n < arr.length; n++){
    for(let m = 1; m <= N; m++){
      if(!arr[n].includes(m)){
        let tmp = arr[n].slice()
        tmp.push(m)
        tmparr.push(tmp)
      }
    }  
  }
  arr = tmparr.slice()
}

for(let k = 0; k < arr.length; k++){
  console.log(...arr[k])
}