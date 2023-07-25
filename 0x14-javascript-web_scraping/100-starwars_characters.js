#!/usr/bin/node
const request = require('request');
function getCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      characters.forEach(function (characterUrl) {
        request(characterUrl, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          } else {
            console.log('Error fetching character data:', error);
          }
        });
      });
    } else {
      console.log('Error fetching movie data:', error);
    }
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as the first argument.');
} else {
  getCharacters(movieId);
}
