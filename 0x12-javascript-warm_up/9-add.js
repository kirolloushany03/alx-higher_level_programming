#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstInteger = parseInt(process.argv[2], 10);
const secondInteger = parseInt(process.argv[3], 10);

if (isNaN(firstInteger) || isNaN(secondInteger)) {
  console.log('NaN');
} else {
  const result = add(firstInteger, secondInteger);
  console.log(result);
}
