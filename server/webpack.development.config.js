'use strict';

const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const SWPrecacheWebpackPlugin = require('sw-precache-webpack-plugin');

// Example:
// https://www.youtube.com/watch?v=qPHlCDOzCEk
// To run the scripts use: npm run-script {dev | prod}

module.exports = {
    entry: {
        commons: [
            'react',
            'react-dom',
            'react-addons-transition-group',
            'react-addons-css-transition-group',
            'redux',
            'react-redux',
            'react-router',
            'redux-promise',
            'redux-thunk',
            'redux-form',
            'react-tap-event-plugin',
            'material-ui',
            'lodash',
            'axios',
            'uuid',
            'velocity-animate',
            'moment'
        ],
        app: [
            // 'react-hot-loader/patch',
            // 'webpack-dev-server/client?http://0.0.0.0:8282', // WebpackDevServer host and port
            // 'webpack/hot/only-dev-server', // "only" prevents reload on syntax errors
            'babel-polyfill',
            './frontend/src/index.js'
        ]
    },
    output: {
      path: path.resolve(__dirname, './frontend/static/'),
      filename: 'ds/js/[name].js',
      publicPath: 'static/'
    },
    module: {
        rules: [
            {
                test: /.js?$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                /*query: {
                    plugins: ["react-hot-loader/babel"]
                }*/
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: [{
                        loader: 'style-loader',
                        query: {
                            modules: true,
                            minimize: true
                        }
                    }],
                    use: [
                        {
                            loader: 'css-loader',
                            query: {
                                modules: true,
                                minimize: true,
                                sourceMap: false,
                                importLoaders: true
                            }
                        }
                    ]
                })
            },
            {
                test: /\.woff(\?v=\d+\.\d+\.\d+)?$/,
                loader: "url-loader",
                query: {
                    name: "fonts/fontawesome-webfont.[ext]",
                    limit: 10000,
                    mimetype: "application/font-woff"
                }
            },
            {
                test: /\.woff2(\?v=\d+\.\d+\.\d+)?$/,
                loader: "url-loader",
                query: {
                    name: "fonts/fontawesome-webfont.[ext]",
                    limit: 10000,
                    mimetype: "application/font-woff"
                }
            },
            {
                test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
                loader: "url-loader",
                query: {
                    name: "fonts/fontawesome-webfont.[ext]",
                    limit: 10000,
                    mimetype: "application/octet-stream"
                }
            },
            {
                test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
                loader: "file-loader",
                query: {
                    name: "fonts/fontawesome-webfont.[ext]"
                }
            },
            {
                test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
                loader: "url-loader",
                query: {
                    name: "fonts/fontawesome-webfont.[ext]",
                    limit: 10000,
                    mimetype: "image/svg+xml"
                }
            }
        ]
    },
    plugins: [
        // new webpack.HotModuleReplacementPlugin(),
        // Output extracted CSS to a file
        new ExtractTextPlugin({
            filename: './ds/css/[name].css',
            disable: false,
            allChunks: true
        }),
        // Create a service worker
        new webpack.optimize.CommonsChunkPlugin({
            name: "commons",
            filename: './ds/js/[name].js',
            chunks: ["commons", "app"]
        }),
        // Deploy everything to template
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, './frontend/templates/') + '/index.tpl.html',
            filename: path.resolve(__dirname, './frontend/templates/') + '/index.html',
            inject: 'body',
            chunks: ["commons", "app"]
        }),
        new webpack.LoaderOptionsPlugin({
            options: {
                eslint: {
                    test: /\.js$/,
                    exclude: /node_modules/,
                    configFile: '.eslintrc',
                    failOnWarning: false,
                    failOnError: true
                }
            }
        }),
    ],
    devServer: {
      contentBase: path.resolve(__dirname, './frontend/'),
      devtool: 'eval',
      publicPath: path.resolve(__dirname, './frontend/static/'),
      compress: false,
      hot: true, // Live-reload
      port: 8282, // Port Number
      host: '0.0.0.0', // Change to '0.0.0.0' for external facing server
      inline: true,
      stats: { colors: true }
    },
    devtool: 'eval'
};
