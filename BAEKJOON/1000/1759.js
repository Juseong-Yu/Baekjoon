const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n')
const firstrow = input[0].split(' ');
const L = parseInt(firstrow[0]);
const C = parseInt(firstrow[1]);
const letter = input[1].split(' ');
let arr = [];

letter.sort();
for(let i = 0; i < C-L+1; i++){
  arr.push([letter[i]])
}

for(let n = 1; n < L; n++){
  let tmparr = [];
  
  for(let k = 0; k < arr.length; k++){
    for (let m = letter.indexOf(arr[k][arr[k].length-1])+1; m < letter.length; m++){
      if(!arr[k].includes(letter[m])){
        let tmp = arr[k].slice()
        tmp.push(letter[m])
        tmparr.push(tmp)
      }
    }
  }
  arr = tmparr
}

for (let idx = 0; idx < arr.length; idx++){
  let count = 0;
  if(arr[idx].includes('a')){
    count++
  }
  if(arr[idx].includes('e')){
    count++
  }
  if(arr[idx].includes('i')){
    count++
  }
  if(arr[idx].includes('o')){
    count++
  }
  if(arr[idx].includes('u')){
    count++
  }
  if(count >= 1 && count <= L-2){
    console.log(arr[idx].join(''))
  }
}