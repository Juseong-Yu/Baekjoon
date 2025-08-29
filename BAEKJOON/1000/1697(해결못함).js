const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ');

const N = parseInt(input[0]);
const K = parseInt(input[1]);
let X = N;
let arr = [X];
let times = 0;
let result = 'notmade'
if (N === K){

}else{
  while(true){
    times++
    let tmparr = [];
    while(arr.length > 0){
      X = arr.shift()
      if(X+1 === K || X-1 === K || 2*X === K){
        result = 'made';
        break
      }else{
        if (X+1 > 0 && X+1 <= 100000 && !tmparr.includes(X+1)){
          tmparr.push(X+1)
        }
        if (X-1 > 0 && X-1 <= 200000 && !tmparr.includes(X-1)){
          tmparr.push(X-1)
        }
        if (X*2 > 0 && X*2 <= 200000 && !tmparr.includes(X*2)){
          tmparr.push(X*2)
        }
      }
    }
    arr = tmparr.slice()
    if(result === 'made'){
      break;
    }
  }
}

console.log(times)