#!/usr/bin/node
// Prints all characters from a Star Wars movie
const request = require('request');

// Extract script arguments
if (process.argv.length < 3) {
  console.log(`Usage: ${process.argv[1]} <movie-id>`);
  process.exit(1);
}

// Extract movie ID
const movieID = parseInt(process.argv[2]);
if (!Number.isInteger(movieID)) {
  console.log(`Invalid movie ID: ${process.argv[2]}`);
  process.exit(1);
}

// Function to fetch data from API
const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200) {
        resolve(JSON.parse(body));
      } else {
        reject(Error(response.statusCode));
      }
    });
  }
  );
};

// Main function
const main = async () => {
  try {
    const movie = await fetchData(`https://swapi-api.alx-tools.com/api/films/${movieID}`);
    const characterURLs = movie.characters;

    // Fetch data from URLs concurrently
    const characters = await Promise.all(characterURLs.map(fetchData));

    // Print data from results
    characters.forEach((data) => console.log(data.name));
  } catch (error) {
    console.log(error);
  }
};

main();
