const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
// let input = fs.readFileSync(path).toString();
  let input = fs.readFileSync(path).toString().split("\n");

  for (let j = 0; j < input.length; j++){
    if(input[j] == '0'){
    break
  }else{
    let arr = input[j].split('')
      let count = 0;
      for (let i = 0; i < arr.length; i++){
        if (arr[i] === '0'){
          count += 4;
        }else if (arr[i] === '1'){
          count += 2;
        }else{
          count +=3; 
        }
      } 
      console.log(count+arr.length + 1);
  }
  }
  
