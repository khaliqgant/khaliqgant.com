/* jshint -W097 */
/* jshint node: true */
/* global document */
/* global window */
/* global JSONEditor */
'use strict';

/* Dependencies ------------------------------------------------------------ */
/**
 * @desc binds JSONEditor to the application scope
 * @requires json-editor
 */

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _react = require('react');

var _react2 = _interopRequireDefault(_react);

var _reactDom = require('react-dom');

var _reactDom2 = _interopRequireDefault(_reactDom);

var _superagent = require('superagent');

var _superagent2 = _interopRequireDefault(_superagent);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

require('json-editor');
var Selectors = require('./selectors');
var workoutsTemplate = require('handlebars!../templates/workouts.html');
var editor;
/**
 * Superagent
 * @see https://github.com/visionmedia/superagent
 */


/*
 * Resources:
 * https://facebook.github.io/react/docs/package-management.html
 * https://github.com/yuanyan/react-ajax
 * http://survivejs.com/webpack_react/webpack_and_react/
 * https://blog.risingstack.com/using-react-with-webpack-tutorial/
 * https://www.twilio.com/blog/2015/08/setting-up-react-for-es6-with-webpack-and-babel-2.html
 * http://www.zev23.com/2014/04/use-gruntjs-to-uglify-es6-application.html
 */

/**
 * Schemas
 * @desc grab all the workout JSON schemas from the workout-tracker directory
 * @type array
 */
var Schemas = requireAll(require.context('json!workout-tracker/workouts', true, /^\.\/.*\.json$/));

/* App --------------------------------------------------------------------- */
var param = getParameterByName('workout');
// this is useful: http://ricostacruz.com/cheatsheets/react.html

if (param === null) {
    renderListHtml();
    loadHtml();
} else {
    loadSchema(param);
    renderWorkoutHtml();
}

// Listeners

var SaveButton = function (_React$Component) {
    _inherits(SaveButton, _React$Component);

    function SaveButton() {
        _classCallCheck(this, SaveButton);

        var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(SaveButton).call(this));

        _this.state = {
            saved: false
        };
        _this.handleClick = _this.handleClick.bind(_this);
        return _this;
    }

    _createClass(SaveButton, [{
        key: 'handleClick',
        value: function handleClick() {
            var json = editor.getValue();
            json.date = new Date();
            json.name = document.getElementById(Selectors.check).value;
            var token = document.getElementById('editor').dataset.token;
            _superagent2.default.post('/api/workout').set('X-CSRFTOKEN', token).send(json).end(function (err, res) {
                console.log(res);
            });

            this.setState({
                saved: !this.state.saved
            });
        }
    }, {
        key: 'render',
        value: function render() {
            var text = this.state.saved ? 'Saved' : 'Save';
            return _react2.default.createElement(
                'div',
                { onClick: this.handleClick },
                text
            );
        }
    }]);

    return SaveButton;
}(_react2.default.Component);

_reactDom2.default.render(_react2.default.createElement(SaveButton, null), document.getElementById(Selectors.save));

/* Utils ------------------------------------------------------------------- */
/**
 * Require All
 * @desc grab all the files within a directory
 * @see https://webpack.github.io/docs/context.html#context-module-api
 */
function requireAll(requireContext) {
    return requireContext.keys().map(requireContext);
}

/**
 * Load Html
 * @desc append compiled html workouts to the DOM
 */
function loadHtml() {
    var workoutsHtml,
        li,
        ul = document.getElementsByClassName(Selectors.workouts)[0];
    for (var i = 0; i < Schemas.length; i++) {
        workoutsHtml = workoutsTemplate(Schemas[i]);
        ul.insertAdjacentHTML('beforeend', workoutsHtml);
    }
}

/**
 * Load Schema
 * @desc iterate through the schemas and load in the passed param using
 *       JSONEditor with configuration options
 * @param {string} param
 */
function loadSchema(param) {
    var el = document.getElementById('editor');

    for (var i = 0; i < Schemas.length; i++) {
        if (Schemas[i].id === param) {
            editor = new JSONEditor(el, {
                ajax: true,
                theme: 'bootstrap2',
                collapsed: true,
                schema: Schemas[i]
            });
        }
    }
}

/**
 * Render List Html
 * @desc add in the list specific header for a workout
 */
function renderListHtml() {
    var Header = _react2.default.createClass({
        displayName: 'Header',

        render: function render() {
            return _react2.default.createElement(
                'h2',
                null,
                'Workouts(',
                this.props.count,
                ')'
            );
        }
    });

    _reactDom2.default.render(_react2.default.createElement(Header, { count: Schemas.length }), document.getElementById(Selectors.header));
}

/**
 * Render Workout Html
 * @desc add in the specific workout DOM elements
 */
function renderWorkoutHtml() {
    var Save = _react2.default.createClass({
        displayName: 'Save',

        render: function render() {
            return _react2.default.createElement(
                'button',
                { type: 'button', id: 'js-save', className: 'btn btn-danger' },
                'Save'
            );
        }
    });
    var Header = _react2.default.createClass({
        displayName: 'Header',

        render: function render() {
            return _react2.default.createElement(
                'a',
                { href: '/apps/workout-tracker' },
                'Back'
            );
        }
    });
    var Check = _react2.default.createClass({
        displayName: 'Check',

        render: function render() {
            return _react2.default.createElement('input', { id: 'js-check', placeholder: 'Name' });
        }
    });
    _reactDom2.default.render(_react2.default.createElement(Header, null), document.getElementById(Selectors.header));
    _reactDom2.default.render(_react2.default.createElement(Save, null), document.getElementById(Selectors.saveContainer));
    _reactDom2.default.render(_react2.default.createElement(Check, null), document.getElementById(Selectors.checker));
}

function getParameterByName(name, url) {
    if (!url) {
        url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) {
        return null;
    }
    if (!results[2]) {
        return '';
    }

    var query = decodeURIComponent(results[2].replace(/\+/g, ' ').replace(/\//g, ''));
    return query;
}
