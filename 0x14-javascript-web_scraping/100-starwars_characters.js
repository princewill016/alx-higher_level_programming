#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const movie = JSON.parse(body);
  movie.characters.forEach(characterUrl => {
    request(characterUrl, (err, response, body) => {
      if (!err) {
        console.log(JSON.parse(body).name);
      }
    });
  });
});
