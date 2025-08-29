const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0]);
let Pi = input[1].split(' ').map((ele)=> {return parseInt(ele)});

if(N === 0){
  console.log(0);
}else{
  let maxstart = 0;
  let maxend = 0;
  let max = 0;
  let rivalstart = 0;
  let rivalend = 0;
  let rival = 0;
  for (let i = 1; i < Pi.length; i++){
    if(Pi[i-1] < Pi[i]){
      if(maxend === i-1){
        maxend = i;
        max = Pi[maxend] - Pi[maxstart];
      }else if(rivalend === i-1){
        rivalend = i;
        rival = Pi[rivalend] - Pi[rivalstart]
        if(rival > max){
          maxstart = rivalstart;
          maxend = rivalend;
          max = rival
        }
      }
    }else{
      rivalstart = i;
      rivalend = i;
      rival = 0
    }
  }
  console.log(max)
}
