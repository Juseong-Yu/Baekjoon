const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('=');

let M1M2 = input[0].split('+');
let M1 = M1M2[0];
let M2 = M1M2[1];
let M3 = input[1];

function makearr(exp){
  //순서대로 C,H,O의 갯수가 저장되어 있음
  let arr = [0,0,0];
  for(let i = 0; i < exp.length; i++){
    if(parseInt(exp[i])<=9 && parseInt(exp[i])>=0){
      let ele = exp[i-1]
      if(ele === 'C'){
        arr.splice(0,1,arr[0]+parseInt(exp[i]))
      }else if(ele === 'H'){
        arr.splice(1,1,arr[1]+parseInt(exp[i]))
      }else{
        arr.splice(2,1,arr[2]+parseInt(exp[i]))
      }
    }
    else if(!(parseInt(exp[i])<=9 && parseInt(exp[i])>=0) && !(parseInt(exp[i+1])<=9 && parseInt(exp[i+1])>=0)){
      let ele = exp[i]
      if(ele === 'C'){
        arr.splice(0,1,arr[0]+1)
      }else if(ele === 'H'){
        arr.splice(1,1,arr[1]+1)
      }else{
        arr.splice(2,1,arr[2]+1)
      }
    }
  }
  return arr
}

M1 = makearr(M1);
M2 = makearr(M2);
M3 = makearr(M3);

outer : for(let i = 1; i <=10 ; i++){
  for(let j = 1; j <= 10; j++){
    for(let k = 1; k <= 10; k++){
      if(M1[0]*i + M2[0]*j === M3[0]*k && M1[1]*i + M2[1]*j === M3[1]*k && M1[2]*i + M2[2]*j === M3[2]*k){
        var I = i;
        var J = j;
        var K = k;
        break outer
      }
    }
  }
}
if(I !== undefined || J !== undefined || K !== undefined){
  console.log(I,J,K)
}else{
  console.log('NEMOGUCE')
}