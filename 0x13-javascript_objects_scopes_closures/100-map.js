#!/usr/bin/node
const list = require('./100-data.js').list
console.log(list)
const mapList = list.map((item, index) => item * index)
console.log(mapList)
