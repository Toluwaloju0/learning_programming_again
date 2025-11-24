const path = require('path');

module.exports = {
  mode: 'production',

  entry: './js/dashboard-main.js',

  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'public'),
  },

  module: {
    rules: [
      // CSS support
       {
            test: /\.css$/i, // Regex to match .css files
            use: ['style-loader', 'css-loader'], // Apply style-loader then css-loader
        },

    //   Images support + optimization
      {
        test: /\.(png|jpe?g|gif|svg)$/i,
        type: 'asset',
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024, // images < 10kb become base64
          },
        },
        generator: {
          filename: 'images/[hash][ext][query]',
        },
      },
    ],
  },

  optimization: {
    minimize: true,
  },
};
