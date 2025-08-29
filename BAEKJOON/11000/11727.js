const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

const n = parseInt(input);
if (n === 1){
  console.log(1)
}else{
  let arr = [1, 3];
  for (let i = 2; i < n; i++){
    let tiles = ((arr[i-2]*2) + (arr[i-1])) % 10007
    arr.push(tiles)
  }
  let result = arr[arr.length - 1];
  console.log(result)
}
