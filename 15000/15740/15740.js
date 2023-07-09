const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'example.txt';
let input = fs.readFileSync(path).toString().split(' ');

var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a+b);