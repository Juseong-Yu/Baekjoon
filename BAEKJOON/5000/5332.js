const { count } = require('console');
const fs = require('fs');
const { parse } = require('path');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');
const L = parseInt(input[0]);
const A = parseInt(input[1]);
const B = parseInt(input[2]);
const C = parseInt(input[3]);
const D = parseInt(input[4]);

const korean = Math.ceil(A / C);
const math = Math.ceil(B/D);

const doh = Math.max(korean,math);
console.log(L-doh)