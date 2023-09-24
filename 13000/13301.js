const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString()

const N = parseInt(input);

let arr = ['1','1'];

function adder(a,b){
  let carry = 0;
  let result = '';
  for (let i = a.length - 1, j = b.length - 1; i >= 0 || j >= 0 || carry; i--, j--) {
    const digitA = i >= 0 ? parseInt(a[i]) : 0;
    const digitB = j >= 0 ? parseInt(b[j]) : 0;
    const sum = digitA + digitB + carry;
    result = (sum % 10) + result;
    carry = sum >= 10 ? 1 : 0;
  }
  return result
}

if(N === 1){
  console.log(4);
}else if(N === 2){
  console.log(6);
}else{
  for(let i = 2; i < N; i++){
    arr.push(adder(arr[i-1],arr[i-2]))
  }
  let long = arr.pop();
  let short = arr.pop();
  let result = adder(long,adder(long,adder(long,adder(long,adder(short,short)))))
  console.log(result)
}
