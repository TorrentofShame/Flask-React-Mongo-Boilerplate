/* eslint-disable no-var */
const webpack = require("webpack");
const { merge } = require("webpack-merge");

const helpers = require("./helpers");
const common = require("./webpack.common");

/* Plugins */


module.exports = merge(common, {
  mode: "development",
  devtool: "inline-source-map",
  output: {
    filename: "[name].bundle.js",
    publicPath: "/",
    path: helpers.root("dist")
  },
  devServer: {
    contentBase: helpers.root("dist"),
    host: "localhost",
    port: 5000,
    hot: true,
    compress: true
  }
});
