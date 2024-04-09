#!/usr/bin/node
function CustomFun () {
  const x = parseInt(process.argv[2], 10);
  if (isNaN(x) || x === undefined) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
CustomFun();
