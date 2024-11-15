#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const charcters = JSON.parse(body).charcters;
  exactOrder(charcters, 0);
});

const exactOrder = (charcters, i) => {
  if (i === charcters.length) return;
  request(charcters[i], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(charcters, i + 1);
  });
};
