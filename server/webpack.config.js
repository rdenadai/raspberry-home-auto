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
    node: {fs: "empty"},
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
        app: ['babel-polyfill', './frontend/src/index.js']
    },
    output: {
        path: path.resolve(__dirname, './frontend/static/'),
        filename: 'ds/js/[name]-[hash].js',
        publicPath: 'static/'
    },
    module: {
        loaders: [
            {
                test: /.js?$/,
                exclude: /node_modules/,
                loader: "babel-loader"
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
        // Output extracted CSS to a file
        new ExtractTextPlugin({
            filename: './ds/css/[name]-[hash].css',
            disable: false,
            allChunks: true
        }),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify('production')
            }
        }),
        // Create a service worker
        new webpack.optimize.CommonsChunkPlugin({
            name: "commons",
            filename: './ds/js/[name]-[hash].js',
            chunks: ["commons", "app"]
        }),
        // Uglify javascript
        new webpack.optimize.UglifyJsPlugin({
            comments: false,
            compressor: {
                screw_ie8: true
            }
        }),
        // Deploy everything to template
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, './frontend/templates/') + '/index.tpl.html',
            filename: path.resolve(__dirname, './frontend/templates/') + '/index.html',
            inject: 'body',
            chunks: ["commons", "app"]
        }),
        new SWPrecacheWebpackPlugin({
            cacheId: 'raspberry-home-auto',
            filename: './sw.js',
            maximumFileSizeToCacheInBytes: 10485760,
            directoryIndex: null,
            staticFileGlobs: [
                "frontend/./**.html",
                "frontend/./**.txt",
                "frontend/static/**.js",
                "frontend/static/**.txt",
                "frontend/static/**.json",
                "frontend/static/dist/js/**.js",
                "frontend/static/dist/css/**.css",
                "frontend/static/fonts/**.woff",
                "frontend/static/fonts/**.woff2",
                "frontend/static/fonts/**.eot",
                "frontend/static/fonts/**.svg",
                "frontend/static/fonts/**.ttf",
                "frontend/static/fonts/**.otf",
                "frontend/static/img/**.png",
                "frontend/static/img/icon/**.png"
            ],
            runtimeCaching: [{
              handler: 'cacheFirst',
              urlPattern: /\/$/,
            }],
            verbose: true
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
        })
    ]
};
