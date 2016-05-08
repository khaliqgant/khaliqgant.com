'use strict';

/**
 * Require All
 * @desc grab all the files within a directory
 * @see https://webpack.github.io/docs/context.html#context-module-api
 */
function requireAll(requireContext) {
  return requireContext.keys().map(requireContext);
}

var Schemas = requireAll(
    require.context('json!workout-tracker/schema', true, /^\.\/.*\.json$/)
);

console.log(Schemas);

