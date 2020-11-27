const path = require("path");
const webpack = require("webpack");

module.exports = {
    entry: ['babel-polyfill', path.resolve(__dirname, "./src/index.js")],
    output: {
        path: path.resolve(__dirname, "./static/frontend/main.js"),
        filename: "[name].js",
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    },
    optimization: {
        minimize: true,
    },
    plugins: [
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: JSON.stringify("production"),
            },
        }),
    ],
};