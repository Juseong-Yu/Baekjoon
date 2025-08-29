const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

let S = input[1].trim().split(' ').map(ele => {return parseInt(ele)});
let R = input[2].trim().split(' ').map(ele => {return parseInt(ele)});

filterS = S.filter(ele => !R.includes(ele));
filterR = R.filter(ele => !S.includes(ele));

let bor = [];
for(let i = 0; i < filterS.length; i++){
  if(filterR.includes(filterS[i]-1) || filterR.includes(filterS[i]+1)){
    bor.push(filterS[i])
    let idx = filterR.indexOf(filterS[i]);
    filterR.splice(idx,1)
  }
}
if(filterS.length - bor.length >= 0){
  console.log(filterS.length - bor.length)
}else{
  console.log(0)
}