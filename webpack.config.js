var js = './static/js/';

module.exports = {
    entry: js + 'workout.js',
    output: {
        filename: js + 'app.js'
    },
    loaders:
        [
            {
                test: /\.json$/,
                loader: 'json-loader'
            }
        ]
};
