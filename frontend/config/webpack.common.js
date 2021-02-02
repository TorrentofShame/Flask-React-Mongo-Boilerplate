/* eslint-disable no-var */
const webpack = require("webpack");

/* Plugins */
const ESLintPlugin = require("eslint-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const WebpackPwaManifest = require("webpack-pwa-manifest");

const manifest = require("./manifest");
const helpers = require("./helpers");

const packageJson = require("../package.json");
const vendorDependencies = Object.keys(packageJson["dependencies"]);

const NODE_ENV = process.env.NODE_ENV;

const babelLoader = {
  loader: "babel-loader",
  options: {
    cacheDirectory: true,
    presets: [
      "@babel/preset-env",
      "@babel/preset-react"
    ],
    plugins: [
      "@babel/plugin-syntax-dynamic-import"
    ]
  }
};

module.exports = {
  entry: {
    main: helpers.root("src/index.jsx"),
    vendor: vendorDependencies
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: [
          babelLoader
        ]
      },
      {
        test: /\.(jpe?g|png|ico|webp|svg|eot|ttf|woff2?)$/i,
        type: "asset/resource",
        generator: {
          filename: "[name].[hash][ext][query]",
        }
      },
      {
        test: /\.html$/,
        use: ["html-loader"]
      },
      {
        test: /\.s[ac]ss$/,
        use: [
          "style-loader",
          {
            loader: "css-loader",
            options: {
              sourceMap: true,
              importLoaders: 1
            }
          },
          "sass-loader"
        ]
      }
    ]
  },
  resolve: {
    extensions: [ ".jsx", ".js", ".scss", ".json", ".html" ],
    alias: {
      _components: helpers.root("src/components"),
      _pages: helpers.root("src/pages"),
      _assets: helpers.root("src/assets"),
      _app: helpers.root("src/app"),
      _styles: helpers.root("src/styles"),
      _utils: helpers.root("src/utils"),
      _webfonts: helpers.root("src/webfonts")
    }
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify(NODE_ENV)
      }
    }),
    new ESLintPlugin({
      extensions: ["js", "jsx"],
      files: ["src"],
      emitError: true,
      emitWarning: true
    }),
    new HtmlWebpackPlugin({
      favicon: helpers.root("public/favicon.png"),
      template: helpers.root("public/index.html")
    }),
    new WebpackPwaManifest({
      filename: "manifest.json",
      inject: true,
      ios: true,
      ...manifest
    }),
    new MiniCssExtractPlugin({
      filename: "[name]-[contenthash].css",
      ignoreOrder: true
    })
  ]
};
