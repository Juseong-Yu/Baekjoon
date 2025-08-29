arr = []
for i in range(9):
  tmp = int(input())
  arr.append(tmp)
arr.sort()
overall = sum(arr)
notlittle = []
for i in range(1,9):
  for j in range(0,i):
    if(overall - arr[i] -arr[j] == 100):
      notlittle = [arr[i],arr[j]]

for k in range(0,9):
  if arr[k] not in notlittle:
    print(arr[k])

# const { count } = require('console');
# const fs = require('fs');
# const { parse } = require('path');
# const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
# let input = fs.readFileSync(path).toString().split('\n');

# let arr = input.map(ele => parseInt(ele));
# const overall = arr.reduce((acc, cur)=> acc+cur);
# arr.sort((a,b) => a-b);

# let notlittle = []
# for(let i = 1; i < arr.length; i++){
#   for(let n = 0; n < i; n++){
#     if(overall - arr[i] -arr[n] === 100){
#       notlittle = [arr[i],arr[n]];
#     }
#   }

# }
# let little = []
# for(let k = 0; k < arr.length; k++){
#   if(!(notlittle.includes(arr[k]))){
#     little.push(arr[k])
#   }
# }
# console.log(little[0]+'\n'+little[1]+'\n'+little[2]+'\n'+little[3]+'\n'+little[4]+'\n'+little[5]+'\n'+little[6])