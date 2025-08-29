N = int(input())
arr = []
for i in range(N):
  tmp = float(input())
  arr.append(tmp)
dp = [arr[0]]
for j in range(1,len(arr)):
  max1 = arr[j]
  if (dp[j-1] * arr[j] > arr[j]):
    dp.append(dp[j-1] * arr[j])
  else:
    dp.append(arr[j])
print('%0.3f' % max(dp))

# const { count } = require('console');
# const fs = require('fs');
# const { parse } = require('path');
# const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
# let input = fs.readFileSync(path).toString().split('\n');

# const N = parseInt(input[0]);
# let arr = []
# for (let i = 1; i <= N; i++){
#   arr.push(parseFloat(input[i]));
# }

# let dp = [arr[0]];

# for (let j = 1; j < arr.length; j++){
#   let max = arr[j]
#   if (dp[j-1] * arr[j] > arr[j]){
#     dp.push(Math.round(dp[j-1] *arr[j]*1000)/1000);
#   }else{
#     dp.push(arr[j])
#   }
# }

# let result = Math.max(...dp);

# result = result * 1000

# result = Math.round(result)

# result = result / 1000
# console.log(result.toFixed(3))