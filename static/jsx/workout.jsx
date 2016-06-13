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
require('json-editor');
var Selectors = require('./selectors');
var workoutsTemplate = require('handlebars!../templates/workouts.html');
var editor;

import React from 'react';
import ReactDom from 'react-dom';
/**
 * Superagent
 * @see https://github.com/visionmedia/superagent
 */
import request from 'superagent';


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
var Schemas = requireAll(
    require.context('json!workout-tracker/workouts', true, /^\.\/.*\.json$/)
);


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
class SaveButton extends React.Component {
    constructor() {
        super();
        this.state = {
            saved: false
        };
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick() {
        var json = editor.getValue();
        json.date = new Date();
        json.name = document.getElementById(Selectors.check).value;
        var token = document.getElementById('editor').dataset.token;
        request
            .post('/api/workout')
            .set('X-CSRFTOKEN', token)
            .send(json)
            .end(function (err, res) {
                console.log(res);
            });

        this.setState({
            saved: !this.state.saved
        });
    }

    render() {
        const text = this.state.saved ? 'Saved' : 'Save';
        return (
            <div onClick={this.handleClick}>
            {text}
            </div>
        );
    }
}

ReactDom.render(
    <SaveButton />,
    document.getElementById(Selectors.save)
);


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
    var workoutsHtml, li,
        ul = document.getElementsByClassName(Selectors.workouts)[0];
    for (var i = 0; i < Schemas.length; i++)
    {
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

    for (var i = 0; i < Schemas.length; i++)
    {
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
function renderListHtml()
{
    var Header = React.createClass({
        render: function() {
            return (
                <h2>Workouts({this.props.count})</h2>
            )
        }
    });

    ReactDom.render(<Header count={Schemas.length} />, document.getElementById(Selectors.header));
}

/**
 * Render Workout Html
 * @desc add in the specific workout DOM elements
 */
function renderWorkoutHtml()
{
    var Save = React.createClass({
        render: function() {
            return (
                <button type="button" id="js-save" className="btn btn-danger">Save</button>
            )
        }
    });
    var Header = React.createClass({
        render: function() {
            return (
                <a href="/apps/workout-tracker">Back</a>
            )
        }
    });
    var Check = React.createClass({
        render: function() {
            return (
                <input id="js-check" placeholder="Name" />
            )
        }
    });
    ReactDom.render(<Header/>, document.getElementById(Selectors.header));
    ReactDom.render(<Save />, document.getElementById(Selectors.saveContainer));
    ReactDom.render(<Check />, document.getElementById(Selectors.checker));
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

        var query = decodeURIComponent(results[2].replace(/\+/g, ' ')
                                    .replace(/\//g, ''));
        return query;
}
