/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

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
	    __webpack_require__(1)
	);

	console.log(Schemas);



/***/ },
/* 1 */
/***/ function(module, exports, __webpack_require__) {

	var map = {
		"./mens_health.json": 2,
		"./total_body_pull.json": 3,
		"./upper_body_push.json": 4
	};
	function webpackContext(req) {
		return __webpack_require__(webpackContextResolve(req));
	};
	function webpackContextResolve(req) {
		return map[req] || (function() { throw new Error("Cannot find module '" + req + "'.") }());
	};
	webpackContext.keys = function webpackContextKeys() {
		return Object.keys(map);
	};
	webpackContext.resolve = webpackContextResolve;
	module.exports = webpackContext;
	webpackContext.id = 1;


/***/ },
/* 2 */
/***/ function(module, exports) {

	module.exports = {
		"$schema": "http://json-schema.org/draft-04/schema#",
		"id": "/mens_health.json",
		"type": "object",
		"required": [
			"title",
			"source",
			"exercises"
		]
	};

/***/ },
/* 3 */
/***/ function(module, exports) {

	module.exports = {
		"title": "Total-Body Pull",
		"$schema": "http://json-schema.org/draft-04/schema#",
		"allOf": [
			{
				"$ref": "/schema/mens_health.json"
			},
			{
				"properties": {
					"title": {
						"type": "string",
						"default": "Total-Body Pull"
					},
					"source": {
						"type": "string",
						"default": "http://www.menshealth.com/fitness/saturday-workout-total-body"
					},
					"exercises": {
						"type": "array",
						"uniqueItems": true,
						"items": {
							"type": "object",
							"properties": {
								"name": {
									"type": "string",
									"enum": [
										"Cliffhanger Challenge: Chinups and Hangs",
										"Foot-Elevated Single-Leg Hip Thrust",
										"Tempo Dumbbell Biceps Curl",
										"Dumbbell Farmer’s Walk"
									]
								},
								"weight": {
									"type": "integer"
								},
								"reps": {
									"type": "integer"
								},
								"time": {
									"type": "string"
								},
								"notes": {
									"type": "string"
								}
							},
							"required": [
								"name",
								"weight",
								"time",
								"notes"
							]
						}
					}
				}
			}
		]
	};

/***/ },
/* 4 */
/***/ function(module, exports) {

	module.exports = {
		"title": "Upper Body Push",
		"$schema": "http://json-schema.org/draft-04/schema#",
		"allOf": [
			{
				"$ref": "/schema/mens_health.json"
			},
			{
				"properties": {
					"title": {
						"type": "string",
						"default": "Upper Body Push"
					},
					"source": {
						"type": "string",
						"default": "http://www.menshealth.com/fitness/tuesday-workout-upper-body"
					},
					"exercises": {
						"type": "array",
						"uniqueItems": true,
						"items": {
							"type": "object",
							"properties": {
								"name": {
									"type": "string",
									"enum": [
										"Barbel Pause Bench Press",
										"Dumbbell Single-Arm Overhead Press",
										"Tempo Pushup",
										"Bear Crawl"
									]
								},
								"weight": {
									"type": "integer"
								},
								"reps": {
									"type": "integer"
								},
								"time": {
									"type": "string"
								},
								"notes": {
									"type": "string"
								}
							},
							"required": [
								"name",
								"weight",
								"time",
								"notes"
							]
						}
					}
				}
			}
		]
	};

/***/ }
/******/ ]);