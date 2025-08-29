const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().trim().split('\n');

const N = parseInt(input[0]);
let nums = input[1].split(' ').map(ele => {return parseInt(ele)})
let counts = input[2].split(' ').map(ele => {return parseInt(ele)})
counts_filter = [];
function countermaker(ele){
  if(ele === 0){
    counts_filter.push('+');
  }else if(ele === 1){
    counts_filter.push('-');
  }else if(ele === 2){
    counts_filter.push('*');
  }else if(ele === 3){
    counts_filter.push('/');
  }
}
for(let i = 0; i < counts.length; i++){
  for(let count=0; count<counts[i]; count++){
    countermaker(i)
  }
}
let results = []
function next(result, arr, place){
  if(place === N){
    results.push(result)
  }else{
    for(let i = 0; i < arr.length; i++){
    if(arr[i] === '+'){
      resultc = result + nums[place]
    }else if(arr[i] === '-'){
      resultc = result - nums[place]
    }else if(arr[i] === '*'){
      resultc = result * nums[place]
    }else if(arr[i] === '/'){
      resultc = Math.trunc(result / nums[place])
    }
    let arrtmp = arr.slice();
    arrtmp.splice(i,1)
    next(resultc, arrtmp, place+1)
  }
  }
}

next(nums[0], counts_filter, 1);
if(Math.max(...results) === -0 || Math.max(...results) === +0){
  console.log(0)
}else{
  console.log(Math.max(...results))
}
if(Math.min(...results) === -0|| Math.min(...results) === +0){
  console.log(0)
}else{
  console.log(Math.min(...results))
}