#!/usr/bin/node
const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);

async function getCharacterName(url) {
  try {
    const response = await requestPromise(url);
    return JSON.parse(response.body).name;
  } catch (err) {
    return null;
  }
}

async function printCharacters(movieId) {
  try {
    const response = await requestPromise(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const movie = JSON.parse(response.body);
    const characters = await Promise.all(
      movie.characters.map(url => getCharacterName(url))
    );
    characters.forEach(name => {
      if (name) console.log(name);
    });
  } catch (err) {
    console.log(err);
  }
}

printCharacters(process.argv[2]);
