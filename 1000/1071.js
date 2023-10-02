const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

const N = parseInt(input[0]);
let arr = input[1].split(' ').map((ele)=>{return parseInt(ele)});

arr.sort((function(a,b){
  return a-b;
}))

let result = [arr[0]];
arr = arr.slice(1)
let tmp = []
let times = arr.length;
for (let i = 1; i < times+1; i++){
  let findmin = false;
  while(findmin === false){
    let min = Math.min(...arr)
    if(arr.length === 0){
      break
    }else if(min === result[i-1] + 1){
      let idx = arr.indexOf(min);
      let move = arr.splice(idx,1);
      tmp.push(...move);
    }else{
      let idx = arr.indexOf(min);
      let move = arr.splice(idx,1);
      result.push(...move);
      findmin = true;
    }
  }
  if(arr.length === 0 && findmin === false){
    break
  }
  arr = [...arr,...tmp];
  tmp = [];
  
}
if(tmp.length !== 0){
  let findplace = -1;
  for(let k = result.length-1; k >= 0; k--){
    if(result[k]+1 !== tmp[0]){
      findplace = k;
      break
    }
  }
  result = [...result.slice(0,findplace+1),...tmp,...result.slice(findplace+1)]
}
if(result.length !== 0){
  console.log(...result)
}else{
  console.log()
}
