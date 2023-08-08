const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

let N = parseInt(input);
let Nlength = input.length;
let result = 0;
while(Nlength > 0){
  result += (N - Math.pow(10,Nlength-1)+1) * Nlength;
  N = Math.pow(10,Nlength-1)-1;
  Nlength-- ;
}

console.log(String(result));