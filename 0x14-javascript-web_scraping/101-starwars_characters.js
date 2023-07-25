#!/usr/bin/node
const request = require('request');
function getCharactersByMovieId(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const charactersUrls = filmData.characters;

      // Fetch the characters' data from their URLs
      charactersUrls.forEach((characterUrl) => {
        request(characterUrl, (error, response, characterBody) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
          } else {
            console.error(`Error fetching character data: ${error}`);
          }
        });
      });
    } else {
      console.error(`Error fetching film data: ${error}`);
    }
  });
}

// Get the movie ID from command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error("Please provide a movie ID as an argument.");
} else {
  getCharactersByMovieId(movieId);
}
