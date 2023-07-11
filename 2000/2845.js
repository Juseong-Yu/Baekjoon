const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

let L = parseInt(input[0].split(' ')[0]);
let P = parseInt(input[0].split(' ')[1]);
let news = input[1].split(' ');
for(let i = 0; i < news.length; i++){
  console.log(news[i] - (L*P));
}
console.log(news)
