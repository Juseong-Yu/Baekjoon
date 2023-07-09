const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(" ");

var a = parseInt(input[0]);
var b = parseInt(input[1]);
var c = parseInt(input[2]);

let counter = {}
for (let i = 1; i <= a; i++){
  for (let j = 1; j <= b; j++){
    for (let k = 1; k <= c; k++){
      result = i + j + k
      if (String(result)in counter){
        counter[result] = counter[result]+1
      }else {
        counter[result] = 1
      }
    }
  }
}
console.log(counter)
let maxKey = null;
let maxvalue = 0;
for (const key in counter){
  if (counter[key] > maxvalue){
    maxKey = key
    maxvalue = counter[key]
  }
}
console.log(maxKey)