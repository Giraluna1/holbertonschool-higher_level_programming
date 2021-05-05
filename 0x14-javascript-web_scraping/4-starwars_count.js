#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const WedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const result of results) {
      for (const character of result.characters) {
        if (character.includes(WedgeAntilles)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
