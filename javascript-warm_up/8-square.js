#!/usr/bin/node
const X = parseInt(process.argv[2]);
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < X; i++) {
    console.log('X'.repeat(X));
  }
}
