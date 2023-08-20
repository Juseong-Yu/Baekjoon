const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()
let cal = false
let result = null


if(input.indexOf('-') === 0){
  cal = true;
  input = input.slice(1);
}

if(input.includes('+')){
  input = input.split('x');
  if(input[0] === ''){
    result = 1
  }else{
    result = input[0];
  }
}else if(input.includes('-')){
  input = input.split('x');
  if(input[0] === ''){
    result = 1
  }else{
    result = input[0];
  }
}else{
  if(input.includes('x')){
    input = input.split('x');
    if(input[0] === ''){
      result = 1
    }else{
      result = input[0]
    }
    
  }else{
    result = 0
  }
}
if(result === 0){
  console.log(0)
}else if(cal === true){
  console.log('-'+result)
}else{
  console.log(result)
}