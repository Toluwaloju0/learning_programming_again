const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
// const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  mode: 'development',

  entry: {
    header: './js/header/header.js',
    body: './js/body/body.js',
    footer: './js/footer/footer.js'
  },

  devtool: 'inline-source-map',

  devServer: {
    static: './public',
    port: 8564,
    open: true
  },

  // plugins: [
  //   new CleanWebpackPlugin(),
  //   new HtmlWebpackPlugin({
  //     title: 'Holberton Dashboard',
  //   }),
  // ],

  plugins: [
    new HtmlWebpackPlugin({
      title: 'Holberton Dashboard',
      filename: 'index.html',
      chunks: ['header', 'body', 'footer', 'runtime'],  // include all bundles
      inject: 'body',
    }),
  ],

  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'public'),
    clean: true
  },

  module: {
    rules: [
      // CSS
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },

      // IMAGES + optimization
      {
        test: /\.(png|jpe?g|gif|svg)$/i,
        type: 'asset',
        parser: {
          dataUrlCondition: {
            maxSize: 10 * 1024,
          },
        },
        generator: {
          filename: 'images/[hash][ext][query]'
        }
      }
    ]
  },

  optimization: {
    splitChunks: {
      chunks: 'all'
    },
    runtimeChunk: 'single',
  },
};
