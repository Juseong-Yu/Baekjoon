const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

let L = parseInt(input);
console.log(L-543)