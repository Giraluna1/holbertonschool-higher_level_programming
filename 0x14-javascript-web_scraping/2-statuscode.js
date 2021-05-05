#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, res) {
  if (error) {
    console.error(`error: ${error}`);
  } else {
    console.log(`code: ${res.statusCode}`);
  }
});
