#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const response = {};
    const users = JSON.parse(body);
    for (const task of users) {
      if (task.completed) {
        if (!response[task.userId]) {
          response[task.userId] = 1;
        } else {
          response[task.userId] += 1;
        }
      }
    }
    console.log(response);
  }
});
