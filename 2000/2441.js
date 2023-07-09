const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString();

var a = parseInt(input);
for (let i = 0; i < a; i++){
  blank = i
  star = a-i
  console.log(' '.repeat(blank)+'*'.repeat(star))
}

