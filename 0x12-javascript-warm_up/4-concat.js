#!/usr/bin/node
const firstArg = process.argv[2];
const secondArg = process.argv[3];

if (firstArg && secondArg) {
  console.log(`${firstArg} is ${secondArg}`);
}
