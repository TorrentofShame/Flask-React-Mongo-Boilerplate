const path = require("path");
const helpers = require("./helpers");

module.exports = {
  short_name: "frontend",
  name: "Frontend",
  start_url: "/",
  display: "standalone",
  theme_color: "#000000",
  background_color: "#FFFFFF",
  icons: [
    {
      src: helpers.root("src/assets/favicon.ico"),
      sizes: [48],
      type: "image/x-icon",
      destination: path.join("icons")
    }
  ]
};
