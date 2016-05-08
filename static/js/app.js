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
	 * @desc grab all the files within a directory
	 * @see https://webpack.github.io/docs/context.html#context-module-api
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
			"workout"
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
					"workout": {
						"type": "array",
						"uniqueItems": true,
						"items": {
							"properties": {
								"Exercise": {
									"type": "string",
									"oneOf": [
										{
											"type": "string",
											"enum": [
												"Cliffhanger Challenge: Chinups and Hangs (A)",
												"Cliffhanger Challenge: Chinups and Hangs (B)"
											],
											"title": "Back",
											"description": "Find your half-max rep total. For instance, say you can do a max total of 10 chinups in a row before you can’t do anymore. That makes your half-max rep total 5 reps (10 divided by 2). If you can only do 5 total reps, your half-max total is 2 to 3. Perform your half-max rep total every minute on the minute for 10 minutes. If you complete the reps before the end of the minute, rest until the next minute begins.Hang block: You can perform this a couple of ways. Option A: Hang for as long as you can, resting only when needed. Continue for 10 minutes.Option B: Hang for 30 seconds, and then rest for 30 seconds. Repeat for 10 minutes total. Every week, add a second of work and remove a second of rest to these time periods."
										},
										{
											"enum": [
												"Foot-Elevated Single-Leg Hip Thrust"
											],
											"title": "Legs",
											"description": "Do all 10 reps on your left leg, and then rest the remainder of the minute. When the next minute begins, switch sides and do all 10 reps on your right leg. Alternate sides every minute."
										},
										{
											"enum": [
												"Tempo Dumbbell Biceps Curl"
											],
											"title": "Biceps",
											"description": "Grab a pair of 10-to-15 pound dumbbells. Do 5 rounds of the exercise. Each round is one minute long followed by a one-minute rest (10 minutes total). Follow the prescribed tempo for each round below. Try to complete as many reps in a minute that the tempo will allow.   Round 1: Eccentric (1-1-3) Lift for 1 second-pause for 1 second at the top-lower for 3 seconds  Round 2: Isometric (1-3-1) Lift for 1 second-lower the weights until your elbows are bent at 90 degrees, and then pause for 3 seconds—lower the rest of the way for 1 second  Round 3: Concentric (3-1-1) Lift for 3 seconds-pause for 1 second at the top-lower for 1 second  Round 4: Continuous Lift for 2 seconds and lower for 2 seconds without pausing at the bottom or top  Round 5: Max Iso  Lift the weights until your elbows are bent to 90 degrees. Now hold this position for a minute or for as long as possible."
										},
										{
											"enum": [
												"Dumbbell Farmer’s Walk"
											],
											"title": "Full Body",
											"description": "Grab a pair of dumbbells that's about 25 percent of your body weight, and hold them at your sides. Walk for 10 minutes. You can perform this a few different ways:  Option A: Walk for 10 minutes, only resting when needed.  Option B: Walk with one dumbbell in your right hand for one minute. Switch hands, and walk for one minute. Alternate sides for 10 minutes straight.   Option C: Perform 30 seconds of walking followed by 30 seconds of rest for 10 minutes straight. Every week, add a second of work and remove a second of rest to these time periods."
										}
									]
								},
								"weight": {
									"type": "integer",
									"title": "Weight"
								},
								"reps": {
									"type": "integer",
									"title": "Reps"
								},
								"time": {
									"type": "string",
									"title": "Time",
									"default": "10 minutes"
								},
								"notes": {
									"type": "string",
									"title": "Notes",
									"description": "Any notes about the exercise"
								}
							}
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
					"workout": {
						"type": "array",
						"items": {
							"properties": {
								"Exercise": {
									"type": "string",
									"oneOf": [
										{
											"type": "string",
											"enum": [
												"Barbel Pause Bench Press"
											],
											"title": "Chest",
											"description": "Choose a load that you can press for about 6 to 8 repetitions max. Then perform 2 to 3 reps every minute on the minute (EMOM) for 20 minutes straight. If you complete the reps before the end of the minute, rest until the next minute begins. Once you can do 3 reps EMOM for 20 minutes straight, increase the load by 5 pounds or 5 percent."
										},
										{
											"enum": [
												"Dumbbell Single-Arm Overhead Press"
											],
											"title": "Shoulders",
											"description": "Grab a 20- to 25-pound dumbbell. Perform 10 reps EMOM for 10 minutes. Do all 10 reps on your left side, and then rest the remainder of the minute. When the next minute begins, switch arms and do all 10 reps on your right side. Alternate sides every minute.Once you can do 10 reps per side for 10 minutes straight, increase the load by 5 pounds."
										},
										{
											"enum": [
												"Tempo Pushup"
											],
											"title": "Upper Body",
											"description": "Do 5 rounds of the pushup. Each round is one minute long followed by a one-minute rest (10 minutes total). Follow the prescribed tempo for each round below. Try to complete as many reps in a minute that the tempo will allow. Round 1: Eccentric (3-1-1)Lower for 3 seconds-pause for 1 second at the bottom-lift for 1 second. Round 2: Isometric (1-3-1). Lower for 1 second-pause for 3 seconds at the bottom-lift for 1 second. Round 3: Concentric (1-1-3). Lower for 1 second-pause for 1 second at the bottom-lift for 3 seconds. Round 4: Continuous Lower for 2 seconds and lift for 2 seconds without pausing at the bottom or top. Round 5: Max IsoLower down into the bottom of a pushup so your chest hovers just above the floor. Now hold this position for a minute or for as long as possible."
										},
										{
											"enum": [
												"Bear Crawl (A)",
												"Bear Crawl (B)"
											],
											"title": "Full Body",
											"description": "Do a bear crawl for 10 minutes. You can perform this a couple of different ways:Option A: Do it for 10 minutes straight, only resting when needed.Option B: Perform 30 seconds of work followed by 30 seconds of rest. Every week, add a second of work and remove a second of rest to these time periods."
										}
									]
								},
								"weight": {
									"type": "integer",
									"title": "Weight"
								},
								"reps": {
									"type": "integer",
									"title": "Reps"
								},
								"time": {
									"type": "string",
									"title": "Time",
									"default": "10 minutes"
								},
								"notes": {
									"type": "string",
									"title": "Notes",
									"description": "Any notes about the exercise"
								}
							}
						}
					}
				}
			}
		]
	};

/***/ }
/******/ ]);