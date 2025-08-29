const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

const N = parseInt(input[0]);
let stack = [];
let result = [];
for (let i = 1; i <= N; i++){
  let order = input[i].split(' ');
  let word = order[0];
  if(word === 'push'){
    let num = order[1]
    stack.push(parseInt(num))
  }else if(word === 'pop'){
    if(stack.length === 0){
      result.push(-1);
    }else{
      let pop = stack.pop();
    result.push(parseInt(pop));
    }
  }else if(word === 'size'){
    result.push(stack.length);
  }else if(word === 'empty'){
    if(stack.length === 0){
      result.push(1);
    }else{
      result.push(0);
    }
  }else if(word === 'top'){
    if(stack.length === 0){
      result.push(-1);
    }else{
      result.push(parseInt(stack[stack.length-1]));
    }
    
  }
}

console.log(result.join('\n'))