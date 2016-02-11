// routes.js
// aoneill - 10/10/15

// Modules
var path = require('path'),
    apn = require('apn'),
    mongodb = require('mongodb');
    exec = require('child_process').exec;

module.exports.load = function(server, app) {
  // Fancy, user-facing home page
  server.get(app.route('/'), function(req, res) {
    res.render(app.view('home'), {
      root: app.util.getRoot(app.name)
    });
  });

  // ------ API -------

  /*server.post(route('/upload'), function(req, res, next) {
    res.json(req.files);
  });*/

  server.post(app.route('/suggest'), function(req, res, next) {
    var books = req.body.books;

    var python = '/usr/bin/python2.7'
    var script = path.join(__dirname, 'scripts', 'suggest.py');
    var params = '"' + books.join('" "') + '"';
    exec([python, script, params].join(' '), 
        function callback(error, stdout, stderr) {
          res.json(JSON.parse(stdout));
    });
  });
}
