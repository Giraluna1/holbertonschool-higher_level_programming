#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const WedgeAntilles = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    let count = 0;
    for (ch of characters) {
      if (ch == WedgeAntilles) {
        request(WedgeAntilles, function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            const films = JSON.parse(body).films;
            for (film in films) {
              count += 1;
            }
          }
        });
      }
    }
    console.log(count);
  }
});
