#!/usr/bin/node
const https = require('https');

const url = process.argv[2];

const req = https.request(url, res => {
  console.log(`statusCode: ${res.statusCode}`);

  res.on('data', d => {
    process.stdout.write(d);
  });
});

req.on('error', error => {
  console.error(error);
});

req.end();
