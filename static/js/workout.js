'use strict';

/**
 * Require All
 * @use grab all the files within a directory
 * HT: https://webpack.github.io/docs/context.html#context-module-api
 */
function requireAll(requireContext) {
  return requireContext.keys().map(requireContext);
}

var Schemas = requireAll(
    require.context('json!workout-tracker/schema', true, /^\.\/.*\.json$/)
);

console.log(Schemas);

