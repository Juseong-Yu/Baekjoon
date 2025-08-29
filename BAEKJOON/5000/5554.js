const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n')

let added = parseInt(input[0]) +parseInt(input[1]) + parseInt(input[2]) + parseInt(input[3]);
let hour  = Math.floor(added / 60);
let min = added % 60;

console.log(hour);
console.log(min);