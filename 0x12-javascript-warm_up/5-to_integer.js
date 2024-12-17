#!/usr/bin/node
const firstArg = process.argv[2];
const convertedNum = parseInt(firstArg);

console.log(convertedNum ? `My number: ${convertedNum}` : 'Not a number');
