#!/usr/bin/node
const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request);
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

async function getCharactersInRightOrder (url) {
  try {
    const response = await requestPromise(url);
    const chars = JSON.parse(response.body).characters;
    for (let i = 0; i < chars.length; ++i) {
      const charResponse = await requestPromise(chars[i]);
      console.log(JSON.parse(charResponse.body).name);
    }
  } catch (err) {
    console.log(err);
  }
}

getCharactersInRightOrder(url);
