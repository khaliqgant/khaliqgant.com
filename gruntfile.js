module.exports = function(grunt) {
    'use strict';

  var
    project = './static/',
    scss    = project + 'scss/',
    css     = project + 'css/',
    js      = project + 'js/',
    webpack = js + '/pack/',
    npmcss  = require('npm-css');

  grunt.initConfig({

    pkg: grunt.file.readJSON('package.json'),

    clean: [css+'*'],

    sass: {
      dev: {
        files: [{
          expand: true,
          cwd: scss,
          src: [
            '*.scss',
            '!_*.scss'
          ],
          dest: css + 'components',
          ext: '.css'
        }],
        options: {
          compass: true,
          cacheLocation: scss + '.sass_cache',
          style: 'expanded'
        }
      }
    },

    cssmin: {
      combine: {
        files: {
          'static/css/kjg.css': [
            css + 'components/*.css'
          ]
        }
      }
    },

    webpack: {
        pack: {
            entry: webpack + 'workout.js',
            output: {
                filename: js + 'workout-app.js'
            },
            loaders:
                [
                {
                    test: /\.json$/,
                    loader: 'json-loader'
                }
            ]
        }
    },

    concat: {
      options: {
        separator: ';',
      },
      dist: {
        src: [
          js + 'kjg.js'
        ],
        dest: js + 'kjg.js'
      }
    },

    uglify: {
      dist: {
        files: [{
          expand: true,
          cwd: js,
          src: '*.js',
          dest: js
        }]
      }
    },

    jshint: {
        src: [webpack]
    },

    watch: {
      scripts: {
        files: [webpack + '*.js'],
        tasks: ['concat','jshint','uglify']
      },
      styles: {
        files: [scss + '*.scss'],
        tasks: ['clean', 'sass','cssmin']
      }
    }

  });

  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-webpack');

  grunt.registerTask('build', 'def', function(){
      var css = npmcss('static/scss/build/plugins.scss');
      grunt.file.write('static/css/components/plugins.css',css);
  });

  grunt.registerTask('styles', 'def', function(){
    grunt.task.run('sass');
    grunt.task.run('cssmin');
  });

  grunt.registerTask('scripts', 'def', function(){
    grunt.task.run('webpack');
    grunt.task.run('concat');
    grunt.task.run('uglify');
  });

  grunt.registerTask('default', 'def', function(){
    grunt.task.run('styles');
    grunt.task.run('scripts');
  });

};
