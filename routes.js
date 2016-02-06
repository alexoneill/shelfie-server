// routes.js
// aoneill - 10/10/15

// Modules
var path = require('path'),
    apn = require('apn'),
    mongodb = require('mongodb');

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
    res.render(view('home'));
  });

  // ------ API -------

  server.post(route('/upload'), function(req, res, next) {
  });
}
