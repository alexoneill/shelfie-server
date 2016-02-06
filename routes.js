// routes.js
// aoneill - 10/10/15

// Modules
var path = require('path'),
    apn = require('apn'),
    mongodb = require('mongodb');
    exec = require('child_process').exec;

// App-scheme specific logic
var appName = path.basename(__dirname);
var _parent = path.join(__dirname, '..');
var apps = require(path.join(_parent, 'app.js'));
var route = apps.routeGen(appName);
var view = apps.viewGen(appName);

// Paths
var _assets = path.join(__dirname, 'assets');
var _ssl = path.join(_assets, 'ssl');

module.exports.load = function(server, app) {
  // Fancy, user-facing home page
  server.get(route('/'), function(req, res) {
    res.render(view('home'), {
      root: apps.getRoot(appName)
    });
  });

  // ------ API -------

  server.post(route('/upload'), function(req, res, next) {
    res.json(req.files);
  });

  server.post(route('/suggest'), function(req, res, next) {
    var books = req.body.books;

    var python = '/usr/bin/python2.7'
    var script = path.join(__dirname, 'scripts', 'suggest.py');
    var params = '"' + books.join('" "') + '"';
    exec([python, script, params].join(' '), 
        function callback(error, stdout, stderr) {
          req.write(stdout);
    });
  });
}
