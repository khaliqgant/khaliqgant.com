/* jshint -W097 */
/* jshint node: true */
/* global document */
/* global JSONEditor */
'use strict';


/* Dependencies ------------------------------------------------------------ */
/**
 * @desc binds JSONEditor to the window
 * @requires json-editor
 */
require('json-editor');
var Selectors = require('./selectors');

/**
 * Schemas
 * @desc grab all the workout JSON schemas from the workout-tracker directory
 * @type array
 */
var Schemas = requireAll(
    require.context('json!workout-tracker/workouts', true, /^\.\/.*\.json$/)
);


/* App --------------------------------------------------------------------- */
loadSchemas();


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
 * Load Schemas
 * @desc iterate through each workout and load it in using JSONEditor with
 *       configuration options
 */
function loadSchemas() {
    var editor,
        el = document.getElementById('editor');

    for (var i = 0; i < Schemas.length; i++)
    {
        editor = new JSONEditor(el, {
            ajax: true,
            theme: 'bootstrap2',
            collapsed: true,
            schema: Schemas[i]
        });
    }
}
