const path = require("path");

const root = p => {
  return path.resolve(__dirname, "../", p);
}

exports.root = root;
