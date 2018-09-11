var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  //res.render('index', { title: 'Express' });

  var fs = require('fs');
  var obj = JSON.parse(fs.readFileSync('E:/Works/2018B/LinearRegressionTechnicalAnalyService/LinearRegressionService/routes/file', 'utf8'));

  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(obj));

});

module.exports = router;
