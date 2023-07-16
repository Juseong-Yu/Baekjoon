const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n')

let T = parseInt(input[0]);

for (let i = 1; i <= T; i++){
  let result = 'YES'
  let arr = input[i].split('');
  let stack = []
  for (let j = 0; j < arr.length; j++){
    if(arr[j]==='('){
      stack.push(arr[j]);
    }else{
      if (stack.slice(-1)[0] === '('){
        stack.pop()
      }else{
        result = 'NO'
      }
    }
  }
  if(stack.length !== 0){
    result = 'NO'
  }
  console.log(result)
}

