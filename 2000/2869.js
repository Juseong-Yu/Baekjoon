const { count } = require('console');
const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split(' ')

let A = parseInt(input[0]);
let B = parseInt(input[1]);
let V = parseInt(input[2]);

let day = 0;
let reach = 0;

// while(true){
//   day++;
//   reach += A;
//   if (reach >= V){
//     break
//   }else{
//     reach -= B;
//   }
// }

day = Math.ceil((V-A) / (A-B)) + 1
console.log(day)