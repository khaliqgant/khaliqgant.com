'use strict';

/* global document */
/* global JSONEditor */

require('json-editor');

var Schemas = requireAll(
    require.context('json!workout-tracker/workouts', true, /^\.\/.*\.json$/)
);

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

/* Utils -------------------------------
 *
/**
 * Require All
 * @desc grab all the files within a directory
 * @see https://webpack.github.io/docs/context.html#context-module-api
 */
function requireAll(requireContext) {
  return requireContext.keys().map(requireContext);
}
