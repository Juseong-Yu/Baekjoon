const fs = require('fs');
const path = process.platform === 'linux' ? '/dev/stdin' : 'text.txt';
let input = fs.readFileSync(path).toString().split('\n');

const N = parseInt(input[0]);
let tree = [];
for (let i = 1; i <= N; i++) {
  tree.push(input[i].split(' '));
}

function findleftright(tree, idx) {
  let leftidx = null;
  let rightidx = null;
  for (let j = 0; j < N; j++) {
    if (tree[j][0] === tree[idx][1]) {
      leftidx = j;
    }
    if (tree[j][0] === tree[idx][2]) {
      rightidx = j;
    }
  }
  return [leftidx, rightidx];
}

function preorder(tree, idx) {
  if (idx === null) {
    return '';
  }
  const currentNode = tree[idx][0];
  const leftidx = findleftright(tree, idx)[0];
  const rightidx = findleftright(tree, idx)[1];
  return currentNode + preorder(tree, leftidx) + preorder(tree, rightidx);
}

function inorder(tree, idx) {
  if (idx === null) {
    return '';
  }
  const currentNode = tree[idx][0];
  const leftidx = findleftright(tree, idx)[0];
  const rightidx = findleftright(tree, idx)[1];
  return inorder(tree, leftidx) + currentNode + inorder(tree, rightidx);
}

function postorder(tree, idx) {
  if (idx === null) {
    return '';
  }
  const currentNode = tree[idx][0];
  const leftidx = findleftright(tree, idx)[0];
  const rightidx = findleftright(tree, idx)[1];
  return postorder(tree, leftidx) + postorder(tree, rightidx) + currentNode;
}

const preorderR = preorder(tree, 0);
const inorderR = inorder(tree, 0);
const postorderR = postorder(tree, 0);

const result = [preorderR, inorderR, postorderR].join('\n');
console.log(result);