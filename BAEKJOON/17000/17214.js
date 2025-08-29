const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim();
let xx = '';
let x = '';
let w = '+W';
if(input.includes('x')){
  input = input.split('x')
  if(input[0] === '2' ){
    xx = 'xx';
  }else if(input[0] === '-2'){
    xx = '-xx';
  }else{
    xx = input[0]/2+'xx'
  }

  if(input[1] !== ''){
    if(input[1] === '+1'){
      x = '+x';
    }else if(input[1] === '-1'){
      x = '-x';
    }else{
      x = input[1]+'x';
    }
  }
}
else{
  if (input === '0'){
    x = '';
    w = 'W';
  }else{
    if(input === '-1'){
      x = '-x';
    }else if(input === '1'){
      x = 'x';
    }else{
      x = input+'x'
    }
    
  }
  
}

console.log(xx+x+w)