const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

N = parseInt(input[0]);
let arr = [];
let result = 1;
while(true){
  for(let i = 1; i <= N; i++){
    if(arr.includes(input[i].slice(-result))){
      result += 1
      arr = []
      break
    }else{
      arr.push(input[i].slice(-result))
    }
  }
  if (result === input[1].length || arr.length === N){
    break
  }
}
console.log(result)
