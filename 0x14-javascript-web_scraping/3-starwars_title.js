#!/usr/bin/node
const request = require('request');
const episode = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + episode[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
