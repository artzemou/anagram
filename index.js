const express = require('express')
const {PythonShell} = require('python-shell')
const PORT = process.env.PORT || 5000
const bodyParser = require('body-parser')
const ejs = require('ejs')
const chalk = require('chalk')
require('dotenv').config()

const app = express()


app.set('view engine', 'ejs')
  .use('/py', express.static(__dirname + '/py'))
  .use(bodyParser.urlencoded({extended: true}))
  .use(bodyParser.json())
  .post('/', function(req, res) { 
    PythonShell.run('py/anagram.py', {args:[req.body.str]}, function (err, results) {
      if (err) throw err;
      if (results[0] === '[]') results[0] = '["oops"]'
      res.json(results[0]);
    });
    
  })
  .get('/*', function(req, res) {
    res.render('index')
  })
  
  .listen(PORT, () => console.log(chalk`🚀  {green Listening on http://localhost:${PORT}}`))
