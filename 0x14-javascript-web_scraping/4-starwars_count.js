#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const films = JSON.parse(body).results;
  const count = films.reduce((acc, film) => {
    return acc + (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/') ? 1 : 0);
  }, 0);
  console.log(count);
});
